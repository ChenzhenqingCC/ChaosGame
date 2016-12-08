// CCBCheck.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <windows.h>
#include <vector>
#include <map>
#include <io.h>
#include <direct.h>

static void checkCCB( const char* fullPath, FILE* fout, const char* fileName, unsigned int size, const char* rootPath )
{
	FILE* fccb;
	if( fopen_s( &fccb, fullPath, "rb" ) )
		return;

	char folderName[256];
	char texName[256];
	char* data = new char[size*2];
	fread( data, 1, size, fccb );
	fclose( fccb );

	bool bChanged = false;
	unsigned int newSize = size;
	std::string root = rootPath;
	std::string srcTexPath;
	std::string dstTexPath;

	std::string originalFolderName = fileName;
	originalFolderName.erase( originalFolderName.find( ".ccb" ) );
	if( originalFolderName.find( "_" ) != std::string::npos )
	{
		originalFolderName.erase( originalFolderName.find( "_") );
	}

	const char* cur = data;
	while( 1 )
	{
		cur = strstr( cur, ".png" );
		if( !cur )
			break;

		const char* slash = cur;
		const char* slash2 = 0;
		int count = 0;
		while( count != 2 )
		{
			if( *slash == '/' )
			{
				count++;
				if( count == 1 )
					slash2 = slash;
			}
			slash--;
		}
		memcpy( folderName, slash + 2, slash2 - slash - 2 );
		memcpy( texName, slash2 + 1, cur - slash2 - 1 + 4 );
		folderName[slash2 - slash - 2] = '\0';
		texName[cur - slash2 - 1 + 4] = '\0';
		if( !strstr( fileName, folderName ) )
		{
			fprintf( fout, "In %s, using textures [%s] in %s\n", fileName, texName, folderName );
			bool copySucceed = true;

			/// copy texName from folderName to self folder and rename
			std::string originalTexPath = "texture/";
			originalTexPath += folderName;
			originalTexPath += "/";
			originalTexPath += texName;
			std::string convertedTexPath = originalTexPath;
			int srtingPos;
			while( ( srtingPos = convertedTexPath.find( folderName ) ) != std::string::npos )
			{
				convertedTexPath.replace( srtingPos, strlen( folderName ), originalFolderName.c_str() );
			}
			srcTexPath = root + originalTexPath;
			dstTexPath = root + convertedTexPath;
			std::string folderPath = dstTexPath;
			folderPath.erase( folderPath.rfind( "/" ) );
			while( ( srtingPos = folderPath.find( "/" ) ) != std::string::npos )
			{
				folderPath.replace( srtingPos, strlen( "/" ), "\\" );
			}
			_mkdir( folderPath.c_str() );
			if( !CopyFile( srcTexPath.c_str(), dstTexPath.c_str(), true ) )
			{
				copySucceed = false;
			}
			int offset = convertedTexPath.length() - originalTexPath.length();

			/// replace png file names in ccb file
			unsigned int leftSize = newSize - ( cur + 4 - data );
			memmove( ( unsigned char* )cur + 4 + offset, ( unsigned char* )cur + 4, leftSize );
			memcpy( ( unsigned char* )cur + 4 + offset - convertedTexPath.length(), convertedTexPath.data(), convertedTexPath.length() );
			cur += offset;
			newSize += offset;

			bChanged = true;
			fprintf( fout, "Replace [%s] to [%s]: %s\n", originalTexPath.c_str(), convertedTexPath.c_str(), copySucceed ? "---Succeed---" : "***Failed***" );
		}

		cur += 4;
	}

	if( bChanged )
	{
		DWORD  dwAttribute=::GetFileAttributes( fullPath );
		if( dwAttribute & FILE_ATTRIBUTE_READONLY )
		{   
			dwAttribute &= ~FILE_ATTRIBUTE_READONLY;  
			SetFileAttributes( fullPath,dwAttribute );
		}  
		if( !fopen_s( &fccb, fullPath, "wb" ) )
		{
			fwrite( data, newSize, 1, fccb );
			fclose( fccb );
		}
	}

	delete[] data;
}

int _tmain(int argc, _TCHAR* argv[])
{
	std::vector<std::string> folders;
	unsigned int i;
	for( i = 1; i < argc; i++ )
	{
		folders.push_back( argv[i] );
	}
	FILE* fout;
	if( fopen_s( &fout, "./result.txt", "wt" ) )
		return 0;

	const char* path = "./../../../ChaosArt/res/effect_editor/";
	std::vector<std::string>::iterator iter;
	for( iter = folders.begin(); iter != folders.end(); ++iter )
	{
		std::string rootPath = path;
		rootPath += ( *iter );
		rootPath += "/";
		std::string fullPath = rootPath + "*";

		_finddata_t fileinfo;
		intptr_t hFile = _findfirst( fullPath.c_str(), &fileinfo );
		if( hFile == -1 )  
			continue;

		do
		{
			std::string nowPath = rootPath + fileinfo.name;

			if( !( fileinfo.attrib & _A_SUBDIR ) && strstr( fileinfo.name, ".ccb" ) )
			{
				checkCCB( nowPath.c_str(), fout, fileinfo.name, fileinfo.size, rootPath.c_str() );
			}
		}while( _findnext( hFile, &fileinfo ) == 0 ); 
	}

	fclose( fout );

	return 0;
}

