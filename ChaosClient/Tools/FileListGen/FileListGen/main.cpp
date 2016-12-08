/*
	@ Desc :	Generate file list for reading
	@ Author :	huangxing	
*/

#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <windows.h>
#include <vector>
#include <map>
#include <io.h>
#include "../../../Client/Client/Classes/Utility/PackageDef.h"

/// USAGE: 
///		FileListGen.exe exe_path root_path suffix_name(.png_.plist_.pvz.cc ...) pkg_type(tex) ignore_path(like"resources-")
///		Generated file list will be the name like ("root_path".pkg."pkg_type"),
///		it's a txt file instead.
///		When using the package, may be need this two parameters "root_path" and "pkg_type"

static void printUsage()
{
	printf( "FileListGen.exe exe_path root_path suffix_name(.png_.plist_.pvz.cc ...) pkg_type(tex) ignore_path(like resources-)\n" );
}

static bool checkPkgType( const char* pkgType )
{
	unsigned int i;
	for( i = 0; i < PACKAGE_TYPE_MAX; i++ )
	{
		if( strstr( PackageTypeName[i], pkgType ) )
			return true;
	}
	return false;
}

static void processPath_win32( const char* path, std::vector<std::string>& suffixs, FILE* fp, const char* relativePath, const char* ignorePath, std::map<std::string, bool>&recordedPaths )
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
		std::string relPath = relativePath;
		relPath += "/";
		relPath += fileinfo.name;

		if( !( fileinfo.attrib & _A_SUBDIR ) )
		{
			if( suffixs.size() == 0 )
			{
				if( recordedPaths.find( relPath ) == recordedPaths.end() )
				{
					fprintf( fp, "%s\n", relPath.c_str() );
					recordedPaths.insert( std::make_pair( relPath, true ) );
				}
			}
			else
			{
				std::vector<std::string>::iterator iter;
				for( iter = suffixs.begin(); iter != suffixs.end(); ++iter )
				{
					if( strstr( fileinfo.name, ( *iter ).c_str() ) )
					{
						std::string writePath = relPath;
						int findIgnore = std::string::npos;
						if( ( findIgnore = writePath.find( ignorePath ) ) != std::string::npos )	/// need not use while
						{
							int right = writePath.find( "/", findIgnore );
							int left = writePath.rfind( "/", findIgnore );
							if( right != std::string::npos && left != std::string::npos )
							{
								writePath = writePath.erase( left, right - left );
							}
						}
						if( recordedPaths.find( writePath ) == recordedPaths.end() )
						{
							fprintf( fp, "%s\n", writePath.c_str() );
							recordedPaths.insert( std::make_pair( writePath, true ) );
						}
					}
				}
			}
		}
		else
		{
			if( strcmp( fileinfo.name, "." ) == 0 || strcmp( fileinfo.name, ".." ) == 0 )
				continue;
			processPath_win32( nowPath.c_str(), suffixs, fp, relPath.c_str(), ignorePath, recordedPaths );
		}
	}while( _findnext( hFile, &fileinfo ) == 0 ); 
}

static std::vector<std::string> split(std::string str,std::string pattern)
{
    std::string::size_type pos;
    std::vector<std::string> result;
    str+=pattern;//扩展字符串以方便操作
    int size=str.size();

    for(int i=0; i<size; i++)
    {
        pos=str.find(pattern,i);
        if(pos<size)
        {
            std::string s=str.substr(i,pos-i);
            result.push_back(s);
            i=pos+pattern.size()-1;
        }
    }
    return result;
}

int main( int argc, char* argv[] )
{
	if( argc != 6 || !checkPkgType( argv[4] ) )
	{
		printUsage();
		return 0;
	}

	std::string exePath = argv[1];
	std::string rootPath = argv[2];
	std::string suffixName = argv[3];
	std::string ignorePath = argv[5];
	std::vector<std::string> suffixs;
	if( suffixName.compare( "*.*" ) != 0 )
	{
		suffixs = split( suffixName, "_" );
	}

	char folderPath[MAX_PATH];
	const char* exePathStr = exePath.c_str();
	if( exePathStr[1] == ':' )
	{
		strcpy( folderPath, exePathStr );
	}
	else
	{
		::GetCurrentDirectory( MAX_PATH, folderPath );
		strcat( folderPath, "\\" );
		strcat( folderPath, exePath.c_str() );
	}
	strcat( folderPath, "\\" );
	strcat( folderPath, rootPath.c_str() );

	std::string pkgPath = folderPath;
	pkgPath += "\\";
	pkgPath += ( strrchr( folderPath, '/' ) + 1 );
	pkgPath += ".pkg.";
	pkgPath += argv[4];

	DWORD  dwAttribute=::GetFileAttributes( pkgPath.c_str() );
	if( dwAttribute & FILE_ATTRIBUTE_READONLY )
	{   
		dwAttribute &= ~FILE_ATTRIBUTE_READONLY;  
		SetFileAttributes( pkgPath.c_str(),dwAttribute );
	}   

	FILE* fp;
	fopen_s( &fp, pkgPath.c_str(), "wt+" );
	if( !fp )
	{
		printUsage();
		return 0;
	}

	std::map<std::string, bool> recordedPaths;
	processPath_win32( folderPath, suffixs, fp, rootPath.c_str(), ignorePath.c_str(), recordedPaths );
	fclose( fp );

	int fileSize = 0;
	fopen_s( &fp, pkgPath.c_str(), "rb" );
	if( fp )
	{
		fseek( fp, 0, SEEK_SET );
		fpos_t start, end;
		fgetpos( fp, &start );
		fseek( fp, 0, SEEK_END );
		fgetpos( fp, &end );
		fileSize = end - start;

		fclose( fp );
	}
	if( fileSize == 0 )
	{
		DeleteFile( pkgPath.c_str() );
	}

	return 0;
}