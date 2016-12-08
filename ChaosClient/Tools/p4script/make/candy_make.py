from polarpath import PolarPath
import subprocess
import os
from p4setting import get_setting
from p4controller import P4Controller
from file_util import File_Util
from combine_lua import combineProjLuaFiles
import stat
from subprocess import Popen, PIPE, STDOUT
from datetime import *  
import time 
import types
import urllib2
import json
import shutil 

ppath = PolarPath()
p4c = P4Controller()
str_online = os.getenv('online', "false")
str_debug_info = os.getenv('debug_info', "false")

hasDebugInfo = (str_debug_info == "true")
isOnline = (str_online == 'true')

def httpRequestProtoVersion(end_version):
	try:
		url ="http://10.1.164.88/chuzzle.php?project=chuzzle&action=cmd&cmd=getreleaseversion&cli=" + str(end_version)
		data = urllib2.urlopen(url).read()
		front_index = data.find('{"retCod')
		word = data[front_index:len(data)]
		return json.loads(word)
	except Exception,e:
		print e

ppath = PolarPath()
p4c = P4Controller()

#the third digit of version differs online version and trunk version
versionThirdDigit = '1'
if isOnline:
	versionThirdDigit = '0'

client_version_int =  File_Util.read_client_version()
if client_version_int is None:
	raise Exception("can't find file end_version ")

proto_version = File_Util.read_proto_version()

if proto_version is None:
	raise Exception("can't find the proto file")

print "getting proto end_version from http://10.1.164.88 "
response = httpRequestProtoVersion(versionThirdDigit + '.' + str(client_version_int))

server_version_str = response['server']
full_version_str = response['version']
full_version_int = response['number']

print "response server_version_str :" + str(server_version_str) + " full_version_str " + str(full_version_str) + " full_version_int " + str(full_version_int)

if None in {server_version_str,full_version_str,full_version_int}:
	raise Exception("can't get proto_version from server")

server_proto_updated = (str(server_version_str) != str(proto_version))
print "server_proto " + str(server_version_str) + " proto_version " + str(proto_version)
proto_version = server_version_str
print str('server_proto_updated ' + str(server_proto_updated))
if not server_proto_updated:
	client_version_int = int(client_version_int) + 1
	print 'server_proto not updated , end_version ++ '
else:
	print 'server_proto_updated change end_version to 0'
	client_version_int = 0

response = httpRequestProtoVersion(versionThirdDigit + '.' + str(client_version_int))
full_version_int = response['number']
full_version_str = response['version']

if not full_version_int:
	raise Exception("can't get full_version_int from server")
	
File_Util.write_proto_version(proto_version)
File_Util.write_client_version(client_version_int)

information_path = ppath.get_information_path()
os.chmod( information_path, stat.S_IWRITE )
fp = open(information_path,"r")
alllines = fp.readlines()  
fp.close() 

fp = open(information_path,'w')  
#end_version = datetime.now().strftime('%Y.%m.%d.%H%M%S');
print 'Write Version ' + str(full_version_int) + ' to Information '

for eachline in alllines: 
	res_index = eachline.find('res_ver = ')
	proto_index = eachline.find('proto_ver = ')
	if res_index != -1:
		fp.writelines('	res_ver = \"' + str(full_version_int)+'\",\n')
	elif(proto_index != -1):
		fp.writelines('	proto_ver = \"' + str(proto_version) +'\",\n')
	else:
		fp.writelines(eachline)  
fp.close()  

p4c.reconcile_file_ea(ppath.information_path)
p4c.reconcile_fold_ea(ppath.version_log_folder)


copy_data = (
	("/CandyCarrier/Art/demo/export/","/CandyCarrier/Client/"+ ppath.client_root +"/Output/data/asset/"),
	("/CandyCarrier/Art/demo/appearance/","/CandyCarrier/Client/"+ ppath.client_root +"/Output/data/table/appearance/"),
	("/CandyCarrier/Design/levels/","/CandyCarrier/Client/"+ ppath.client_root +"/Output/data/table/levels/","full"),
	("/CandyCarrier/Design/config/","/CandyCarrier/Client/"+ ppath.client_root +"/Output/data/table/configuration/"),
	("/CandyCarrier/Design/setting/fixed_levels/","/CandyCarrier/Client/"+ ppath.client_root +"/Output/data/table/setting/fixed_levels/","full"),
	("/CandyCarrier/Design/setting/newbie/","/CandyCarrier/Client/"+ ppath.client_root +"/Output/data/table/setting/newbie/","full"),
)

root = ppath.setting['root']

for row in copy_data:
	num = len(row)
	needDelete = False
	if num >= 3 and row[2] == "full":
		print ("clear fold " + row[1])
		File_Util.remove_fold(root + row[1])
		needDelete = True
	print ("copying files from " + row[0] + " to " + row[1])
	origin_full = ppath.setting['root'] + row[0]
	File_Util.copy_fold(root + row[0],root + row[1])
	if needDelete:
		p4c.reconcile_fold_ead(row[1])
	else:
		p4c.reconcile_fold_ea(row[1])
		
p4c.submit('[Jenkins submit config ]')

#combine lua scripts
#combine lua scripts should come after "config" action, because some configuration lua scripts will be changed in "config" action
print("----Start to combine lua scripts----");
bRelease = True
if hasDebugInfo:
	bRelease = False
	print "debug lua combine"
else:
	print "release lua combine"
lua_script_path_to_combine = ppath.setting['root'] + '/CandyCarrier/Client/' + ppath.client_root + '/Output/data/script'
combineProjLuaFiles(lua_script_path_to_combine, bRelease)
print("----combining lua scripts finished----");
#combine finished
#do not reconcile!

#copy combined script file to different folder and send to p4
print "----copy combined scripts to CombinedScripts folder----"
srcLuaFolderDir = "/CandyCarrier/Client/"+ ppath.client_root +"/Output/data/script/"
destLuaFolderDir = "/CandyCarrier/Client/"+ ppath.client_root +"/CombinedLuaScripts/"

print "remove folder of " + destLuaFolderDir
File_Util.remove_fold(root + destLuaFolderDir)

print ("copying files from " + srcLuaFolderDir + " to " + destLuaFolderDir)
File_Util.copy_fold(root + srcLuaFolderDir , root + destLuaFolderDir)
p4c.reconcile_fold_ead(destLuaFolderDir)

p4c.submit("[Jenkins submit combined scripts]")
print "----copy combined scripts finished----"
#copy combined script file to different folder and send to p4 end

#run DataEncryptor
str_encrypt = os.getenv('do_encrypt', 'false')
is_encrypt = (str_encrypt == 'true')
print "--- do_encrypt " + str_encrypt
if is_encrypt:
	dataEncryptor_folder = ppath.get_tool_path() + 'DataEncryptor/'
	os.chdir(dataEncryptor_folder)
	relate_script_path_to_exe = '../../../../CandyCarrier/Client/{0}/Output/data/script/'.format(ppath.client_root)
	relate_table_path_to_exe = '../../../../CandyCarrier/Client/{0}/Output/data/table/'.format(ppath.client_root)
	param_script = 'DataEncryptor.exe -encrypt -name {0} {1}'.format(relate_script_path_to_exe,'.lua')
	os.system(param_script)
	param_table = 'DataEncryptor.exe -encrypt -name {0} {1}'.format(relate_table_path_to_exe,'.lua')
	os.system(param_table)
	print "DataEncryptor done"
	
#run msbuild
print "run msbuild..."
sln_path = ppath.setting['root'] + '/CandyCarrier/Client/'+ ppath.client_root +'/PolarClient.sln'

p = subprocess.call(["C:/Windows/Microsoft.NET/Framework64/v4.0.30319/MSBuild.exe", '/p:Configuration=Debug','/p:Platform=Win32',sln_path])
if p==1: raise Exception("msbuild Failed")
print "msbuild done"

#make file scheme

data_fold = ppath.get_data_folder()
res_file_scheme_path = data_fold + ppath.res_file_scheme
if os.path.exists(res_file_scheme_path):
	os.chmod( res_file_scheme_path, stat.S_IWRITE )
	os.remove(res_file_scheme_path)
	
print "create BuildBaseScheme ..."
os.chdir(ppath.get_output_folder())
param = "BuildBaseScheme"
subprocess.call(["PolarClient.exe", "BuildVersionInfo",param])

if not os.path.exists(res_file_scheme_path):
	raise Exception("create BuildBaseScheme failed")
	
print "BuildBaseScheme created,copy to build fold and submit"

filescheme_fold = ppath.get_filescheme_folder() + str(full_version_str) +'/'
File_Util.remove_fold(filescheme_fold)
os.mkdir(filescheme_fold) 
shutil.copy2(res_file_scheme_path, filescheme_fold)
#full-resource table
p4c.reconcile_file_ea(ppath.data_folder + ppath.res_file_scheme)
#full-resource table pool 
p4c.reconcile_fold_ea(ppath.filescheme_folder)

p4c.submit('[Jenkins submit version data ]')

#ant create apk
os.chdir(ppath.get_candy_android_path())
print "Start ant build android ..."
setting = get_setting()
os.environ["JAVA_HOME"] = setting['java_home']

p = subprocess.call([setting['ant_path'], 'clean','release',"-Dsdk.dir=" + setting['android_sdk']])
if p==1: raise Exception("ant build Failed")
print "ant build done"

ps1_path = ppath.setting['root'] + '/polar/Client/Tools/Jenkins-script/make/send_to_tfs.ps1'
apk_file = ppath.get_candy_android_path() + 'bin/PolarClient-release.apk'
candy_output = ppath.setting['root'] + '/CandyCarrier/Client/' + ppath.client_root + '/Output/'
dir_name = ppath.client_root + "-" + str(full_version_str)

print "ps1_path: " + ps1_path +"apk_file : " + apk_file + "candy_output : " + candy_output  +"dir_name : " + dir_name

ps_is_encrypted = '$false'
if is_encrypt:
	ps_is_encrypted = '$true'
tfs_dir = "Develop"
if isOnline:
	tfs_dir = "Online"
param = 'powershell -ExecutionPolicy Unrestricted {0} -output_folder {1} -apk_path {2} -root {3} -tfs_fold {4} -encrypted {5}'\
	.format(ps1_path,candy_output,apk_file,dir_name,"/Candy/" + tfs_dir + "/",ps_is_encrypted)

print "send to tfs param: " + param

os.system(param)
print 'send to tfs done'


