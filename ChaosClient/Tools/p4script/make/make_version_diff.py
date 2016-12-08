import shutil  
import os  
import os.path 
import sys
from subprocess import Popen, PIPE, STDOUT


new_output_path = os.path.normcase("E:\client\Client\PolarClient\Output")

def create_version_info(output_path):
	file_path = output_path + r'\info\res_file_scheme.xml'
	file_path = os.path.abspath(file_path) 
	if not os.path.exists(file_path):
		os.chdir(output_path)
		os.system('PolarClient.exe BuildVersionInfo BuildBaseScheme')
	if os.path.exists(file_path) == False :
		print "error with create version xml,quit"
		sys.exit()
	return file_path
	

print "create new version xml"
new_info_xml_path = create_version_info(new_output_path)

raise Exception("Done")
old_output_path = os.path.normcase("E:\pc_422")
print "create old version xml"
old_info_xml_path = create_version_info(old_output_path)

copy_targetDir = new_output_path + r'\compare_info'
copy_targetDir = os.path.abspath(copy_targetDir)

if not os.path.exists(copy_targetDir):  
    os.makedirs(copy_targetDir)  

copy_targetFile = copy_targetDir + r'\res_file_scheme.xml'
copy_targetFile = os.path.abspath(copy_targetFile)
print "cope old version xml to new one..."
shutil.copyfile(old_info_xml_path,copy_targetFile )  
print "CreateDiffResDirX xml..."
os.chdir(new_output_path)
Popen(['PolarClient.exe', 'BuildVersionInfo','CreateDiffResDirX|/compare_info/res_file_scheme.xml|/info/res_file_scheme.xml|diff_pack/polar'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)


