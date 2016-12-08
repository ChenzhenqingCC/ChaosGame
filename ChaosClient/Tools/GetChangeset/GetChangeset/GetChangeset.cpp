// GetChangeset.cpp : 定义控制台应用程序的入口点。
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

/// usage: GetChangeset changeset_num

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc != 2 )
	{
		printf( "GetChangeset parameter is wrong, usage:GetChangeset changeset_num!\n" );
		return 1;
	}

	std::string changeset = argv[1];

	int start = changeset.find( "Change " ) + strlen( "Change " );
	int end = changeset.find( " ", start );
	std::string changesetStr = changeset.substr( start, end - start );

	printf( "%s\n", changesetStr.c_str() );

	return 0;
}

