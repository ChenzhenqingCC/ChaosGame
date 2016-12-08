// VerDiffer.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>
#include <windows.h>
#include <stdlib.h>
#include <string>
#include <windows.h>
#include <vector>
#include <map>
#include <io.h>
#include <direct.h>
#include "md5.h"
#include "../../../Client/Client/Classes/Utility/DataEncrypt.h"

/// usage: VerDiffer srcVer dstVer region root platform path
/// sample: VerDiffer 0.1.347.347 0.1.347.355 1 E:\share\publish\versions pc data
/// package geneate path: root\region\srcVer_to_dstVer.zip

static void md5ToString( unsigned char* md5, std::string& md5Str )
{
	char md5buf[32];
	unsigned int i;
	for( i = 0; i < 16; i++ )
	{
		sprintf_s( md5buf, 32, "%02x", md5[i] );
		md5Str.append( md5buf );
	}
}

static void generateMd5( const char* rootPath, const char* relativePath, std::map<std::string, std::string>& md5Map )
{
	intptr_t hFile;
    _finddata_t fileinfo;
	std::string root;
    root.assign( rootPath );
	root = root + "\\";
	std::string findPath = root + "*";

	hFile = _findfirst( findPath.c_str(), &fileinfo );  
	if( hFile == -1 )  
		return;

	do
	{
		std::string nowPath = root + fileinfo.name;
		std::string relPath = relativePath;
		relPath += "/";
		relPath += fileinfo.name;
		if( !( fileinfo.attrib & _A_SUBDIR ) )
		{
			FILE* fp = NULL;
			if( fopen_s( &fp, nowPath.c_str(), "rb" ) )
				continue;

			unsigned char* data = new unsigned char[fileinfo.size];
			fread( data, fileinfo.size, 1, fp );
			fclose( fp );

			std::string md5String;
			unsigned char digset[16];
			MD5_CTX md5Ctx;
			MD5Init( &md5Ctx );
			MD5Update( &md5Ctx, data, fileinfo.size );
			MD5Final( &md5Ctx, digset );
			md5ToString( digset, md5String );
			md5Map.insert( std::make_pair( relPath, md5String ) );

			delete[] data;
		}
		else
		{
			if( strcmp( fileinfo.name, "." ) == 0 || strcmp( fileinfo.name, ".." ) == 0 )
				continue;
			generateMd5( nowPath.c_str(), relPath.c_str(), md5Map );
		}
	}while( _findnext( hFile, &fileinfo ) == 0 ); 
}

static void generateFullPath( const char* relPath, const char* rootPath, std::string& fullPath )
{
	fullPath = rootPath;
	fullPath += relPath;
	unsigned int length = fullPath.length();
	char* charData = ( char* )fullPath.data();
	for( unsigned int i = 0; i < length; i++ )
	{
		if( charData[i] == '/' )
		{
			charData[i] = '\\';
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc != 7 )
	{
		printf( "VerDiffer srcVer dstVer region root platform path\n" );
		return 1;
	}

	std::string srcVer = argv[1];
	std::string dstVer = argv[2];
	std::string region = argv[3];
	std::string root = argv[4];
	std::string platform = argv[5];
	std::string path = argv[6];

	std::string srcPath = root + "\\" + region + "\\" + srcVer + "\\data\\" + platform + "\\Output\\" + path;
	std::string dstPath = root + "\\" + region + "\\" + dstVer + "\\data\\" + platform + "\\Output\\" + path;
	std::string relativePath = path;

	std::map<std::string, std::string> srcMd5Maps;
	std::map<std::string, std::string> dstMd5Maps;
	generateMd5( srcPath.c_str(), relativePath.c_str(), srcMd5Maps );
	generateMd5( dstPath.c_str(), relativePath.c_str(), dstMd5Maps );

	// differ files
	std::vector<std::string> updateList;
	std::map<std::string, std::string>::iterator srcIter;
	std::map<std::string, std::string>::iterator dstIter;
	for( dstIter = dstMd5Maps.begin(); dstIter != dstMd5Maps.end(); ++dstIter )
	{
		if( ( srcIter = srcMd5Maps.find( ( dstIter->first ) ) ) == srcMd5Maps.end() || dstIter->second.compare( srcIter->second.c_str() ) != 0 )
		{
			updateList.push_back( dstIter->first );
			continue;
		}
	}

	// generate zip file
	FILE* fpOut = NULL;
	std::string zipFile = root + "\\" + region + "\\" + platform + "\\" + srcVer + "_to_" + dstVer + ".zip";
	std::string zipPath = root + "\\" + region + "\\" + platform;
	_mkdir( zipPath.c_str() );
	if( fopen_s( &fpOut, zipFile.c_str(), "wb" ) )
	{
		printf( "Can't create zip file!\n" );
		return 1;
	}

	// write total file number
	unsigned int totalNumber = updateList.size();
	fwrite( &totalNumber, sizeof( unsigned int ), 1, fpOut );

	// write zip file
	std::string rootPath = root + "\\" + region + "\\" + dstVer + "\\data\\" + platform + "\\Output\\";
	std::vector<std::string>::iterator iter;
	for( iter = updateList.begin(); iter != updateList.end(); ++iter )
	{
		relativePath = *iter;
		std::string fullPath;
		generateFullPath( relativePath.c_str(), rootPath.c_str(), fullPath );

		FILE* fp = NULL;
		if( fopen_s( &fp, fullPath.c_str(), "rb" ) )
		{
			printf( "can't find file when prepare verdiff : %s\n", relativePath );
			return 1;
		}

		fseek( fp, 0, SEEK_END );
		unsigned int fileSize = ftell( fp );
		fseek( fp, 0, SEEK_SET );
		unsigned char* pData = new unsigned char[fileSize];
		fread( pData, fileSize, 1, fp );
		fclose( fp );

		// make file zip
		CGZEncrypt gzDecryptor;
		unsigned int outLength = gzDecryptor.GetOutputLength( pData, fileSize, true );
		unsigned char* pFileOutData = new unsigned char[outLength];
		gzDecryptor.Encrypt( FILE_DATA_ENCRYPT_KEY, pData, pFileOutData, fileSize, &outLength );

		// write to file
		fwrite( relativePath.data(), relativePath.length() + 1, 1, fpOut );
		fwrite( &outLength, sizeof( unsigned int ), 1, fpOut );
		fwrite( pFileOutData, outLength, 1, fpOut );

		delete[] pFileOutData;
		delete[] pData;
	}
	fclose( fpOut );
	printf( "Generate patch file successfully: %s!\n", zipFile.c_str() );

	return 0;
}

