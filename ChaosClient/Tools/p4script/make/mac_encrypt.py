from polarpath import PolarPath

import os


ppath = PolarPath()

do_encrypt = os.getenv('do_encrypt', 'true')
#run DataEncryptor
if do_encrypt == 'true':
	dataEncryptor_folder = ppath.get_tool_path() + 'DataEncryptor/'
	os.chdir(dataEncryptor_folder)
	relate_script_path_to_exe = '../../{0}/Output/data/script/'.format(ppath.client_root)
	param = './DataEncryptor_Mac -encrypt -name {0} {1}'.format(relate_script_path_to_exe,'.lua')
	os.system(param)
	
	relate_table_path_to_exe = '../../{0}/Output/data/table/'.format(ppath.client_root)
	param_table = 'DataEncryptor.exe -encrypt -name {0} {1}'.format(relate_table_path_to_exe,'.lua')
	os.system(param_table)
	print "DataEncryptor done"