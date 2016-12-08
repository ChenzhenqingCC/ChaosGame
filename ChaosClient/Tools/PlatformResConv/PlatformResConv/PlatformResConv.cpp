// PlatformResConv.cpp : 定义控制台应用程序的入口点。
// command:
//		PlatformResConv type path
// examples:
//		PlatformResConv ios effect ..\..\Client\Output\data\obj\ccb\comeff
//		PlatformResConv ios effect ..\..\Client\Output\data\obj\ccb\mireff
//		PlatformResConv ios effect ..\..\Client\Output\data\obj\ccb\miseff
//		PlatformResConv ios effect ..\..\Client\Output\data\obj\ccb\skieff
//		PlatformResConv ios spine ..\..\Client\Output\data\obj\spine
//		PlatformResConv ios ui ..\..\Client\Output\data\ccb\texture
//		PlatformResConv ios map ..\..\Client\Output\data\map\texture\terrain_0100\tile
//		PlatformResConv ios map ..\..\Client\Output\data\map\texture\terrain_0200\tile
//		PlatformResConv ios map ..\..\Client\Output\data\map\texture\terrain_0300\tile
//		PlatformResConv ios map ..\..\Client\Output\data\map\texture\terrain_0500\tile
//		PlatformResConv ios map ..\..\Client\Output\data\map\texture\terrain_0800\tile
//		PlatformResConv ios map ..\..\Client\Output\data\map\texture\terrain_1100\tile
//		PlatformResConv ios map ..\..\Client\Output\data\map\texture\terrain_6000\tile
//		PlatformResConv ios map ..\..\Client\Output\data\map\texture\terrain_8000\tile
//		PlatformResConv ios map ..\..\Client\Output\data\map\texture\terrain_9800\tile
//		PlatformResConv ios map ..\..\Client\Output\data\map\texture\terrain_9900\tile
//		PlatformResConv ios maptype ..\..\Client\Output\data\map\texture\arena
//		PlatformResConv ios maptype ..\..\Client\Output\data\map\texture\dark
//		PlatformResConv ios maptype ..\..\Client\Output\data\map\texture\desert
//		PlatformResConv ios maptype ..\..\Client\Output\data\map\texture\grass
//		PlatformResConv ios maptype ..\..\Client\Output\data\map\texture\lava
//		PlatformResConv ios maptype ..\..\Client\Output\data\map\texture\main
//		PlatformResConv ios maptype ..\..\Client\Output\data\map\texture\snow
//		PlatformResConv ios maptype ..\..\Client\Output\data\map\texture\stageselect
//		PlatformResConv ios maptype ..\..\Client\Output\data\map\texture\stsm
//		PlatformResConv ios maptype ..\..\Client\Output\data\map\texture\swamp
//		PlatformResConv ios bg ..\..\Client\Output\data\map\background\bg_01
//		PlatformResConv ios bg ..\..\Client\Output\data\map\background\bg_03
//		PlatformResConv ios bg ..\..\Client\Output\data\map\background\bg_04
//		PlatformResConv ios bg ..\..\Client\Output\data\map\background\bg_8000_01
//		PlatformResConv ios bg ..\..\Client\Output\data\map\background\bg_square
//		PlatformResConv_bat

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
#include "../../VerDiffer/VerDiffer/md5.h"

static std::string workPath;

enum PLAT_TYPE
{
	IOS,
	ANDROID,
};

enum CONV_TYPE
{
	EFFECT = 0,
	SPINE,
	UI,
	MAP,
	MAPTYPE,
	BG,
};

enum PACK_TYPE
{
	RGB_ONLY,
	RGB_ALPHA_SEPARATE,
	RGB_ALPHA_MERGE,
};

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

static bool isMD5Equal( const char* src, const char* dst )
{
	FILE* fp;
	if( fopen_s( &fp, src, "rb" ) )
		return false;

	fpos_t startPos, endPos;
	fseek( fp, 0, SEEK_SET );
	fgetpos( fp, &startPos );
	fseek( fp, 0, SEEK_END );
	fgetpos( fp, &endPos );
	unsigned int size = endPos - startPos;
	fseek( fp, 0, SEEK_SET );
	char* data = new char[size];
	fread( data, 1, size, fp );
	fclose( fp );

	std::string md5StringSrc;
	unsigned char digset[16];
	MD5_CTX md5Ctx;
	MD5Init( &md5Ctx );
	MD5Update( &md5Ctx, ( unsigned char* )data, size );
	MD5Final( &md5Ctx, digset );
	md5ToString( digset, md5StringSrc );
	delete[] data;

	if( fopen_s( &fp, dst, "rb" ) )
		return false;

	fseek( fp, 0, SEEK_SET );
	fgetpos( fp, &startPos );
	fseek( fp, 0, SEEK_END );
	fgetpos( fp, &endPos );
	size = endPos - startPos;
	fseek( fp, 0, SEEK_SET );
	data = new char[size];
	fread( data, 1, size, fp );
	fclose( fp );

	std::string md5StringDst;
	MD5Init( &md5Ctx );
	MD5Update( &md5Ctx, ( unsigned char* )data, size );
	MD5Final( &md5Ctx, digset );
	md5ToString( digset, md5StringDst );
	delete[] data;

	if( md5StringDst.compare( md5StringSrc.c_str() ) == 0 )
		return true;

	return false;
}

static bool convertPngAndPlist( PLAT_TYPE plat, const char* path, const char* listGenType, PACK_TYPE packType, const char* compare, FILE* fout )
{
	bool ret = false;
	std::string rootPath = path;
	rootPath += "\\";
	std::string fullPath = rootPath + "*";

	_finddata_t fileinfo;
	intptr_t hFile = _findfirst( fullPath.c_str(), &fileinfo );
	if( hFile == -1 )  
		return ret;

	do
	{
		std::string nowPath = rootPath + fileinfo.name;
		std::string nowDstPath = path;
		nowDstPath += "\\";
		nowDstPath += fileinfo.name;
		std::string comparePath = compare;
		if( comparePath.compare( "" ) != 0 )
		{
			comparePath += "\\";
			comparePath += fileinfo.name;	
		}
		if( fileinfo.attrib & _A_SUBDIR )
		{
			if( strcmp( fileinfo.name, "." ) == 0 || strcmp( fileinfo.name, ".." ) == 0 )
				continue;

			if( convertPngAndPlist( plat, nowPath.c_str(), listGenType, packType, comparePath.c_str(), fout ) && listGenType )
			{
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
					fprintf( fout, "FileListGen %s %s .png_.plist_.pvr_.pvr.ccz_.pkm_.pkm.ogz %s resources-\n", left.c_str(), right.c_str(), listGenType );
				}
			}
		}
		else
		{
			if( strstr( fileinfo.name, ".plist" ) )
			{
				FILE* fp;
				if( fopen_s( &fp, nowPath.c_str(), "rb" ) )
					continue;

				char* data = new char[fileinfo.size];
				fread( data, 1, fileinfo.size, fp );
				fclose( fp );

				DWORD  dwAttribute=::GetFileAttributes( nowPath.c_str() );
				if( dwAttribute & FILE_ATTRIBUTE_READONLY )
				{   
					dwAttribute &= ~FILE_ATTRIBUTE_READONLY;  
					SetFileAttributes( nowPath.c_str(),dwAttribute );
				}   

				if( fopen_s( &fp, nowPath.c_str(), "wb" ) )
					continue;

				char* pContent = new char[fileinfo.size + 1];
				memcpy( pContent, data, fileinfo.size );
				pContent[fileinfo.size] = '\0';
				delete[] data;

				char* nowContent = pContent;
				char fileContent[256];
				bool nextChange = false;
				do
				{
					memset( fileContent, 0, 256 );
					sscanf( nowContent, "%[^\n]", fileContent );
					nowContent += strlen( fileContent ) + 1;
					if( strstr( fileContent, "<key>realTextureFileName</key>" ) || strstr( fileContent, "<key>textureFileName</key>" ) )
					{
						nextChange = true;
					}
					else if( nextChange )
					{
						std::string tmp = fileContent;
						if( plat == IOS )
							tmp.replace( tmp.find( ".png" ), strlen( ".png" ), ".pvr.ccz" );
						else
							tmp.replace( tmp.find( ".png" ), strlen( ".png" ), ".pkm" );
						memset( fileContent, 0, 256 );
						strcpy_s( fileContent, tmp.data() );
						nextChange = false;
					}
					fprintf( fp, "%s\n", fileContent );
				}while( nowContent[0] != '\0' );
				delete[] pContent;
				fclose( fp );
			}
			else if( strstr( fileinfo.name, ".png" ) )
			{
				ret = true;
				bool isChanged = true;
				bool isExist = false;
				if( comparePath.compare( "" ) != 0 )
				{
					isChanged = !isMD5Equal( nowDstPath.c_str(), comparePath.c_str() );

					std::string checkPath = comparePath;
					checkPath = checkPath.erase( checkPath.rfind( ".png" ) );
					if( plat == IOS )
					{
						checkPath.replace( checkPath.find( "data\\pc\\Output" ), strlen( "data\\pc\\Output" ), "data\\ios\\Output" );
						checkPath += ".pvr.ccz";
					}
					else
					{
						checkPath.replace( checkPath.find( "data\\pc\\Output" ), strlen( "data\\pc\\Output" ), "data\\android\\Output" );
						checkPath += ".pkm";
					}
					if( _access( checkPath.c_str(), 0 ) != -1 )
					{
						isExist = true;
					}
				}
				
				if( isChanged || !isExist )
				{
					nowDstPath = nowDstPath.erase( nowDstPath.rfind( ".png" ) );
					if( plat == IOS )
					{
						if( packType == RGB_ALPHA_SEPARATE )
						{
							fprintf( fout, "TexturePacker --texture-format png --max-size 4096 --disable-rotation --opt ALPHA --border-padding 0 --shape-padding 0 --trim-mode None --data %s-a8.plist --format cocos2d --sheet %s-a8.png %s\n", nowDstPath.c_str(), nowDstPath.c_str(), nowPath.c_str() );
							fprintf( fout, "del %s-a8.plist /Q /F\n", nowDstPath.c_str() );
							fprintf( fout, "TexturePacker --texture-format pvr3ccz --pvr-quality best --premultiply-alpha --max-size 4096 --disable-rotation --opt PVRTC4_NOALPHA --border-padding 0 --shape-padding 0 --trim-mode None --data %s-a8.plist --format cocos2d --sheet %s-a8.pvr.ccz %s-a8.png\n", nowDstPath.c_str(), nowDstPath.c_str(), nowDstPath.c_str() );
							fprintf( fout, "del %s-a8.plist /Q /F\n", nowDstPath.c_str() );
							fprintf( fout, "del %s-a8.png /Q /F\n", nowDstPath.c_str() );
							fprintf( fout, "TexturePacker --texture-format pvr3ccz --pvr-quality best --premultiply-alpha --max-size 4096 --disable-rotation --opt PVRTC4_NOALPHA --border-padding 0 --shape-padding 0 --trim-mode None --data %s_temp.plist --format cocos2d --sheet %s.pvr.ccz %s\n", nowDstPath.c_str(), nowDstPath.c_str(), nowPath.c_str() );
							fprintf( fout, "del %s_temp.plist /Q /F\n", nowDstPath.c_str() );
							fprintf( fout, "del %s /Q /F\n", nowPath.c_str() );
						}
						else if( packType == RGB_ALPHA_MERGE )
						{
							fprintf( fout, "TexturePacker --texture-format pvr3ccz --pvr-quality best --premultiply-alpha --max-size 4096 --disable-rotation --opt PVRTC4 --border-padding 0 --shape-padding 0 --trim-mode None --data %s_temp.plist --format cocos2d --sheet %s.pvr.ccz %s\n", nowDstPath.c_str(), nowDstPath.c_str(), nowPath.c_str() );
							fprintf( fout, "del %s_temp.plist /Q /F\n", nowDstPath.c_str() );
							fprintf( fout, "del %s /Q /F\n", nowPath.c_str() );
						}
						else if( packType == RGB_ONLY )
						{
							fprintf( fout, "TexturePacker --texture-format pvr3ccz --pvr-quality best --premultiply-alpha --max-size 4096 --disable-rotation --opt PVRTC4_NOALPHA --border-padding 0 --shape-padding 0 --trim-mode None --data %s_temp.plist --format cocos2d --sheet %s.pvr.ccz %s\n", nowDstPath.c_str(), nowDstPath.c_str(), nowPath.c_str() );
							fprintf( fout, "del %s_temp.plist /Q /F\n", nowDstPath.c_str() );
							fprintf( fout, "del %s /Q /F\n", nowPath.c_str() );
						}
					}
					else
					{
						if( packType == RGB_ALPHA_SEPARATE )
						{
							fprintf( fout, "TexturePacker --texture-format png --max-size 4096 --disable-rotation --opt ALPHA --border-padding 0 --shape-padding 0 --trim-mode None --data %s-a8.plist --format cocos2d --sheet %s-a8.png %s\n", nowDstPath.c_str(), nowDstPath.c_str(), nowPath.c_str() );
							fprintf( fout, "del %s-a8.plist /Q /F\n", nowDstPath.c_str() );
							fprintf( fout, "TexturePacker --texture-format pkm --premultiply-alpha --max-size 4096 --disable-rotation --opt ETC1 --border-padding 0 --shape-padding 0 --trim-mode None --data %s-a8.plist --format cocos2d --sheet %s-a8.pkm %s-a8.png\n", nowDstPath.c_str(), nowDstPath.c_str(), nowDstPath.c_str() );
							fprintf( fout, "del %s-a8.plist /Q /F\n", nowDstPath.c_str() );
							fprintf( fout, "del %s-a8.png /Q /F\n", nowDstPath.c_str() );
							fprintf( fout, "TexturePacker --texture-format pkm --premultiply-alpha --max-size 4096 --disable-rotation --opt ETC1 --border-padding 0 --shape-padding 0 --trim-mode None --data %s_temp.plist --format cocos2d --sheet %s.pkm %s\n", nowDstPath.c_str(), nowDstPath.c_str(), nowPath.c_str() );
							fprintf( fout, "del %s_temp.plist /Q /F\n", nowDstPath.c_str() );
							fprintf( fout, "del %s /Q /F\n", nowPath.c_str() );
							//fprintf( fout, "PKMPacker %s.pkm\n", nowDstPath.c_str() );
							//fprintf( fout, "del %s.pkm /Q /F\n", nowDstPath.c_str() );
							//fprintf( fout, "PKMPacker %s-a8.pkm\n", nowDstPath.c_str() );
							//fprintf( fout, "del %s-a8.pkm /Q /F\n", nowDstPath.c_str() );
						}
						else if( packType == RGB_ALPHA_MERGE )
						{
							fprintf( fout, "TexturePacker --texture-format pkm --premultiply-alpha --max-size 4096 --disable-rotation --opt ETC1 --border-padding 0 --shape-padding 0 --trim-mode None --data %s_temp.plist --format cocos2d --sheet %s.pkm %s\n", nowDstPath.c_str(), nowDstPath.c_str(), nowPath.c_str() );
							fprintf( fout, "del %s_temp.plist /Q /F\n", nowDstPath.c_str() );
							fprintf( fout, "del %s /Q /F\n", nowPath.c_str() );
							//fprintf( fout, "PKMPacker %s.pkm\n", nowDstPath.c_str() );
							//fprintf( fout, "del %s.pkm /Q /F\n", nowDstPath.c_str() );
						}
						else if( packType == RGB_ONLY )
						{
							fprintf( fout, "TexturePacker --texture-format pkm --premultiply-alpha --max-size 4096 --disable-rotation --opt ETC1 --border-padding 0 --shape-padding 0 --trim-mode None --data %s_temp.plist --format cocos2d --sheet %s.pkm %s\n", nowDstPath.c_str(), nowDstPath.c_str(), nowPath.c_str() );
							fprintf( fout, "del %s_temp.plist /Q /F\n", nowDstPath.c_str() );
							fprintf( fout, "del %s /Q /F\n", nowPath.c_str() );
							//fprintf( fout, "PKMPacker %s.pkm\n", nowDstPath.c_str() );
							//fprintf( fout, "del %s.pkm /Q /F\n", nowDstPath.c_str() );
						}
					}
				}
				else
				{
					nowDstPath = nowDstPath.erase( nowDstPath.rfind( "\\" ) + 1 );
					comparePath = comparePath.erase( comparePath.rfind( ".png" ) );
					if( plat == IOS )
					{
						comparePath.replace( comparePath.find( "data\\pc\\Output" ), strlen( "data\\pc\\Output" ), "data\\ios\\Output" );
						if( packType == RGB_ALPHA_SEPARATE )
						{
							fprintf( fout, "xcopy %s.pvr.ccz %s /I /Q /Y\n", comparePath.c_str(), nowDstPath.c_str() );
							fprintf( fout, "xcopy %s-a8.pvr.ccz %s /I /Q /Y\n", comparePath.c_str(), nowDstPath.c_str() );
							fprintf( fout, "del %s /Q /F\n", nowPath.c_str() );
						}
						else
						{
							fprintf( fout, "xcopy %s.pvr.ccz %s /I /Q /Y\n", comparePath.c_str(), nowDstPath.c_str() );
							fprintf( fout, "del %s /Q /F\n", nowPath.c_str() );
						}
					}
					else
					{
						comparePath.replace( comparePath.find( "data\\pc\\Output" ), strlen( "data\\pc\\Output" ), "data\\android\\Output" );
						if( packType == RGB_ALPHA_SEPARATE )
						{
							fprintf( fout, "xcopy %s.pkm %s /I /Q /Y\n", comparePath.c_str(), nowDstPath.c_str() );
							fprintf( fout, "xcopy %s-a8.pkm %s /I /Q /Y\n", comparePath.c_str(), nowDstPath.c_str() );
							fprintf( fout, "del %s /Q /F\n", nowPath.c_str() );
						}
						else
						{
							fprintf( fout, "xcopy %s.pkm %s /I /Q /Y\n", comparePath.c_str(), nowDstPath.c_str() );
							fprintf( fout, "del %s /Q /F\n", nowPath.c_str() );
						}
					}
				}
			}
		}
	}while( _findnext( hFile, &fileinfo ) == 0 );
	return ret;
}

static void convertEffect( PLAT_TYPE plat, const char* path, const char* compare, FILE* fout )
{
	PACK_TYPE packType = RGB_ALPHA_MERGE;
	if( plat == ANDROID )
	{
		packType = RGB_ALPHA_SEPARATE;
	}
	convertPngAndPlist( plat, path, NULL, packType, compare, fout );
}

static void convertSpine( PLAT_TYPE plat, const char* path, const char* compare, FILE* fout )
{
	convertPngAndPlist( plat, path, "chardata", RGB_ALPHA_SEPARATE, compare, fout );
}

static void convertUI( PLAT_TYPE plat, const char* path, const char* compare, FILE* fout )
{
	convertPngAndPlist( plat, path, NULL, RGB_ALPHA_SEPARATE, compare, fout );
}

static void convertMap( PLAT_TYPE plat, const char* path, const char* compare, FILE* fout )
{
	PACK_TYPE packType = RGB_ALPHA_MERGE;
	if( plat == ANDROID )
	{
		packType = RGB_ALPHA_SEPARATE;
	}
	convertPngAndPlist( plat, path, NULL, packType, compare, fout );
}

static void convertMapType( PLAT_TYPE plat, const char* path, const char* compare, FILE* fout )
{
	PACK_TYPE packType = RGB_ALPHA_MERGE;
	if( plat == ANDROID )
	{
		packType = RGB_ALPHA_SEPARATE;
	}
	bool ret = convertPngAndPlist( plat, path, "tex", packType, compare, fout );
	if( ret )
	{
		std::string nowDstPath = path;
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
			fprintf( fout, "FileListGen %s %s .png_.plist_.pvr_.pvr.ccz_.pkm_.pkm.ogz tex resources-\n", left.c_str(), right.c_str() );
		}
	}
}

static void convertBg( PLAT_TYPE plat, const char* path, const char* compare, FILE* fout )
{
	bool ret = convertPngAndPlist( plat, path, "tex", RGB_ONLY, compare, fout );
	if( ret )
	{
		std::string nowDstPath = path;
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
			fprintf( fout, "FileListGen %s %s .png_.plist_.pvr_.pvr.ccz_.pkm_.pkm.ogz tex resources-\n", left.c_str(), right.c_str() );
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc != 5 && argc != 6 )
		return 0;

	PLAT_TYPE plat;
	if( strcmp( argv[1], "ios" ) == 0 )
		plat = IOS;
	else
		plat = ANDROID;

	CONV_TYPE type;
	if( strcmp( argv[2], "effect" ) == 0 )
		type = EFFECT;
	else if( strcmp( argv[2], "spine" ) == 0 )
		type = SPINE;
	else if( strcmp( argv[2], "ui" ) == 0 )
		type = UI;
	else if( strcmp( argv[2], "map" ) == 0 )
		type = MAP;
	else if( strcmp( argv[2], "maptype" ) == 0 )
		type = MAPTYPE;
	else
		type = BG;
	std::string path = argv[3];
	path += argv[4];
	std::string compare = "";
	if( argc == 6 && argv[5] != NULL && argv[5][0] != '\0' )
	{
		compare = argv[5];
		compare += argv[4];
	}

	char buf[MAX_PATH+1];  
	GetCurrentDirectory( MAX_PATH, buf );
	workPath = buf;

	FILE* fout;
	if( fopen_s( &fout, ".\\PlatformResConv_bat.bat", "wt" ) )
		return 0;

	fprintf( fout, "cd %s\n", workPath.c_str() );

	if( type == EFFECT )
	{
		convertEffect( plat, path.c_str(), compare.c_str(), fout );
	}
	else if( type == SPINE )
	{
		convertSpine( plat, path.c_str(), compare.c_str(), fout );
	}
	else if( type == UI )
	{
		convertUI( plat, path.c_str(), compare.c_str(), fout );
	}
	else if( type == MAP )
	{
		convertMap( plat, path.c_str(), compare.c_str(), fout );
	}
	else if( type == MAPTYPE )
	{
		convertMapType( plat, path.c_str(), compare.c_str(), fout );
	}
	else
	{
		convertBg( plat, path.c_str(), compare.c_str(), fout );
	}

	fclose( fout );
	return 0;

	return 0;
}

