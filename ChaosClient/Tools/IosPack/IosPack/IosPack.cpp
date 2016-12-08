// IosPack.cpp : 定义控制台应用程序的入口点。
// command:
//		IosPack channel version_str language_string http_workspace
// examples:
//		IosPack internal.develop_android-normal.onekey_android-normal.baidu_ios-appstore.v5 0.8.15656.15656_1 ch "http://192.168.1.98:8080/job/m"

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

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc != 5 )
		return 0;

	std::string strChannel = argv[1];
	std::string strVersion = argv[2];
	std::string strLanguage = argv[3];
	std::string strHttp = argv[4];

	FILE* fout;
	if( fopen_s( &fout, ".\\IosPack_bat.bat", "wt" ) )
		return 0;

	std::string strLeftChannel;
	std::string strRightChannel = strChannel;
	while( strRightChannel != "" )
	{
		unsigned int idx = strRightChannel.find( "_" );
		if( idx != std::string::npos )
		{
			strLeftChannel = strRightChannel.substr( 0, idx );
			strRightChannel = strRightChannel.substr( idx + 1 );
		}
		else
		{
			strLeftChannel = strRightChannel;
			strRightChannel = "";
		}

		unsigned int dotIdx = strLeftChannel.find( "." );
		if( dotIdx != std::string::npos )
		{
			std::string strServerId = strLeftChannel.substr( 0, dotIdx );
			std::string strChannelId = strLeftChannel.substr( dotIdx + 1 );

			if( strServerId.find( "android" ) == std::string::npos )
			{
				if( strChannelId == "v5" || strChannelId == "develop" )
				{
					fprintf( fout, "start %s/buildWithParameters?VERSION_STRING=%s^&CHANNEL_STRING=%s^&LANGUAGE_STRING=%s^&SERVER_STRING=%s\n", strHttp.c_str(), strVersion.c_str(), strChannelId.c_str(), strLanguage.c_str(), strServerId.c_str() );
				}
				else
				{
					std::string jbHttp = strHttp;
					unsigned int slashIdx = jbHttp.rfind( "/" );
					if( slashIdx != std::string::npos )
					{
						std::string jbLeft = jbHttp.substr( 0, slashIdx + 1 );
						std::string jbRight = jbHttp.substr( slashIdx + 1 );
						jbHttp = jbLeft;
						jbHttp += "j";
						jbHttp += jbRight;
					}
					fprintf( fout, "start %s/buildWithParameters?VERSION_STRING=%s^&CHANNEL_STRING=%s^&LANGUAGE_STRING=%s^&SERVER_STRING=%s\n", jbHttp.c_str(), strVersion.c_str(), strChannelId.c_str(), strLanguage.c_str(), strServerId.c_str() );
				}
			}
		}
	}

	fclose( fout );

	return 0;
}

