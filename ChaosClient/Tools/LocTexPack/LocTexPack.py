#coding=utf-8
import os
import sys
import hashlib


lan = sys.argv[2]

toolpath = sys.argv[1] + '/ChaosClient/Tools/DataProcess'

tex_tmp_dir = sys.argv[1] + '/ChaosClient/Client/Output/loc/' + lan + '/data/ccb/texture_tmp'

tex_suffix = '/ChaosClient/Client/Output/loc/' + lan + '/data/ccb/texture'

tex_tag_dir = sys.argv[1] + tex_suffix

p4_dir = '//depot' + tex_suffix

p4_account = 'p4 -P maple123 -C utf8 -u chenzhenqing -p 192.168.1.251:1999 -c chaos_pack'


def tex_pack():
	#更新ui目录
	os.system(p4_account + ' sync -f //depot/ChaosArt/res/loc/' + lan + '/...#head')
	os.system(p4_account + ' sync -f //depot/ChaosArt/res/ui_editor/...#head')
	#打包texture
	print(toolpath)
	os.chdir(toolpath)
	os.system('call LocUIConverter_loc.bat ' + lan)
	
#大文件的MD5值
def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = file(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()
	
def AddAndEditFile(dir):
	newDir = dir
	if os.path.isfile(dir):
		fpath,fname =os.path.split(dir)
		rname, rext = os.path.splitext(fname)
		tmp_md5 = GetFileMd5(dir)
		if rext == '.png' or rext == '.plist':
			tag_file = tex_tag_dir + '/' + fname
			p4_file_dir  = p4_dir + '/' + fname
			print(dir)
			if os.path.exists(tag_file):
				tag_md5 = GetFileMd5(tag_file)
				if tmp_md5 == tag_md5:
					print(fname + ' is the same file')
				else:
					print(fname + ' is difference')
					os.system(p4_account + ' edit -c default ' + p4_file_dir)
			else:
				os.system(p4_account + ' add -d -f -c default ' + p4_file_dir)
				if rext == '.png':
					os.system(p4_account + ' reopen -c default -t binary ' + p4_file_dir)
				if rext == '.plist':
					os.system(p4_account + ' reopen -c default -t text ' + p4_file_dir)
				print(fname + ' is not exists')
	elif os.path.isdir(dir):  
		for s in os.listdir(dir):
			newDir=os.path.join(dir,s)
			AddAndEditFile(newDir)
			
			
def DeleteFile(dir):
	newDir = dir
	if os.path.isfile(dir):
		fpath,fname =os.path.split(dir)
		rname, rext = os.path.splitext(fname)
		tmp_md5 = GetFileMd5(dir)
		if rext == '.png' or rext == '.plist':
			tag_file = tex_tmp_dir + '/' + fname
			p4_file_dir  = p4_dir + '/' + fname
			if os.path.exists(tag_file):
				print(fname + ' exists')
			else:
				os.system(p4_account + ' delete -c default -v ' + p4_file_dir)
				print(fname + ' is not exists')
	elif os.path.isdir(dir):  
		for s in os.listdir(dir):
			newDir=os.path.join(dir,s)
			DeleteFile(newDir)
			
def submit():
	os.system('xcopy ' + '"' + tex_tmp_dir + '"' + ' ' + '"' + tex_tag_dir + '"' + ' /E /I /Q /Y /R')
	os.system(p4_account + ' submit -f revertunchanged -d ccbAutoPublish')
	
tex_pack()	
AddAndEditFile(tex_tmp_dir)
DeleteFile(tex_tag_dir)
submit()
