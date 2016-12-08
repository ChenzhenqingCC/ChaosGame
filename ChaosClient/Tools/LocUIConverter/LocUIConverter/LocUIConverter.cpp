// LocUIConverter.cpp : 定义控制台应用程序的入口点。
// command:
//		LocUIConverter vnm ui_editor ..\..\..\ChaosArt\res ..\..\Client\Output data\ccb\texture
//		call LocUIConverter_bat

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <windows.h>
#include <vector>
#include <map>
#include <io.h>
#include <direct.h>
#include <assert.h>

static void replaceSlash( std::string& str )
{
	unsigned int i;
	for( i = 0; i < str.length(); i++ )
	{
		char* word = ( char* )str.data();
		if( word[i] == '/' )
		{
			word[i] = '\\';
		}
	}
}

static bool copyRelativeTexture( const char* srcTexPath, const char* srcFolder, const char* dstPath, const char* dstFolder, const char* srcLocTexPath, bool isLoced, FILE* fout )
{
	// fprintf( fout, "xcopy /Y /Q /R /E %s\\%s %s\\texture\\work\\%s\\\n", srcTexPath, srcFolder.c_str(), dstPath, dstFolder.c_str() );
	// "*_rep_" as the key
	if( strstr( srcFolder, "_rep_" ) != NULL )
	{
		std::string fullpath = srcTexPath;
		fullpath += "\\";
		fullpath += srcFolder;
		fullpath = fullpath.erase( fullpath.rfind( "_rep_" ) + 5 );
		fullpath += "*.png";

		_finddata_t fileinfo;
		intptr_t hFile = _findfirst( fullpath.c_str(), &fileinfo );
		if( hFile == -1 )  
			return isLoced;

		do
		{
			if( strstr( srcFolder, fileinfo.name ) == NULL )
			{
				std::string newSrcFolder = srcFolder;
				newSrcFolder = newSrcFolder.erase( newSrcFolder.rfind( "\\" ) );
				newSrcFolder += "\\";
				newSrcFolder += fileinfo.name;
				fprintf( fout, "xcopy /Y /Q /R /E %s\\%s %s\\work\\%s\\\n", srcTexPath, newSrcFolder.c_str(), dstPath, dstFolder );

				// copy loc textures
				std::string srcLocPng = srcLocTexPath;
				srcLocPng = srcLocPng + "\\" + fileinfo.name;
				if( ::GetFileAttributes( srcLocPng.c_str() ) != -1 )
				{
					// exist
					isLoced = true;
					fprintf( fout, "xcopy /Y /Q /R /E %s %s\\work\\%s\\\n", srcLocPng.c_str(), dstPath, dstFolder );
				}
			}
		}while( _findnext( hFile, &fileinfo ) == 0 ); 
	}
	return isLoced;
}

std::string&   replace_all(std::string&   str,const   std::string&   old_value,const   std::string&   new_value)   
{   
	while(true)   {   
		std::string::size_type   pos(0);   
		if(   (pos=str.find(old_value))!=std::string::npos   )   
			str.replace(pos,old_value.length(),new_value);   
		else   break;   
	}   
	return   str;   
} 

static void convertUITexture( const char* srcCCBPath, const char* srcTexPath, const char* srcLocTexPath, const char* dstTexPath, FILE* fout , const char* rootCCBPath, const char* locCCBPath)
{
	std::string rootPath = srcCCBPath;
	rootPath += "\\";
	std::string fullPath = rootPath + "*";

	_finddata_t fileinfo;
	intptr_t hFile = _findfirst( fullPath.c_str(), &fileinfo );
	if( hFile == -1 )  
		return;

	do
	{
		std::string nowPath = rootPath + fileinfo.name;

		if( fileinfo.attrib & _A_SUBDIR )
		{
			if( strcmp( fileinfo.name, "." ) == 0 || strcmp( fileinfo.name, ".." ) == 0 )
				continue;
			convertUITexture( nowPath.c_str(), srcTexPath, srcLocTexPath, dstTexPath, fout, rootCCBPath, locCCBPath);
		}
		else if( strstr( fileinfo.name, ".ccb" ) )
		{
			fprintf( fout, "md %s\\work\n", dstTexPath );

			std::string tagPath = nowPath;
				
			replace_all(tagPath, rootCCBPath, locCCBPath);

			FILE* fccb;
			if(fopen_s(&fccb, tagPath.c_str(),"rb"))
				if( fopen_s( &fccb, nowPath.c_str(), "rb" ) )
					continue;
			

			char* data = new char[fileinfo.size];
			fread( data, 1, fileinfo.size, fccb );
			fclose( fccb );

			std::map<std::string, std::string> pngs;
			const char* cur = data;
			while( 1 )
			{
				cur = strstr( cur, ".png" );
				if( !cur )
					break;

				char fullPngPath[256];
				const char* find = cur;
				bool isFound = true;
				while( 1 )
				{
					int length = cur - find;
					assert( length < 256 );
					if( length > 0 )
					{
						memcpy( fullPngPath, find, length );
					}
					fullPngPath[length] = '\0';
					if( strstr( fullPngPath, "texture/" ) == fullPngPath )
					{
						break;
					}
					else if( strstr( fullPngPath, "<string>" ) == fullPngPath )
					{
						isFound = false;
						break;
					}
					find--;
				}
				if( isFound )
				{
					strcat_s( fullPngPath, ".png" );
					if( pngs.find( fullPngPath ) == pngs.end() )
					{
						std::string pngFile = fullPngPath;
						pngFile = pngFile.substr( pngFile.rfind( "/" ) + 1 );
						pngs[fullPngPath] = pngFile;
					}
				}
				cur += 4;
			}
			delete[] data;

			/// make plist and png
			bool isLoced = false;
			std::string ccbname = fileinfo.name;
			ccbname = ccbname.erase( ccbname.find( ".ccb" ) );
			std::string pngstr;
			std::map<std::string, std::string>::iterator iter;
			for( iter = pngs.begin(); iter != pngs.end(); ++iter )
			{
				pngstr += iter->first;
				pngstr += " ";

				std::string srcFolder = iter->first;
				std::string dstFolder = srcFolder;
				dstFolder = dstFolder.erase( dstFolder.rfind( "/" ) );
				replaceSlash( srcFolder );
				replaceSlash( dstFolder );
				fprintf( fout, "xcopy /Y /Q /R /E %s\\%s %s\\work\\%s\\\n", srcTexPath, srcFolder.c_str(), dstTexPath, dstFolder.c_str() );

				// copy loc textures
				std::string srcLocPng = srcLocTexPath;
				srcLocPng = srcLocPng + "\\" + iter->second.c_str();
				if( ::GetFileAttributes( srcLocPng.c_str() ) != -1 )
				{
					// exist
					isLoced = true;
					fprintf( fout, "xcopy /Y /Q /R /E %s %s\\work\\%s\\\n", srcLocPng.c_str(), dstTexPath, dstFolder.c_str() );
				}

				isLoced = copyRelativeTexture( srcTexPath, srcFolder.c_str(), dstTexPath, dstFolder.c_str(), srcLocTexPath, isLoced, fout );
			}
			if( pngstr.length() && isLoced )
			{
				pngstr = pngstr.erase( pngstr.length() - 1 );
				if( ccbname.find( "mirentereff" ) != std::string::npos )
					fprintf( fout, "TexturePacker --texture-format png --allow-free-size --size-constraints POT --force-squared --extrude 1 --disable-rotation --opt RGBA8888 --trim-mode None --data %s/%s.plist --format cocos2d --sheet %s/%s.png %s\\work\\texture\n", dstTexPath, ccbname.c_str(), dstTexPath, ccbname.c_str(), dstTexPath );
				else
					fprintf( fout, "TexturePacker --texture-format png --allow-free-size --size-constraints POT --force-squared --extrude 1 --enable-rotation --opt RGBA8888 --trim-mode None --data %s/%s.plist --format cocos2d --sheet %s/%s.png %s\\work\\texture\n", dstTexPath, ccbname.c_str(), dstTexPath, ccbname.c_str(), dstTexPath );
			}

			fprintf( fout, "rd /s /q %s\\work\n", dstTexPath );
		}
	}while( _findnext( hFile, &fileinfo ) == 0 );
}

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc != 6 )
		return 0;

	std::string language = argv[1];
	std::string srcCCBFolder = argv[2];
	std::string srcPath = argv[3];
	std::string dstPath = argv[4];
	std::string dstCCBTexFolder = argv[5];

	FILE* fout;
	if( fopen_s( &fout, ".\\LocUIConverter_bat.bat", "wt" ) )
		return 0;

	std::string srcCCBPath = srcPath + "\\" + srcCCBFolder;
	std::string srcCCBTexPath = srcPath + "\\loc\\" + language + "\\ui";
	std::string dstCCBTexPath = dstPath + "\\loc\\" + language + "\\" + dstCCBTexFolder;
	std::string locCCBPath = srcPath + "\\loc\\" + language + "\\" + srcCCBFolder;

	// clear generated textures
	fprintf( fout, "rd /s /q %s\n", dstCCBTexPath.c_str() );
	fprintf( fout, "md %s\n", dstCCBTexPath.c_str() );

	char buf[MAX_PATH+1];  
	GetCurrentDirectory( MAX_PATH, buf );
	std::string fullDstPath = buf;
	fullDstPath += "\\";
	fullDstPath += dstCCBTexPath;

	convertUITexture( srcCCBPath.c_str(), srcCCBPath.c_str(), srcCCBTexPath.c_str(), dstCCBTexPath.c_str(), fout, srcCCBPath.c_str(), locCCBPath.c_str());

	fclose( fout );

	return 0;
}

