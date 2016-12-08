// LuajitListGen.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <windows.h>
#include <vector>
#include <map>
#include <io.h>

#define SRC_TYPE ".lua"
#define DST_TYPE ".obj"

static void processFolder( const char* fullPath, const char* rootPath, const char* dstRootPath, FILE* batFile )
{
	_finddata_t fileinfo;
	intptr_t hFile = _findfirst( fullPath, &fileinfo );
	if( hFile == -1 )  
		return;

	do
	{
		std::string nowPath = rootPath;
		nowPath += fileinfo.name;
		std::string newDstRootPath = dstRootPath;
		newDstRootPath += fileinfo.name;
		if( !( fileinfo.attrib & _A_SUBDIR ) )
		{
			if( strstr( fileinfo.name, SRC_TYPE ) )
			{
				newDstRootPath.replace( newDstRootPath.rfind( SRC_TYPE ), strlen( SRC_TYPE ), DST_TYPE );
				fprintf( batFile, ".\\..\\..\\Client\\scripting\\lua\\luajit\\LuaJIT-2.0.1\\x86_bin\\luajit -b %s %s\n", nowPath.c_str(), newDstRootPath.c_str() );
			}
		}
		else
		{
			if( strcmp( fileinfo.name, "." ) == 0 || strcmp( fileinfo.name, ".." ) == 0 )
				continue;

			nowPath += "\\";
			std::string newFullPath = nowPath + "*";
			fprintf( batFile, "md %s\n", newDstRootPath.c_str() );
			newDstRootPath += "\\";
			processFolder( newFullPath.c_str(), nowPath.c_str(), newDstRootPath.c_str(), batFile );
		}
	}while( _findnext( hFile, &fileinfo ) == 0 ); 
}

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc != 4 )
	{
		printf( "Usage: LuajitListGen src dst batfile ( relative to 'data/' folder )" );
		return 0;
	}

	FILE* batFile = NULL;
	if( fopen_s( &batFile, argv[3], "wt" ) )
		return 0;

	const char* path = ".\\..\\..\\Client\\Output\\data\\";
	std::string srcFolder = argv[1];
	std::string dstFolder = argv[2];

	std::string rootPath = path;
	rootPath += srcFolder;
	rootPath += "\\";
	std::string fullPath = rootPath + "*";
	std::string dstRootPath = path;
	dstRootPath += dstFolder;

	fprintf( batFile, "rd /s /q %s\n", dstRootPath.c_str() );
	fprintf( batFile, "md %s\n", dstRootPath.c_str() );
	dstRootPath += "\\";
	processFolder( fullPath.c_str(), rootPath.c_str(), dstRootPath.c_str(), batFile );

	fclose( batFile );

	return 0;
}

