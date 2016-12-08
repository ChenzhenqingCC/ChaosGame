// ResConverter.cpp : 定义控制台应用程序的入口点。
// command:
//		ResConverter effect ..\..\..\ChaosArt\res\effect_editor_publish\comeff ..\..\Client\Output\data\obj\ccb\comeff
//		ResConverter effect ..\..\..\ChaosArt\res\effect_editor_publish\mireff ..\..\Client\Output\data\obj\ccb\mireff
//		ResConverter effect ..\..\..\ChaosArt\res\effect_editor_publish\miseff ..\..\Client\Output\data\obj\ccb\miseff
//		ResConverter effect ..\..\..\ChaosArt\res\effect_editor_publish\skieff ..\..\Client\Output\data\obj\ccb\skieff
//		ResConverter spine ..\..\..\ChaosArt\res\char_editor ..\..\Client\Output\data\obj\spine
//		ResConverter spine ..\..\..\ChaosArt\res\item_editor ..\..\Client\Output\data\obj\spine
//		ResConverter ui ..\..\..\ChaosArt\res\ui_editor ..\..\Client\Output\data\ccb
//		ResConverter ui ..\..\..\ChaosArt\res\ui_editor ..\..\Client\Output\data\ccb aaa.ccb
//		ResConverter map ..\..\..\ChaosArt\res\map_editor\texture\terrain_9900\tile ..\..\Client\Output\data\map\texture\terrain_9900\tile
//		ResConverter_bat

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

enum CONV_TYPE
{
	EFFECT = 0,
	SPINE,
	UI,
	MAP,
};

enum CONV_EFFECT_MODE
{
	NONE = 0,
	CCBI,
	TEXTURE,
};

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

static void convertEffect( const char* srcPath, const char* dstPath, FILE* fout, CONV_EFFECT_MODE mode )
{
	std::string rootPath = srcPath;
	rootPath += "\\";
	std::string fullPath = rootPath + "*";

	_finddata_t fileinfo;
	intptr_t hFile = _findfirst( fullPath.c_str(), &fileinfo );
	if( hFile == -1 )  
		return;

	do
	{
		std::string nowPath = rootPath + fileinfo.name;
		std::string nowDstPath = dstPath;
		nowDstPath += "\\";
		nowDstPath += fileinfo.name;
		if( fileinfo.attrib & _A_SUBDIR )
		{
			if( strcmp( fileinfo.name, "." ) == 0 || strcmp( fileinfo.name, ".." ) == 0 )
				continue;

			if( strcmp( fileinfo.name, "texture" ) == 0 || mode == TEXTURE )
			{
				if( strcmp( fileinfo.name, "texture" ) == 0 )
				{
					fprintf( fout, "rd /s /q %s\n", nowDstPath.c_str() );
					fprintf( fout, "md %s\n", nowDstPath.c_str() );
				}
				convertEffect( nowPath.c_str(), nowDstPath.c_str(), fout, TEXTURE );
				if( mode == TEXTURE )
				{
					fprintf( fout, "md %s\\work\n", dstPath );
					fprintf( fout, "xcopy /Y /Q /R /E %s %s\\work\\%s\\\n", nowPath.c_str(), dstPath, fileinfo.name );
					fprintf( fout, "TexturePacker --texture-format png --allow-free-size --size-constraints POT --force-squared --enable-rotation --opt RGBA8888 --data %s/%s.plist --format cocos2d --sheet %s/%s.png %s\\work\n", dstPath, fileinfo.name, dstPath, fileinfo.name, dstPath );
					fprintf( fout, "rd /s /q %s\\work\n", dstPath );
					int outputPos = nowDstPath.find( "\\Output" );
					if( outputPos != std::string::npos )
					{
						std::string right = nowDstPath.substr( outputPos + strlen( "\\Output" ) + 1 );
						std::string left = nowDstPath.substr( 0, outputPos + strlen( "\\Output" ) );
						int slashPos;
						while( ( slashPos = right.find( "\\" ) ) != std::string::npos )
						{
							right.replace( slashPos, 1, "/" );
						}
						while( ( slashPos = left.find( "\\" ) ) != std::string::npos )
						{
							left.replace( slashPos, 1, "/" );
						}
						//fprintf( fout, "FileListGen %s %s .png_.plist_.pvr.ccz ccbdata resources-\n", left.c_str(), right.c_str() );
					}
				}
			}
			else if( strcmp( fileinfo.name, "subccb" ) == 0 )
			{
				fprintf( fout, "md %s\n", nowDstPath.c_str() );
				convertEffect( nowPath.c_str(), nowDstPath.c_str(), fout, CCBI );
			}
		}
		else
		{
			if( mode == CCBI && strstr( fileinfo.name, ".ccbi" ) )
			{
				std::string copyPath = dstPath;
				copyPath += "\\";
				fprintf( fout, "xcopy /Y /Q /R /E %s %s\n", nowPath.c_str(), copyPath.c_str() );
			}
		}
	}while( _findnext( hFile, &fileinfo ) == 0 ); 
}

static void convertSpine( const char* srcPath, const char* dstPath, FILE* fout )
{
	std::string rootPath = srcPath;
	rootPath += "\\";
	std::string fullPath = rootPath + "*";

	_finddata_t fileinfo;
	intptr_t hFile = _findfirst( fullPath.c_str(), &fileinfo );
	if( hFile == -1 )  
		return;

	do
	{
		std::string nowPath = rootPath + fileinfo.name;
		std::string nowDstPath = dstPath;
		nowDstPath += "\\";
		nowDstPath += fileinfo.name;
		if( fileinfo.attrib & _A_SUBDIR )
		{
			if( strcmp( fileinfo.name, "." ) == 0 || strcmp( fileinfo.name, ".." ) == 0 )
				continue;

			fprintf( fout, "md %s\n", nowDstPath.c_str() );
			convertSpine( nowPath.c_str(), nowDstPath.c_str(), fout );
			int outputPos = nowDstPath.find( "\\Output" );
			if( outputPos != std::string::npos )
			{
				std::string right = nowDstPath.substr( outputPos + strlen( "\\Output" ) + 1 );
				std::string left = nowDstPath.substr( 0, outputPos + strlen( "\\Output" ) );
				int slashPos;
				while( ( slashPos = right.find( "\\" ) ) != std::string::npos )
				{
					right.replace( slashPos, 1, "/" );
				}
				while( ( slashPos = left.find( "\\" ) ) != std::string::npos )
				{
					left.replace( slashPos, 1, "/" );
				}
				fprintf( fout, "FileListGen %s %s .png_.plist_.pvr.ccz_.pkm chardata resources-\n", left.c_str(), right.c_str() );
			}
		}
		else
		{
			if( strstr( fileinfo.name, ".atlas" ) || strstr( fileinfo.name, ".json" ) )
			{
				std::string copyPath = dstPath;
				copyPath += "\\";
				fprintf( fout, "xcopy /Y /Q /R /E %s %s\n", nowPath.c_str(), copyPath.c_str() );
			}
			else if( strstr( fileinfo.name, ".png" ) )
			{
				nowDstPath = nowDstPath.erase( nowDstPath.rfind( ".png" ) );
				fprintf( fout, "TexturePacker --texture-format png --allow-free-size --disable-rotation --force-squared --opt RGBA8888 --border-padding 0 --trim-mode None --data %s.plist --format cocos2d --sheet %s.png %s\n", nowDstPath.c_str(), nowDstPath.c_str(), nowPath.c_str() );
				fprintf( fout, "del %s.plist /Q /F\n", nowDstPath.c_str() );
			}
		}
	}while( _findnext( hFile, &fileinfo ) == 0 ); 
}

static std::string sCCBFile;

static void copyRelativeTexture( const char* srcTexPath, const char* srcFolder, const char* dstPath, const char* dstFolder, FILE* fout )
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
			return;

		do
		{
			if( strstr( srcFolder, fileinfo.name ) == NULL )
			{
				std::string newSrcFolder = srcFolder;
				newSrcFolder = newSrcFolder.erase( newSrcFolder.rfind( "\\" ) );
				newSrcFolder += "\\";
				newSrcFolder += fileinfo.name;
				fprintf( fout, "xcopy /Y /Q /R /E %s\\%s %s\\texture\\work\\%s\\\n", srcTexPath, newSrcFolder.c_str(), dstPath, dstFolder );
			}
		}while( _findnext( hFile, &fileinfo ) == 0 ); 
	}
}

static void convertUITexture( const char* srcPath, const char* srcTexPath, const char* dstPath, FILE* fout )
{
	std::string rootPath = srcPath;
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
			convertUITexture( nowPath.c_str(), srcTexPath, dstPath, fout );
		}
		else if( strstr( fileinfo.name, ".ccb" ) && ( sCCBFile == "" || sCCBFile == fileinfo.name ) )
		{
			fprintf( fout, "md %s\\texture\\work\n", dstPath );

			FILE* fccb;
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
				fprintf( fout, "xcopy /Y /Q /R /E %s\\%s %s\\texture\\work\\%s\\\n", srcTexPath, srcFolder.c_str(), dstPath, dstFolder.c_str() );
				copyRelativeTexture( srcTexPath, srcFolder.c_str(), dstPath, dstFolder.c_str(), fout );
			}
			if( pngstr.length() )
			{
				pngstr = pngstr.erase( pngstr.length() - 1 );
				if( ccbname.find( "mirentereff" ) != std::string::npos )
					fprintf( fout, "TexturePacker --texture-format png --allow-free-size --size-constraints POT --force-squared --extrude 1 --disable-rotation --opt RGBA8888 --trim-mode None --data %s/texture/%s.plist --format cocos2d --sheet %s/texture/%s.png %s\\texture\\work\\texture\n", dstPath, ccbname.c_str(), dstPath, ccbname.c_str(), dstPath );
				else
					fprintf( fout, "TexturePacker --texture-format png --allow-free-size --size-constraints POT --force-squared --extrude 1 --enable-rotation --opt RGBA8888 --trim-mode None --data %s/texture/%s.plist --format cocos2d --sheet %s/texture/%s.png %s\\texture\\work\\texture\n", dstPath, ccbname.c_str(), dstPath, ccbname.c_str(), dstPath );
			}

			fprintf( fout, "rd /s /q %s\\texture\\work\n", dstPath );
		}

	}while( _findnext( hFile, &fileinfo ) == 0 ); 
}

static void convertMap( const char* srcPath, const char* dstPath, FILE* fout )
{
	std::string rootPath = srcPath;
	rootPath += "\\";
	std::string fullPath = rootPath + "*.png";

	_finddata_t fileinfo;
	intptr_t hFile = _findfirst( fullPath.c_str(), &fileinfo );
	if( hFile == -1 )  
		return;

	do
	{
		std::string nowPath = rootPath + fileinfo.name;
		std::string nowDstPath = dstPath;
		nowDstPath += "\\";
		nowDstPath += fileinfo.name;
		nowDstPath = nowDstPath.erase( nowDstPath.rfind( ".png" ) );
		fprintf( fout, "TexturePacker --texture-format png --allow-free-size --size-constraints POT --force-squared --extrude 1 --disable-rotation --opt RGBA8888 --border-padding 0 --data %s.plist --format cocos2d --sheet %s.png %s\n", nowDstPath.c_str(), nowDstPath.c_str(), nowPath.c_str() );
	}while( _findnext( hFile, &fileinfo ) == 0 ); 
}

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc != 4 && argc != 5 )
		return 0;

	CONV_TYPE type;
	if( strcmp( argv[1], "effect" ) == 0 )
		type = EFFECT;
	else if( strcmp( argv[1], "spine" ) == 0 )
		type = SPINE;
	else if( strcmp( argv[1], "ui" ) == 0 )
		type = UI;
	else
		type = MAP;
	std::string srcPath = argv[2];
	std::string dstPath = argv[3];

	sCCBFile = "";
	if( argc == 5 && type == UI )
	{
		sCCBFile = argv[4];
	}

	FILE* fout;
	if( fopen_s( &fout, ".\\ResConverter_bat.bat", "wt" ) )
		return 0;

	// recreate folder
	if( type == EFFECT )
	{
		fprintf( fout, "rd /s /q %s\n", dstPath.c_str() );
		fprintf( fout, "md %s\n", dstPath.c_str() );
	}
	else if( type == UI )
	{
		if( sCCBFile == "" )
		{
			fprintf( fout, "rd /s /q %s\\texture\n", dstPath.c_str() );
			fprintf( fout, "md %s\\texture\n", dstPath.c_str() );
		}
		else
		{
			// set file writable
			unsigned int idx = sCCBFile.find( ".ccb" );
			if( idx != std::string::npos )
			{
				std::string sCCBFront = sCCBFile.substr( 0, idx );
				fprintf( fout, "del /f /q %s\\texture\\%s.png\n", dstPath.c_str(), sCCBFront.c_str() );
				fprintf( fout, "del /f /q %s\\texture\\%s.plist\n", dstPath.c_str(), sCCBFront.c_str() );
			}
		}
	}

	// parser
	if( type == EFFECT )
	{
		convertEffect( srcPath.c_str(), dstPath.c_str(), fout, CCBI );
	}
	else if( type == SPINE )
	{
		convertSpine( srcPath.c_str(), dstPath.c_str(), fout );
	}
	else if( type == UI )
	{
		char buf[MAX_PATH+1];  
		GetCurrentDirectory( MAX_PATH, buf );
		std::string fullDstPath = buf;
		fullDstPath += "\\";
		fullDstPath += dstPath;
		convertUITexture( srcPath.c_str(), srcPath.c_str(), fullDstPath.c_str(), fout );
	}
	else
	{
		convertMap( srcPath.c_str(), dstPath.c_str(), fout );
	}

	fclose( fout );
	return 0;
}

