// AndroidPack.cpp : 定义控制台应用程序的入口点。
// command:
//		AndroidPack channel ver_str region_str changeset_str language_str workspace dev_path sdk_path
// examples:
//		AndroidPack internal.develop_android-normal.onekey_android-normal.baidu 0.8.15656.15656 1 15656 simple_chinese "D:\Program Files (x86)\Jenkins\jobs\chaos_pc-android\workspace" "ChaosClient\Client\Client\proj.android" "ChaosClient\Client\Client\proj.android_all"
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
	int i;
	printf("AndroidPack get params:");
	for(i=0;i<argc;i++){
		printf("%d ------ %s \n",i,argv[i]);
	}

	if( argc < 9 )
		return 0;

	std::string strChannel = argv[1];
	std::string strVersion = argv[2];
	std::string strRegion = argv[3];
	std::string strChangeset = argv[4];
	std::string strLanguage = argv[5];
	std::string strRoot = argv[6];
	std::string strDevPath = argv[7];
	std::string strSdkPath = argv[8];
	std::string strExpansionFileSize = "";
	std::string strNeedExpansion = "";
	if( argc > 9 )
	{
		strExpansionFileSize = argv[9];
	}
	if( argc > 10 )
	{
		strNeedExpansion = argv[10];
	}



	unsigned int dotPos = strVersion.find( "." );
	std::string tmp1 = strVersion.substr( 0, dotPos );
	std::string tmp2 = strVersion.substr( dotPos + 1 );
	dotPos = tmp2.find( "." );
	std::string tmp3 = tmp2.substr( 0, dotPos );
	std::string strVersionName = tmp1 + "." + tmp3;

	strDevPath = strRoot + "\\" + strDevPath;
	strSdkPath = strRoot + "\\" + strSdkPath;

	FILE* fout;
	if( fopen_s( &fout, ".\\AndroidPack_bat.bat", "wt" ) )
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
			std::string buildPath;
			std::string dataPath;
			if( 0 )//strChannelId.find( "develop" ) != std::string::npos )
			{
				buildPath = strDevPath;
				dataPath = "..\\..\\..\\Output\\data";
			}
			else
			{
				buildPath = strSdkPath;
				buildPath += "\\polarClient\\src\\main";
				dataPath = "..\\..\\..\\..\\..\\..\\Output\\data";
			}
			if( strServerId.find( "ios" ) == std::string::npos )
			{
				fprintf( fout, "attrib -r \"%s\\ChaosClient\\Client\\Output\\data\\config\"\n", strRoot.c_str() );
				fprintf( fout, "xcopy \"%s\\ChaosClient\\Tools\\Configs\\ios_encrypt\\config\" \"%s\\ChaosClient\\Client\\Output\\data\" /E /I /Q /Y\n", strRoot.c_str(), strRoot.c_str() );
				fprintf( fout, "cd /d \"%s\\ChaosClient\\Client\\Output\\data\"\n", strRoot.c_str() );
				fprintf( fout, "echo servergroup=%s>>config\n", strServerId.c_str() );
				fprintf( fout, "echo channel=%s>>config\n", strChannelId.c_str() );
				fprintf( fout, "echo language=%s>>config\n", strLanguage.c_str() );
				fprintf( fout, "cd /d \"%s\"\n", buildPath.c_str() );
				fprintf( fout, "attrib -r \"%s\\AndroidManifest.xml\"\n", buildPath.c_str() );
				fprintf( fout, "python \"%s\\ChaosClient\\Tools\\DataProcess\\version_android.py\" AndroidManifest.xml %s %s\n", strRoot.c_str(), strChangeset.c_str(), strVersionName.c_str() );
				fprintf( fout, "mklink /D .\\assets\\data %s\n", dataPath.c_str() );
				fprintf( fout, "set ANDROID_HOME=D:\\adt-bundle\\sdk\n" );
				fprintf( fout, "set JAVA_HOME=D:\\Program Files\\Java\\jdk1.8.0_25\n" );
				if( 0 )//strChannelId.find( "develop" ) != std::string::npos )
				{
					fprintf( fout, "call ant clean release\n" );
				}
				else
				{
					fprintf( fout, "cd /d \"%s\"\n", strSdkPath.c_str() );
					std::string assemblePath = "assemble";
					char channelIdC[64];
					strcpy_s( channelIdC, strChannelId.c_str() );
					channelIdC[0] -= 32;
					assemblePath += channelIdC;
					assemblePath += "Release";
					fprintf( fout, "call Gradle %s -PExpansionVersionCode=%s -PExpansionFileSize=%s -PNeedUseExpansion=%s \n", assemblePath.c_str(),strChangeset.c_str(),strExpansionFileSize.c_str(),strNeedExpansion.c_str());
					
				}
				
				std::string verPath = "E:\\share\\publish\\versions\\";
				verPath += strRegion;
				verPath += "\\";
				fprintf( fout, "md %s\n", verPath.c_str() );
				verPath += strVersion;
				verPath += "\\";
				fprintf( fout, "md %s\n", verPath.c_str() );
				verPath += "android";
				verPath += "\\";
				fprintf( fout, "md %s\n", verPath.c_str() );
				verPath += strServerId;
				verPath += "\\";
				fprintf( fout, "md %s\n", verPath.c_str() );
				verPath += strChannelId;
				verPath += "\\";
				fprintf( fout, "rd %s /s /q\n", verPath.c_str() );
				fprintf( fout, "md %s\n", verPath.c_str() );

				std::string new_apk_name = "maplegame_";
				new_apk_name += strVersion;
				new_apk_name += "_";
				new_apk_name += strServerId;
				new_apk_name += "_";
				new_apk_name += strChannelId;
				new_apk_name += ".apk";
				std::string src_apk_path;
				std::string src_apk_name;
				if( 0 )//strChannelId.find( "develop" ) != std::string::npos )
				{
					src_apk_path = buildPath + "\\bin\\PolarClient-release.apk";
					src_apk_name = "PolarClient-release.apk";
				}
				else
				{
					src_apk_name = strChannelId;
					src_apk_name += "Release.apk";
					src_apk_path = strSdkPath + "\\bin\\" + src_apk_name;
				}
				fprintf( fout, "xcopy \"%s\" \"%s\" /I /Q /Y\n", src_apk_path.c_str(), verPath.c_str() );
				if(strExpansionFileSize != "")
				{
					std::string zip_expansion_file_path = strRoot + "\\ChaosClient\\Tools\\MakeSmallPack\\temp_for_expansion\\main.1.packagename.obb";
					fprintf( fout, "xcopy \"%s\" \"%s\" /I /Q /Y\n", zip_expansion_file_path.c_str(), verPath.c_str() );
				}
				fprintf( fout, "cd /d \"%s\"\n", verPath.c_str() );
				fprintf( fout, "ren \"%s\" %s\n", src_apk_name.c_str(), new_apk_name.c_str() );
				
			}
		}
	}

	fclose( fout );

	return 0;
}

