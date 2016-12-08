import shutil  
import os  
import os.path 
import sys
import stat
import subprocess 

from file_util import File_Util
from polarpath import PolarPath
ppath = PolarPath()

def get_version_xml(version):
	scheme_fold = os.path.normcase("E:\client\CandyCarrier\Client\PolarClient\Build\FileScheme")
	return scheme_fold + '\\'+ str(version) +'\\res_file_scheme.xml'
	
def copy_file(file,target_folder,taret_name):
	if not os.path.exists(target_folder):	
		os.makedirs(target_folder)
	targetFile = target_folder + r'\\' + taret_name
	targetFile = os.path.abspath(targetFile)
	shutil.copyfile(file,targetFile) 
scp_info = "root|10.1.164.53|36000|/data/htdocs/polar/package/client|seed@DEVy1"
#scp_info = os.getenv('scp_info', '')
print 'scp_info ' + scp_info
strs = scp_info.split("|")
if len(strs) < 5:
	raise Exception("scp_info error format")

version = '1.2.0.9'
compare_version = '1.2.0.8'
#version = os.getenv('version', 0)
#compare_version = os.getenv('compare_version', 0)
print "version {0} compare_version {1} ".format(version,compare_version)
#if compare_version == 0:
	#file = open("E:/client/Client/Build/version/last_sendtoserver_version", 'r')
	#compare_version = str(file.readline())

if 0 in (version, compare_version) :
	raise Exception("Need version and compare_version")
	
print "clean info fold"

def on_rm_error( func, path, exc_info):
    os.chmod( path, stat.S_IWRITE )
    # os.unlink( path )
	
def clean_fold(root_path,fold):
	full_path = root_path + fold
	full_path = os.path.abspath(full_path)
	if os.path.exists(full_path):
		shutil.rmtree( full_path, onerror = on_rm_error )
	return full_path

output_path = os.path.normcase("E:\client\CandyCarrier\Client\PolarClient\Output")
build_path = os.path.normcase("E:\client\CandyCarrier\Client\PolarClient\Build")

compare_dir = clean_fold(output_path,r'\compare_info')
diff_dir = clean_fold(output_path,r'\diff_pack')

diff_folder_name = "diff_" + str(version)

same_version = (str(version) == str(compare_version))
if not same_version:
	print "create diff package from version {0} to {1} ..".format(compare_version,version)

	current_version_xml = get_version_xml(version)
	compare_version_xml = get_version_xml(compare_version)

	if False in(os.path.exists(current_version_xml),os.path.exists(compare_version_xml)):
		raise Exception("version_xml not found")
		
	#dataEncryptor_folder = ppath.get_tool_path() + 'DataEncryptor/'
	#os.chdir(dataEncryptor_folder)
	#relate_script_path_to_exe = '../../{0}/Output/data/script/'.format(ppath.client_root)
	#param = 'DataEncryptor.exe -encrypt -name {0} {1}'.format(relate_script_path_to_exe,'.lua')
	#os.system(param)
	
	#relate_table_path_to_exe = '../../{0}/Output/data/table/'.format(ppath.client_root)
	#param_table = 'DataEncryptor.exe -encrypt -name {0} {1}'.format(relate_table_path_to_exe,'.lua')
	#os.system(param_table)
	
	#print "DataEncryptor done"

	copy_file(compare_version_xml,compare_dir,"res_file_scheme_old.xml")
	copy_file(current_version_xml,compare_dir,"res_file_scheme_new.xml")

	
	diff_folder = diff_dir + r'/' + diff_folder_name
	print "CreateDiffResDirX xml..."
	os.chdir(output_path)
	param = "CreateDiffResDirX|/compare_info/res_file_scheme_old.xml|/compare_info/res_file_scheme_new.xml|diff_pack/" + diff_folder_name
	subprocess.call(["PolarClient.exe", "BuildVersionInfo",param])

	if not os.path.exists(diff_folder + r'/data/PolarClient_Diff.xml'):  
		raise Exception("CreateDiffResDirX failed")

	#start zip diff_dir
	sz_path = r"C:\Program Files\7-Zip\7z.exe"
	#bbxhz_1.1.0.12_patch.zip
	zip_name = "bbxhz_" + version + "_patch.zip"
	zip_target = diff_dir + '/' + zip_name
	subprocess.call([sz_path, 'a', '-tzip','-r', zip_target, diff_folder + '/*'])
	
	#--BuildVersionInfo CreateDiffPackInfo|Polar_DiffPack|diff_pack|polar_diff.zip|Android|QQ|15|12|1
	#bbxhz_1.1.0.12_patch.xml
	platform = "Android"
	target = "QQ"
	xml_name_1 = "bbxhz_" + version + "_patch"
	param = "CreateDiffPackInfo|{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}".format(xml_name_1,"diff_pack",zip_name,platform,target,version,compare_version,1)
	subprocess.call(["PolarClient.exe", "BuildVersionInfo",param])

	#send file to server
	temp_fold = clean_fold(build_path,'/Temp')
	
	apk_file = r"E:\client\CandyCarrier\Client\PolarClient\PolarClient\proj.android\bin\PolarClient-release.apk"
	#bbxhz_1.1.0.12_patch.xml
	apk_name = "bbxhz_" + version + "_pkg.apk"
	copy_file(apk_file,temp_fold + '/package',apk_name)
	copy_file(zip_target,temp_fold + '/patch',zip_name)
	copy_file(diff_dir + '/' + xml_name_1 + ".xml",temp_fold + '/patch',xml_name_1 + ".xml")
	#subprocess.call([sz_path, 'a', '-tzip','-r', temp_fold + '/' + 'client.zip', temp_fold +'/*.*'])
	
	#'../PolarClient/Output/diff_folder_name/','./temp/pc.zip',
	send_files = []
	send_files.append('./temp/package')
	send_files.append('./temp/patch')
	#send_files.append('./temp/client.zip')
	#send_files.append('../PolarClient/Output/diff_pack/'+ xml_name_1 + ".xml")
	#send_files.append('../PolarClient/Output/diff_pack/'+ zip_name)
	#send_files.append('./temp/' + apk_name)
	os.chdir('E:\client\CandyCarrier\Client\PolarClient\Build')
	for file in send_files: 
		if not os.path.exists(file):
			raise Exception(file + "not exist")
		cmd = r'C:\cygwin64\bin\bash.exe --login "E:\client\CandyCarrier\Client\PolarClient\Build\BUILD.sh" {0} {1} {2} {3} {4} {5}'.format(strs[0],strs[1],strs[2],strs[3],strs[4],file)
		os.system(cmd)
		
	#write version to file
	#os.system("attrib E:/client/Client/Build/version/last_sendtoserver_version -r")
	#file_object = open('E:/client/Client/Build/version/last_sendtoserver_version', 'w')
	#file_object.write(str(version))
	#file_object.close( )

	print "copy files to server DONE"
else:
	raise Exception("Same version don't need compare")





