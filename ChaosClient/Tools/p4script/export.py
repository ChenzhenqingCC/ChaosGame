import sys
import os
import subprocess
import stat
from P4 import P4
# import re

p4 = None

def is_opened(depot_path):
	opened = p4.run_opened('-C',p4.client,'-u',p4.user)
	for info in opened:
		if info['depotFile'] == depot_path :
			return True


# 由于项目p4命令行不带reconcile接口，自己实现一个简单版本的
def reconcile(depot_path, open_path_list, open_name_list):
	# 先试图add
	where_info = p4.run_where(depot_path)[0]
	client_path = where_info['path']
	p4.run_add('-d',client_path)
	# 再试图edit
	p4.run_edit(depot_path)
	p4.run_revert('-a' , '-c' , 'default')
	if is_opened(depot_path):
		open_path_list.append(depot_path)
		base_file_name = os.path.basename(client_path)
		open_name_list.append(base_file_name)
		return True
	else:
		return False


def set_all_file_readable(path):
	if os.path.isdir(path):
		files = os.listdir(path)
		for f in files:
				full_path = os.path.join(path, f)
				if os.path.isdir(full_path):
					set_all_file_readable(full_path)
				else:
					os.chmod(full_path, stat.S_IWRITE )
	else:
		os.chmod(path, stat.S_IWRITE )


def Exprot(p_p4,depot_files):
	global p4
	p4 = p_p4
	# 更新ui资源目录
	p4.run_sync('//depot/ChaosArt/res/ui_editor/...')
	ui_publish_depot = '//depot/ChaosArt/res/ui_editor_publish/...'
	p4.run_sync(ui_publish_depot)
	# 将ui_publish设为可写，防止ccb builder导不出ccbi
	where_info = p4.run_where(ui_publish_depot)[0]
	ui_publish_path = where_info['path']
	ui_publish_path = ui_publish_path.replace('...','')
	set_all_file_readable(ui_publish_path)
	# 获取工具目录
	TOOL_P4_DIR = "//depot/ChaosClient/Tools/DataProcess/ui_convert_single.bat"
	tool_file = p4.run_fstat(TOOL_P4_DIR)[0]['clientFile']
	tool_dir = os.path.dirname(tool_file)
	# 拷贝publish目录下所有ccbi到output目录
	p = subprocess.Popen('copy_ccbi',shell=True,cwd=tool_dir)
	p.wait()

	ui_editor_path = '//depot/ChaosArt/res/ui_editor'
	client_ccbdir_path = '//depot/ChaosClient/Client/Output/data/ccb'
	texture_path = '//depot/ChaosClient/Client/Output/data/ccb/texture'

	change_files = []
	change_names = []

	for path in depot_files:
		if path.endswith('.ccb'):
			fstat = p4.run_fstat(path)[0]

			local_file_path = fstat['clientFile']
			depot_file_path = fstat['depotFile']
			base_file_name = os.path.basename(local_file_path)
			print("ResConverter " + base_file_name)
			# 更新图片
			args = 'ResConverter ui ..\\..\\..\\ChaosArt\\res\\ui_editor ..\\..\\Client\\Output\\data\\ccb {0}'.format(base_file_name)
			p = subprocess.Popen(args,shell=True,cwd=tool_dir)
			p.wait()
			p = subprocess.Popen('ResConverter_bat',shell=True,cwd=tool_dir)
			p.wait()
			# 加入更新图片至pending list
			file_pre_name = base_file_name.split('.')[0]
			pic_path = texture_path+'/'+file_pre_name+'.png'

			if reconcile(pic_path, change_files, change_names):
				pic_plist_path = texture_path + '/' + file_pre_name + '.plist'
				reconcile(pic_plist_path, change_files, change_names)

			# 加入更新ccbi至pending list
			relative_path = os.path.relpath(depot_file_path,ui_editor_path)
			ccbi_path = os.path.join(client_ccbdir_path,relative_path)+'i'
			ccbi_path = ccbi_path.replace('\\','/')
			reconcile(ccbi_path, change_files, change_names)

	if len(change_files) > 0:
		changelist = p4.fetch_change()
		changelist._files = change_files
		changelist._description = 'Export:'+str(change_names)
		print(p4.save_change(changelist))
		# 获取change_id
		# r = re.compile("Change ([1-9][0-9]*) created.")
		# m = r.match(result[0])
		# change_id = "0"
		# if m: change_id = m.group(1)
	else:
		print('no changes')

