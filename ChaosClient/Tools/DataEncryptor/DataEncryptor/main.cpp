/*
	@ Desc:		Data descryptor
	@ Author:	siriushuang
*/
#include <stdlib.h>
#include <stdio.h>
#include <string>
#ifdef WIN32
#include <windows.h>
#include <io.h>
#else
#include <sys/types.h>
#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h>
#include <libgen.h>
#endif
#include <map>
#include <iostream>
#include "../../../Client/Client/Classes/Utility/DataEncrypt.h"

static std::map<std::string, bool> generatedFiles;

static void printUsage()
{
	printf( "DataEncryptor [-encrypt|-decrypt] [-name|-noname](file name encryption) fullfilepath extension(etc, .lua )\n" );
	printf( "DataEncryptor test encrypt|decrypt filepath dstfilepath\n" );
}

#ifdef WIN32
static void testEncrypt( bool isEncrypt, CDataEncrypt* pDecrypt, const char* path, const char* dstpath )
{
	char exePath[MAX_PATH];
	::GetCurrentDirectory( MAX_PATH, exePath );
	strcat( exePath, "\\" );

	std::string srcPath = exePath;
	srcPath += path;
	std::string dstPath = exePath;
	dstPath += dstpath;

	FILE* fp = NULL;
	if( fopen_s( &fp, srcPath.c_str(), "rb" ) )
	{
		return;
	}

	fseek( fp, 0, SEEK_END );
	unsigned int fileSize = ftell( fp );
	fseek( fp, 0, SEEK_SET );
	unsigned char* pData = new unsigned char[fileSize];
	fread( pData, fileSize, 1, fp );
	fclose( fp );

	unsigned int outLength = pDecrypt->GetOutputLength( pData, fileSize, isEncrypt );
	unsigned char* pFileOutData = new unsigned char[outLength];
	if( isEncrypt )
		pDecrypt->Encrypt( FILE_DATA_ENCRYPT_KEY, pData, pFileOutData, fileSize, &outLength );
	else
		pDecrypt->Decrypt( FILE_DATA_ENCRYPT_KEY, pData, pFileOutData, fileSize, &outLength );

	fp = NULL;
	if( fopen_s( &fp, dstPath.c_str(), "wb" ) )
	{
		return;
	}
	fwrite( pFileOutData, outLength, 1, fp );
	fclose( fp );

	delete[] pFileOutData;
	delete[] pData;
}

static void processPath_win32( CDataEncrypt* pDecrypt, CDataEncrypt* pFileNameEncryptor, const char* path, const char* extName, bool isEncrypt, bool isFileNameEncrypt, const char* nameKey, const char* fileKey )
{
	intptr_t hFile;
    _finddata_t fileinfo;  
	std::string root;
    root.assign( path );
	int len = root.length();  
  
	if( path[len-1] != '\\' )
	{  
		root.append( "\\" );  
	}  
	std::string findPath = root + "*";

	hFile = _findfirst( findPath.c_str(), &fileinfo );  
	if( hFile == -1 )  
		return;  

	do
	{  
		std::string nowPath = root + fileinfo.name;
		if( generatedFiles.find( nowPath ) != generatedFiles.end() )
			continue;

		if( !( fileinfo.attrib & _A_SUBDIR ) && strstr( fileinfo.name, extName ) )
		{
			FILE* fp;
			fopen_s( &fp, nowPath.c_str(), "rb" );
			fpos_t start, end;
			fseek( fp, 0, SEEK_SET );
			fgetpos( fp, &start );
			fseek( fp, 0, SEEK_END );
			fgetpos( fp, &end );
			fpos_t fileLen = end - start;
			unsigned char* pFileData = new unsigned char[fileLen];
			fseek( fp, 0, SEEK_SET );
			fread( pFileData, fileLen, 1, fp );
			fclose( fp );

			unsigned char* pXorFileOutData = NULL;
			unsigned int xorOutLength;
			if( isEncrypt )
			{
				unsigned int outLength = pDecrypt->GetOutputLength( pFileData, fileLen, isEncrypt );
				unsigned char* pFileOutData = new unsigned char[outLength];
				if( isEncrypt )
					pDecrypt->Encrypt( fileKey, pFileData, pFileOutData, fileLen, &outLength );
				else
					pDecrypt->Decrypt( fileKey, pFileData, pFileOutData, fileLen, &outLength );
				delete[] pFileData;

				xorOutLength = pFileNameEncryptor->GetOutputLength( pFileOutData, outLength, isEncrypt );
				pXorFileOutData = new unsigned char[xorOutLength];
				if( isEncrypt )
					pFileNameEncryptor->Encrypt( fileKey, pFileOutData, pXorFileOutData, outLength, &xorOutLength );
				else
					pFileNameEncryptor->Decrypt( fileKey, pFileOutData, pXorFileOutData, outLength, &xorOutLength );
				delete[] pFileOutData;
			}
			else
			{
				xorOutLength = CResourceDecryptUtil::DecryptorData( fileKey, pFileData, &pXorFileOutData, fileLen );
			}

			::SetFileAttributes( nowPath.c_str(), FILE_ATTRIBUTE_NORMAL );
			::DeleteFile( nowPath.c_str() );

			if( isEncrypt && isFileNameEncrypt )
			{
				const char* newFileName = CResourceDecryptUtil::EncryptorFilename( nameKey, fileinfo.name );
				nowPath = root + newFileName;
				delete[] newFileName;
			}
			else if( !isEncrypt && isFileNameEncrypt )
			{
				const char* newFileName = CResourceDecryptUtil::DecryptorFilename( nameKey, fileinfo.name );
				nowPath = root + newFileName;
				delete[] newFileName;
			}

			fopen_s( &fp, nowPath.c_str(), "wb" );
			fseek( fp, 0, SEEK_SET );
			fwrite( pXorFileOutData, xorOutLength, 1, fp );
			fclose( fp );
			generatedFiles.insert( std::make_pair( nowPath, true ) );
			if( pXorFileOutData )
				delete[] pXorFileOutData;
		}
		else
		{
			if( strcmp( fileinfo.name, "." ) == 0 || strcmp( fileinfo.name, ".." ) == 0 )
				continue;
			processPath_win32( pDecrypt, pFileNameEncryptor, nowPath.c_str(), extName, isEncrypt, isFileNameEncrypt, nameKey, fileKey );
		}
	}while( _findnext( hFile, &fileinfo ) == 0 ); 
}
#else
static void processPath_mac( CDataEncrypt* pDecrypt, CDataEncrypt* pFileNameEncryptor, const char* path, const char* extName, bool isEncrypt, bool isFileNameEncrypt, const char* nameKey, const char* fileKey )
{
    DIR* d;
    struct dirent* file;
    struct stat sb;
    
    std::string root;
    root.assign( path );
	int len = root.length();
    
	if( path[len-1] != '/' )
	{
		root.append( "/" );
	}
	std::string findPath = root;
    
    if( !( d = opendir( findPath.c_str() ) ) )
    {
        printf( "open dir fail\n" );
        return;
    }
    
    while( ( file = readdir( d ) ) != NULL )
    {
        std::string nowPath = root + file->d_name;
		if( generatedFiles.find( nowPath ) != generatedFiles.end() )
			continue;
        
        if( stat( nowPath.c_str(), &sb ) < 0 )
            continue;
        
        if( S_ISDIR( sb.st_mode ) )
        {
            if( strcmp( file->d_name, "." ) == 0 || strcmp( file->d_name, ".." ) == 0 )
				continue;
            
            processPath_mac( pDecrypt, pFileNameEncryptor, nowPath.c_str(), extName, isEncrypt, isFileNameEncrypt, nameKey, fileKey );
        }
        else if( strcmp( file->d_name, ".DS_Store" ) != 0 && strstr( file->d_name, extName ) )
        {
            FILE* fp;
			fp = fopen( nowPath.c_str(), "rb" );
			fpos_t start, end;
			fseek( fp, 0, SEEK_SET );
			fgetpos( fp, &start );
			fseek( fp, 0, SEEK_END );
			fgetpos( fp, &end );
			fpos_t fileLen = end - start;
			unsigned char* pFileData = new unsigned char[fileLen];
			fseek( fp, 0, SEEK_SET );
			fread( pFileData, fileLen, 1, fp );
			fclose( fp );
            
			unsigned char* pXorFileOutData = NULL;
			unsigned int xorOutLength;
			if( isEncrypt )
			{
				unsigned int outLength = pDecrypt->GetOutputLength( pFileData, fileLen, isEncrypt );
				unsigned char* pFileOutData = new unsigned char[outLength];
				if( isEncrypt )
					pDecrypt->Encrypt( fileKey, pFileData, pFileOutData, fileLen, &outLength );
				else
					pDecrypt->Decrypt( fileKey, pFileData, pFileOutData, fileLen, &outLength );
				delete[] pFileData;
                
				xorOutLength = pFileNameEncryptor->GetOutputLength( pFileOutData, outLength, isEncrypt );
				pXorFileOutData = new unsigned char[xorOutLength];
				if( isEncrypt )
					pFileNameEncryptor->Encrypt( fileKey, pFileOutData, pXorFileOutData, outLength, &xorOutLength );
				else
					pFileNameEncryptor->Decrypt( fileKey, pFileOutData, pXorFileOutData, outLength, &xorOutLength );
				delete[] pFileOutData;
			}
			else
			{
				xorOutLength = CResourceDecryptUtil::DecryptorData( fileKey, pFileData, &pXorFileOutData, fileLen );
			}
            
            chmod( nowPath.c_str(), S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH );
			remove( nowPath.c_str() );
            
			if( isEncrypt && isFileNameEncrypt )
			{
				const char* newFileName = CResourceDecryptUtil::EncryptorFilename( nameKey, file->d_name );
				nowPath = root + newFileName;
				delete[] newFileName;
			}
			else if( !isEncrypt && isFileNameEncrypt )
			{
				const char* newFileName = CResourceDecryptUtil::DecryptorFilename( nameKey, file->d_name );
				nowPath = root + newFileName;
				delete[] newFileName;
			}
            
			fp = fopen( nowPath.c_str(), "wb" );
			fseek( fp, 0, SEEK_SET );
			fwrite( pXorFileOutData, xorOutLength, 1, fp );
			fclose( fp );
			generatedFiles.insert( std::make_pair( nowPath, true ) );
			if( pXorFileOutData )
				delete[] pXorFileOutData;
        }
    }
    closedir( d );
}
#endif

int main( int argc, char* argv[] )
{
	if( argc == 5 && strcmp( argv[1], "test" ) == 0 )
	{
		CDataEncrypt* pEncryptor = new CGZEncrypt();
		bool isEncrypt = false;
		if( strcmp( argv[2], "encrypt" ) == 0 )
			isEncrypt = true;
		testEncrypt( isEncrypt, pEncryptor, argv[3], argv[4] );
		delete pEncryptor;
		return 0;
	}

	if( argc != 5 )
	{
		printUsage();
		return 1;
	}

	bool isEncrypt = false;
	if( strcmp( argv[1], "-encrypt" ) == 0 )
		isEncrypt = true;
	else if( strcmp( argv[1], "-decrypt" ) == 0 )
		isEncrypt = false;
	else
	{
		printUsage();
		return 1;
	}

	bool isFileNameEncrypt = false;
	if( strcmp( argv[2], "-name" ) == 0 )
		isFileNameEncrypt = true;
	else if( strcmp( argv[2], "-noname" ) == 0 )
		isFileNameEncrypt = false;
	else
	{
		printUsage();
		return 1;
	}

	std::string fullFilePath = argv[3];
	std::string extName = argv[4];

	generatedFiles.clear();
	CDataEncrypt* pEncryptor = new CGZEncrypt();
	CDataEncrypt* pFileNameEncrypt = new CXorEncrypt();
#ifdef WIN32
	char exePath[MAX_PATH];
	::GetCurrentDirectory( MAX_PATH, exePath );
	strcat( exePath, "\\" );
	strcat( exePath, fullFilePath.c_str() );
	processPath_win32( pEncryptor, pFileNameEncrypt, exePath, extName.c_str(), isEncrypt, isFileNameEncrypt, FILE_NAME_ENCRYPT_KEY, FILE_DATA_ENCRYPT_KEY );
	///--for test processPath_win32( pEncryptor, pFileNameEncrypt, fullFilePath.c_str(), !isEncrypt, !isFileNameEncrypt, FILE_NAME_ENCRYPT_KEY, FILE_DATA_ENCRYPT_KEY );
#else
    chdir( dirname( argv[0] ) );
    processPath_mac( pEncryptor, pFileNameEncrypt, fullFilePath.c_str(), extName.c_str(), isEncrypt, isFileNameEncrypt, FILE_NAME_ENCRYPT_KEY, FILE_DATA_ENCRYPT_KEY );
#endif // WIN32

	delete pFileNameEncrypt;
	delete pEncryptor;

	return 0;
}