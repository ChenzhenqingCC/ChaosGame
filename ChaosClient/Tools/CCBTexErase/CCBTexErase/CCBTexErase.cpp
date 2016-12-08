// CCBTexErase.cpp : 定义控制台应用程序的入口点。
// 参数2：
//		1.ccb的总目录
//		2.texture的总目录

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <windows.h>
#include <vector>
#include <map>
#include <io.h>
#include <direct.h>

static void getAllPng( std::map<std::string, std::string>& pngMaps, const char* pngPath )
{
	std::string searchPath = pngPath;
	searchPath += "/*";

	_finddata_t fileinfo;
	intptr_t hFile = _findfirst( searchPath.c_str(), &fileinfo );
	if( hFile == -1 )  
		return;

	do
	{
		if( !( fileinfo.attrib & _A_SUBDIR ) )
		{
			if( strstr( fileinfo.name, ".png" ) )
			{
				std::string totalPath = pngPath;
				std::string keyPath = pngPath;
				keyPath.erase( 0, keyPath.rfind( "/" ) + 1 );
				keyPath += "/";
				keyPath += fileinfo.name;
				totalPath += "/";
				totalPath += fileinfo.name;

				pngMaps[keyPath] = totalPath;
			}
		}
		else
		{
			if( strcmp( fileinfo.name, "." ) == 0 || strcmp( fileinfo.name, ".." ) == 0 )
				continue;

			std::string newPath = pngPath;
			newPath += "/";
			newPath += fileinfo.name;
			getAllPng( pngMaps, newPath.c_str() );
		}
	}while( _findnext( hFile, &fileinfo ) == 0 ); 
}

static void checkCCB( std::map<std::string, std::string>& pngMaps, const char* ccbPath, unsigned int size )
{
	FILE* fccb;
	if( fopen_s( &fccb, ccbPath, "rb" ) )
		return;

	char* data = new char[size*2];
	fread( data, 1, size, fccb );
	fclose( fccb );

	char folderName[256];
	char texName[256];
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

		std::string originalTexPath = folderName;
		originalTexPath += "/";
		originalTexPath += texName;

		std::map<std::string, std::string>::iterator iter = pngMaps.find( originalTexPath.c_str() );
		if( iter != pngMaps.end() )
		{
			pngMaps.erase( iter );
		}
		cur += 4;
	}

	delete[] data;
}

static void checkAllCCB( std::map<std::string, std::string>& pngMaps, const char* ccbPath )
{
	std::string searchPath = ccbPath;
	searchPath += "/*";

	_finddata_t fileinfo;
	intptr_t hFile = _findfirst( searchPath.c_str(), &fileinfo );
	if( hFile == -1 )  
		return;

	do
	{
		if( !( fileinfo.attrib & _A_SUBDIR ) )
		{
			if( strstr( fileinfo.name, ".ccb" ) )
			{
				std::string totalPath = ccbPath;
				totalPath += "/";
				totalPath += fileinfo.name;

				checkCCB( pngMaps, totalPath.c_str(), fileinfo.size );
			}
		}
		else
		{
			if( strcmp( fileinfo.name, "." ) == 0 || strcmp( fileinfo.name, ".." ) == 0 )
				continue;

			std::string newPath = ccbPath;
			newPath += "/";
			newPath += fileinfo.name;
			checkAllCCB( pngMaps, newPath.c_str() );
		}
	}while( _findnext( hFile, &fileinfo ) == 0 ); 
}

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc != 3 )
		return 0;
	
	char outputFileName[256];
	sprintf_s( outputFileName, 256, "./erase_result_%s.txt", strrchr( argv[1], '/' ) + 1 );

	FILE* fout;
	if( fopen_s( &fout, outputFileName, "wt" ) )
		return 0;

	std::string ccbPath = argv[1];
	std::string pngPath = argv[2];

	std::map<std::string, std::string> pngMaps;	// key dir/tex.png, value is fullpath
	getAllPng( pngMaps, pngPath.c_str() );

	checkAllCCB( pngMaps, ccbPath.c_str() );

	unsigned int size = 0;
	_finddata_t fileinfo;
	std::map<std::string, std::string>::iterator iter;
	for( iter = pngMaps.begin(); iter != pngMaps.end(); ++iter )
	{
		intptr_t hFile = _findfirst( iter->second.c_str(), &fileinfo );
		if( hFile != -1 )
		{
			size += fileinfo.size;
		}
		fprintf( fout, "Unused texture [%s], size:%d\n", iter->first.c_str(), fileinfo.size );

		/// delete file
		DWORD  dwAttribute=::GetFileAttributes( iter->second.c_str() );
		if( dwAttribute & FILE_ATTRIBUTE_READONLY )
		{   
			dwAttribute &= ~FILE_ATTRIBUTE_READONLY;  
			SetFileAttributes( iter->second.c_str(),dwAttribute );
		}
		DeleteFile( iter->second.c_str() );
	}
	fprintf( fout, "Total unused texture size:%d\n", size );

	fclose( fout );

	return 0;
}

