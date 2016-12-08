// PatchInfoGen.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "stxutif.h"

#include <stdio.h>
#include <windows.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <map>
#include <io.h>
#include <direct.h>
#include <iostream> 
#include <iosfwd>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <codecvt>

#include "../../../Client/external/rapidxml/rapidxml.hpp"
#include "../../../Client/external/rapidxml/rapidxml_print.hpp"
#include "../../../Client/external/rapidxml/rapidxml_utils.hpp"
#include "../../VerDiffer/VerDiffer/md5.h"

using namespace rapidxml;

void wstringSplit( std::wstring& s, std::wstring& delim, std::vector<std::wstring>* ret )
{
	size_t last = 0;
	size_t index = s.find_first_of( delim, last );
	while( index != std::wstring::npos )
	{
		ret->push_back( s.substr( last, index - last ) );
		last = index + 1;
		index = s.find_first_of( delim, last );
	}
	if( index - last > 0 )
	{
		ret->push_back( s.substr( last, index - last ) );
	}
}

static const char* unicodeToUtf8( std::wstring strUnicode )
{
	if( strUnicode.length() > 0 )
	{	
		int nUtf8Length = WideCharToMultiByte( CP_UTF8, 0, strUnicode.c_str(), -1, NULL, 0, NULL, FALSE );
		char* pszUtf8Buf = new char[nUtf8Length + 1];
		memset( pszUtf8Buf, 0, ( nUtf8Length + 1 ) * sizeof( char ) );

		WideCharToMultiByte( CP_UTF8, 0, strUnicode.c_str(), -1, pszUtf8Buf, ( nUtf8Length + 1 ) * sizeof( char ), NULL, FALSE );
		return pszUtf8Buf;
	}
	return NULL;
}

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

static bool compare_version( const std::string& str1, const std::string& str2 )
{
	std::string from1 = str1;
	std::string from2 = str2;

	int fromVer1[4], fromVer2[4];

	fromVer1[0] = atoi( from1.substr( 0, from1.find( "." ) ).c_str() );
	from1 = from1.substr( from1.find( "." ) + 1 );
	fromVer1[1] = atoi( from1.substr( 0, from1.find( "." ) ).c_str() );
	from1 = from1.substr( from1.find( "." ) + 1 );
	fromVer1[2] = atoi( from1.substr( 0, from1.find( "." ) ).c_str() );
	fromVer1[3] = atoi( from1.substr( from1.find( "." ) + 1 ).c_str() );

	fromVer2[0] = atoi( from2.substr( 0, from2.find( "." ) ).c_str() );
	from2 = from2.substr( from2.find( "." ) + 1 );
	fromVer2[1] = atoi( from2.substr( 0, from2.find( "." ) ).c_str() );
	from2 = from2.substr( from2.find( "." ) + 1 );
	fromVer2[2] = atoi( from2.substr( 0, from2.find( "." ) ).c_str() );
	fromVer2[3] = atoi( from2.substr( from2.find( "." ) + 1 ).c_str() );

	if( fromVer1[0] != fromVer2[0] )
		return fromVer1[0] < fromVer2[0] ? true : false;

	if( fromVer1[1] != fromVer2[1] )
		return fromVer1[1] < fromVer2[1] ? true : false;

	if( fromVer1[2] != fromVer2[2] )
		return fromVer1[2] < fromVer2[2] ? true : false;

	if( fromVer1[3] != fromVer2[3] )
		return fromVer1[3] < fromVer2[3] ? true : false;

	return true;
}

static bool sort_by_version( const std::string& str1, const std::string& str2 )
{
	std::string from1 = str1.substr( 0, str1.find( "_to_" ) );
	std::string from2 = str2.substr( 0, str2.find( "_to_" ) );

	return compare_version( from1, from2 );
}

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc != 2 )
	{
		printf( "parameter wrong!\n" );
		system( "PAUSE" );
		return 1;
	}

	std::wstring outfile = argv[1];

	intptr_t hFile;
    _finddata_t fileinfo;
	std::string findPath;

	WCHAR szFilePath[MAX_PATH + 1] = { 0 };
	GetModuleFileName( NULL, szFilePath, MAX_PATH );
	( _tcsrchr( szFilePath, _T( '\\' ) ) )[1] = 0;
	char scFilePath[MAX_PATH + 1];
	wcstombs( scFilePath, szFilePath, MAX_PATH );
	findPath = scFilePath;
	findPath += "*.zip";

	std::vector<unsigned int> vernums;
	std::vector<std::string> versions;
	std::vector<std::string>::iterator iter;

	hFile = _findfirst( findPath.c_str(), &fileinfo );  
	if( hFile != -1 )
	{
		do
		{
			if( !strstr( fileinfo.name, "_to_" ) )
			{
				printf( "invalid patch file name!\n" );
				system( "PAUSE" );
				return 1;
			}
			versions.push_back( fileinfo.name );
		}while( _findnext( hFile, &fileinfo ) == 0 );
	}

	/// order patches
	std::sort( versions.begin(), versions.end(), sort_by_version );

	/// verify patches
	std::string oldFrom = "";
	std::string oldTo = "";
	iter = versions.begin();
	while( iter != versions.end() )
	{
		std::string curFrom = iter->substr( 0, iter->find( "_to_" ) );
		std::string curTo = iter->substr( iter->find( "_to_" ) + strlen( "_to_" ) );
		curTo = curTo.substr( 0, curTo.find( ".zip" ) );
		if( !compare_version( curFrom, curTo ) )
		{
			printf( "invalid patch order!\n" );
			system( "PAUSE" );
			return 1;
		}

		if( oldFrom.compare( "" ) != 0 && oldTo.compare( "" ) != 0 )
		{
			if( oldTo.compare( curFrom.c_str() ) != 0 )
			{
				printf( "invalid patch order!\n" );
				system( "PAUSE" );
				return 1;
			}
		}

		oldFrom = curFrom;
		oldTo = curTo;
		iter++;
	}

	/// read announcement.txt
	std::vector<std::wstring> titles;
	std::vector<std::wstring> contents;
	std::wifstream inf( "announcement.txt", std::ios::binary );
	if( inf.is_open() )
	{
		inf.imbue( std::locale( inf.getloc(), new std::codecvt_utf16<wchar_t, 0x10ffff, std::consume_header> ) );

		int state = 0;
		std::wstring wline;
		std::wstring longContent;
		while( std::getline( inf, wline ) )
		{
			if( wline == L"\r" )
			{
				if( state == 1 )
				{
					if( !longContent.empty() )
					{
						longContent = longContent.erase( longContent.length() - 1 );
					}
					contents.push_back( longContent.c_str() );
				}
				state = 0;
				continue;
			}
			
			wline = wline.erase( wline.length() - 1 );
			if( state == 0 )
			{
				titles.push_back( wline );
				state = 1;
				longContent = _T( "" );
			}
			else if( state == 1 )
			{
				longContent += wline;
				longContent += _T( "\n" );
			}
		}
		inf.close();
	}

	/// read servers.txt
	std::vector<std::wstring> serverDatas;
	inf.open( "servers.txt", std::ios::binary );
	if( inf.is_open() )
	{
		inf.imbue( std::locale( inf.getloc(), new std::codecvt_utf16<wchar_t, 0x10ffff, std::consume_header> ) );

		std::wstring wline;
		while( std::getline( inf, wline ) )
		{
			wline = wline.erase( wline.length() - 1 );
			serverDatas.push_back( wline );
		}

		inf.close();
	}

	/// read testservers.txt
	std::vector<std::wstring> testServerDatas;
	inf.open( "testservers.txt", std::ios::binary );
	if( inf.is_open() )
	{
		inf.imbue( std::locale( inf.getloc(), new std::codecvt_utf16<wchar_t, 0x10ffff, std::consume_header> ) );

		std::wstring wline;
		while( std::getline( inf, wline ) )
		{
			wline = wline.erase( wline.length() - 1 );
			testServerDatas.push_back( wline );
		}

		inf.close();
	}

	/// read minversion.txt
	std::wstring minVersionStr = _T("");
	inf.open( "minversion.txt", std::ios::binary );
	if( inf.is_open() )
	{
		inf.imbue( std::locale( inf.getloc(), new std::codecvt_utf16<wchar_t, 0x10ffff, std::consume_header> ) );

		std::wstring wline;
		if( std::getline( inf, wline ) )
		{
			wline = wline.erase( wline.length() - 1 );
			minVersionStr = wline;
		}

		inf.close();
	}

	/// write xml
	xml_document<> doc;
	xml_node<>* root = doc.allocate_node( rapidxml::node_pi, doc.allocate_string( "xml version='1.0' encoding='utf-8'" ) );
	doc.append_node( root ); 

	xml_node<>* node =   doc.allocate_node( node_element, "config", NULL );  
    doc.append_node( node ); 

	xml_node<>* servers = doc.allocate_node( node_element, "servers", NULL );
	node->append_node( servers );

	unsigned int count = 0;
	for( count = 0; count < serverDatas.size(); count++ )
	{
		std::wstring serverData = serverDatas[count];
		std::vector<std::wstring> serverStrs;
		wstringSplit( serverData, std::wstring( _T( " " ) ), &serverStrs );

		// name
		char* nameStr = new char[32];
		sprintf( nameStr, "name_%d", count );
		vernums.push_back( ( unsigned int )nameStr );
		const char* utf8Str = unicodeToUtf8( serverStrs[0] );
		servers->append_node( doc.allocate_node( node_element, nameStr, utf8Str ) );
		vernums.push_back( ( unsigned int )utf8Str );

		// url
		char* urlStr = new char[32];
		sprintf( urlStr, "url_%d", count );
		vernums.push_back( ( unsigned int )urlStr );
		utf8Str = unicodeToUtf8( serverStrs[1] );
		servers->append_node( doc.allocate_node( node_element, urlStr, utf8Str ) );
		vernums.push_back( ( unsigned int )utf8Str );

		// dispName
		char* dispNameStr = new char[32];
		sprintf( dispNameStr, "dispName_%d", count );
		vernums.push_back( ( unsigned int )dispNameStr );
		utf8Str = unicodeToUtf8( serverStrs[2] );
		servers->append_node( doc.allocate_node( node_element, dispNameStr, utf8Str ) );
		vernums.push_back( ( unsigned int )utf8Str );

		// official
		char* officialStr = new char[32];
		sprintf( officialStr, "official_%d", count );
		vernums.push_back( ( unsigned int )officialStr );
		utf8Str = unicodeToUtf8( serverStrs[3] );
		servers->append_node( doc.allocate_node( node_element, officialStr, utf8Str ) );
		vernums.push_back( ( unsigned int )utf8Str );

		// status
		char* statusStr = new char[32];
		sprintf( statusStr, "status_%d", count );
		vernums.push_back( ( unsigned int )statusStr );
		utf8Str = unicodeToUtf8( serverStrs[4] );
		servers->append_node( doc.allocate_node( node_element, statusStr, utf8Str ) );
		vernums.push_back( ( unsigned int )utf8Str );

		// status
		char* sidStr = new char[32];
		sprintf( sidStr, "serverid_%d", count );
		vernums.push_back( ( unsigned int )sidStr );
		utf8Str = unicodeToUtf8( serverStrs[5] );
		servers->append_node( doc.allocate_node( node_element, sidStr, utf8Str ) );
		vernums.push_back( ( unsigned int )utf8Str );
	}

	xml_node<>* minversion = doc.allocate_node( node_element, "minversion", NULL );
	node->append_node( minversion );

	if( minVersionStr.length() > 0 )
	{
		// min version
		char* versionStr = new char[32];
		sprintf( versionStr, "version" );
		vernums.push_back( ( unsigned int )versionStr );
		const char* utf8Str = unicodeToUtf8( minVersionStr );
		minversion->append_node( doc.allocate_node( node_element, versionStr, utf8Str ) );
		vernums.push_back( ( unsigned int )utf8Str );
	}

	xml_node<>* testservers = doc.allocate_node( node_element, "testservers", NULL );
	node->append_node( testservers );

	for( count = 0; count < testServerDatas.size(); count++ )
	{
		std::wstring serverData = testServerDatas[count];
		std::vector<std::wstring> testServerStrs;
		wstringSplit( serverData, std::wstring( _T( " " ) ), &testServerStrs );

		// name
		char* nameStr = new char[32];
		sprintf( nameStr, "name_%d", count );
		vernums.push_back( ( unsigned int )nameStr );
		const char* utf8Str = unicodeToUtf8( testServerStrs[0] );
		testservers->append_node( doc.allocate_node( node_element, nameStr, utf8Str ) );
		vernums.push_back( ( unsigned int )utf8Str );

		// url
		char* urlStr = new char[32];
		sprintf( urlStr, "url_%d", count );
		vernums.push_back( ( unsigned int )urlStr );
		utf8Str = unicodeToUtf8( testServerStrs[1] );
		testservers->append_node( doc.allocate_node( node_element, urlStr, utf8Str ) );
		vernums.push_back( ( unsigned int )utf8Str );

		// dispName
		char* dispNameStr = new char[32];
		sprintf( dispNameStr, "dispName_%d", count );
		vernums.push_back( ( unsigned int )dispNameStr );
		utf8Str = unicodeToUtf8( testServerStrs[2] );
		testservers->append_node( doc.allocate_node( node_element, dispNameStr, utf8Str ) );
		vernums.push_back( ( unsigned int )utf8Str );

		// official
		char* officialStr = new char[32];
		sprintf( officialStr, "official_%d", count );
		vernums.push_back( ( unsigned int )officialStr );
		utf8Str = unicodeToUtf8( testServerStrs[3] );
		testservers->append_node( doc.allocate_node( node_element, officialStr, utf8Str ) );
		vernums.push_back( ( unsigned int )utf8Str );

		// status
		char* statusStr = new char[32];
		sprintf( statusStr, "status_%d", count );
		vernums.push_back( ( unsigned int )statusStr );
		utf8Str = unicodeToUtf8( testServerStrs[4] );
		testservers->append_node( doc.allocate_node( node_element, statusStr, utf8Str ) );
		vernums.push_back( ( unsigned int )utf8Str );
	}

	xml_node<>* announcement = doc.allocate_node( node_element, "announcement", NULL );
	node->append_node( announcement );

	for( count = 0; count < titles.size(); count++ )
	{
		std::wstring title = titles[count];
		std::wstring content = contents[count];

		// title
		char* titleStr = new char[32];
		sprintf( titleStr, "title_%d", count );
		const char* utf8Str = unicodeToUtf8( title );
		announcement->append_node( doc.allocate_node( node_element, titleStr, utf8Str ) );
		vernums.push_back( ( unsigned int )titleStr );
		vernums.push_back( ( unsigned int )utf8Str );

		// content
		char* contentStr = new char[32];
		sprintf( contentStr, "content_%d", count );
		utf8Str = unicodeToUtf8( content );
		announcement->append_node( doc.allocate_node( node_element, contentStr, utf8Str ) );
		vernums.push_back( ( unsigned int )contentStr );
		vernums.push_back( ( unsigned int )utf8Str );
	}

	xml_node<>* patchinfo = doc.allocate_node( node_element, "patches", NULL );
	node->append_node( patchinfo );

	count = 0;
	for( iter = versions.begin(); iter != versions.end(); ++iter )
	{
		char* countStr = new char[32];
		sprintf( countStr, "patch_%d", count );
		
		patchinfo->append_node( doc.allocate_node( node_element, countStr, iter->c_str() ) );
		vernums.push_back( ( unsigned int )countStr );

		// md5
		char* md5Str = new char[32];
		char* md5Code = new char[64];
		sprintf_s( md5Str, 32, "md5_%d", count );
		{
			FILE* fp = NULL;
			if( !fopen_s( &fp, iter->c_str(), "rb" ) )
			{
				fseek( fp, 0, SEEK_END );
				unsigned int zipSize = ftell( fp );
				fseek( fp, 0, SEEK_SET );
				unsigned char* zipData = new unsigned char[zipSize];
				fread( zipData, zipSize, 1, fp );
				fclose( fp );

				std::string md5String;
				unsigned char digset[16];
				MD5_CTX md5Ctx;
				MD5Init( &md5Ctx );
				MD5Update( &md5Ctx, zipData, zipSize );
				MD5Final( &md5Ctx, digset );
				md5ToString( digset, md5String );
				strcpy_s( md5Code, 64, md5String.data() );

				patchinfo->append_node( doc.allocate_node( node_element, md5Str, md5Code ) );
				vernums.push_back( ( unsigned int )md5Code );
			}
			else
			{
				printf( "can't generate md5 code!\n" );
				system( "PAUSE" );
				return 1;
			}
		}
		vernums.push_back( ( unsigned int )md5Str );

		// count increase
		count++;
	}

	std::ofstream out( outfile.c_str(), std::ios::out | std::ios::binary );
	unsigned char smarker[3];
	smarker[0] = 0xEF;
	smarker[1] = 0xBB;
	smarker[2] = 0xBF;
	out << smarker;
	out.close();

	std::ofstream fs;
	fs.open( outfile.c_str() );
	std::locale utf8_locale( std::locale(), new gel::stdx::utf8cvt<false> );
	fs.imbue( utf8_locale ); 
    fs << doc; 
	fs.close();

	for( count = 0; count < vernums.size(); count++ )
	{
		delete[] ( char* )vernums[count];
	}

	return 0;
}

