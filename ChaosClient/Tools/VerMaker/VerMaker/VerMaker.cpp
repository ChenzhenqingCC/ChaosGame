// VerMaker.cpp : 定义控制台应用程序的入口点。
//
#include "stdafx.h"
#include <stdio.h>
#include <windows.h>
#include <stdlib.h>
#include <string>
#include <windows.h>
#include <vector>
#include <map>
#include <io.h>
#include <direct.h>
#include "../../../Client/Client/Classes/Utility/DataEncrypt.h"

/// usage: VerMaker mainversion region serverupdate changeset filepath

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc != 6 )
	{
		printf( "VerMaker parameter is wrong, usage:VerMaker mainversion region serverupdate changeset filepath!\n" );
		return 1;
	}

	std::string mainVersion = argv[1];
	std::string region = argv[2];
	std::string serverUpdate = argv[3];
	std::string changeset = argv[4];
	std::string filePath = argv[5];

	/// get now changeset
	//  changeset format "Change changeset XXXX"
	//  version info format "xxx.xxx.xxx.xxx_xxx"
	int start = changeset.find( "Change " ) + strlen( "Change " );
	int end = changeset.find( " ", start );
	std::string changesetStr = changeset.substr( start, end - start );
	std::string serverStr = changesetStr;

	FILE* fp = NULL;
	if( serverUpdate.compare( "false" ) == 0 )
	{
		if( fopen_s( &fp, filePath.c_str(), "rb" ) )
		{
			printf( "VerMaker can't find original version file:%s\n", filePath.c_str() );
			return 1;
		}

		fseek( fp, 0, SEEK_END );
		unsigned int size = ftell( fp );
		unsigned char* data = new unsigned char[size];
		fseek( fp, 0, SEEK_SET );
		fread( data, size, 1, fp );

		unsigned char* outputData = NULL;
		unsigned int outputLength = CResourceDecryptUtil::DecryptorData( FILE_DATA_ENCRYPT_KEY, data, &outputData, size );

		char* totalString = new char[outputLength + 1];
		memcpy( totalString, outputData, outputLength );
		totalString[outputLength] = '\0';

		std::string versionInfo = totalString;
		int first = versionInfo.find( "." );
		int second = versionInfo.find( ".", first + 1 );
		int third = versionInfo.find( ".", second + 1 );
		serverStr = versionInfo.substr( second + 1, third - second - 1 );

		delete[] totalString;
		delete[] outputData;
		delete[] data;
		fclose( fp );
	}

	fp = NULL;
	if( fopen_s( &fp, filePath.c_str(), "wb" ) )
	{
		printf( "VerMaker can't create file:%s\n", filePath.c_str() );
		return 1;
	}
	
	std::string version_str = mainVersion + "." + serverStr + "." + changesetStr + "_" + region;
	printf( "%s\n", version_str.c_str() );

	CXorEncrypt xorDecrptor;
	CGZEncrypt gzDecryptor;

	unsigned int outLength = gzDecryptor.GetOutputLength( ( unsigned char* )version_str.data(), version_str.length(), true );
	unsigned char* pFileOutData = new unsigned char[outLength];
	gzDecryptor.Encrypt( FILE_DATA_ENCRYPT_KEY, ( unsigned char* )version_str.data(), pFileOutData, version_str.length(), &outLength );

	unsigned int xorOutLength = xorDecrptor.GetOutputLength( pFileOutData, outLength, true );
	unsigned char* pXorFileOutData = new unsigned char[xorOutLength];
	xorDecrptor.Encrypt( FILE_DATA_ENCRYPT_KEY, pFileOutData, pXorFileOutData, outLength, &xorOutLength );
	delete[] pFileOutData;
	
	fwrite( pXorFileOutData, xorOutLength, 1, fp );

	delete[] pXorFileOutData;
	fclose( fp );
	
	return 0;
}

