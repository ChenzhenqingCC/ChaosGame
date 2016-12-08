// PKMPacker.cpp : 定义控制台应用程序的入口点。
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

/// usage: PKMPacker pkm_path  ( generate pkm.gz in the same folder with pkm )

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc != 2 )
	{
		printf( "PKMPacker parameter is wrong, usage:PKMPacker pkm_path!\n" );
		return 1;
	}

	std::string filePath = argv[1];

	FILE* fp = NULL;
	if( fopen_s( &fp, filePath.c_str(), "rb" ) )
	{
		printf( "PKMPacker error: can't find pkm file:%s\n", filePath.c_str() );
		return 0;
	}
	fseek( fp, 0, SEEK_END );
	unsigned int size = ftell( fp );
	unsigned char* data = new unsigned char[size];
	fseek( fp, 0, SEEK_SET );
	fread( data, size, 1, fp );
	fclose( fp );

	CGZEncrypt gzDecryptor;
	unsigned int outLength = gzDecryptor.GetOutputLength( data, size, true );
	unsigned char* pFileOutData = new unsigned char[outLength];
	gzDecryptor.Encrypt( FILE_DATA_ENCRYPT_KEY, data, pFileOutData, size, &outLength );

	delete[] data;

	filePath += ".ogz";
	if( fopen_s( &fp, filePath.c_str(), "wb" ) )
	{
		delete[] pFileOutData;
		printf( "PKMPacker error: can't write output pkm.gz file:%s\n", filePath.c_str() );
		return 0;
	}

	fwrite( pFileOutData, outLength, 1, fp );
	fclose( fp );
	delete[] pFileOutData;

	return 0;
}

