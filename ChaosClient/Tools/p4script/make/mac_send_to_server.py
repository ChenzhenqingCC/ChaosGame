import shutil  
import os  
import os.path 
import sys
import subprocess 

#/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 /Users/plutopapa/polar_workplace/Client/Tools/Jenkins-script/mac_send_to_server.py
#send file to server
#"root|10.1.164.53|36000|/data/htdocs/polar/package/client|seed@DEVy1"

def on_rm_error( func, path, exc_info):
    # path contains the path of the file that couldn't be removed
    # let's just assume that it's read-only and unlink it.
    os.chmod( path, stat.S_IWRITE )
    # os.unlink( path )
	
def clean_fold(root_path,fold):
	full_path = root_path + fold
	full_path = os.path.abspath(full_path)
	if os.path.exists(full_path):
		shutil.rmtree( full_path, onerror = on_rm_error )
	return full_path

def copy_file(file,target_folder,taret_name):
	if not os.path.exists(target_folder):	
		os.makedirs(target_folder)
	targetFile = target_folder + '/' + taret_name
	shutil.copyfile(file,targetFile) 

version = os.getenv('version', 0)
compare_version = os.getenv('compare_version', 0)

if 0 in (version, compare_version) :
	raise Exception("Need version and compare_version")

temp_path = os.path.normcase("/Users/plutopapa/polar_workplace/Client/PolarClientVersion/Build/Temp")


scp_info = os.getenv('scp_info', '')
print "get_scp_info " + scp_info
strs = scp_info.split("|")
print "len " + str(len(strs))
if len(strs) < 5:
	raise Exception("scp_info error format")

ipa_file = "/Users/plutopapa/polar_workplace/PolarClient.ipa"
#bbxhz_1.1.0.12_patch.xml
clean_fold(temp_path,'/package')
ipa_name = "bbxhz_" + version + "_pkg.ipa"
copy_file(ipa_file,"/Users/plutopapa/polar_workplace/Client/PolarClientVersion/Build/Temp/package",ipa_name)

send_files = ['./Temp/package']
os.chdir('/Users/plutopapa/polar_workplace/Client/PolarClientVersion/Build')
for file in send_files: 
	if not os.path.exists(file):
		raise Exception(file + " not exist")
	cmd = r'./BUILD.sh {0} {1} {2} {3} {4} {5}'.format(strs[0],strs[1],strs[2],strs[3],strs[4],file)
	os.system(cmd)
	
print "copy files to server DONE"





