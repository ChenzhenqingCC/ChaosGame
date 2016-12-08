import shutil 
import os 
import stat
from polarpath import PolarPath

def on_readonly(func, path, excinfo):
	os.chmod(path, stat.S_IWRITE)

def remove_readonly(func, path, excinfo):
	os.chmod(path, stat.S_IWRITE)
	os.remove(path)

class File_Util(object):
	@staticmethod
	def remove_fold(full_path,remain_readonly=False):
		if os.path.exists(full_path):
			print 'remove ' + full_path
			if remain_readonly:
				shutil.rmtree( full_path, onerror = on_readonly )
			else:
				shutil.rmtree( full_path, onerror = remove_readonly )
		return full_path

	@staticmethod	
	def copy_fold(src, dest, ingore_filenames = {}):
		if not os.path.exists(dest):
			os.makedirs(dest)
		if not os.path.isdir(dest):
			raise Exception('ERROR :dest is not fold')
		File_Util.recursive_overwrite(src, dest, ingore_filenames)

	@staticmethod	
	def recursive_overwrite(src, dest, ingore_filenames):
		# print (src.encode('gb2312') + "  " + dest.encode('gb2312'))
		if os.path.isdir(src):
			if not os.path.isdir(dest):
				os.makedirs(dest)
			files = os.listdir(src)
			for f in files:
				if f not in ingore_filenames:
					dest_full = os.path.join(dest, f)
					if os.path.exists(dest_full):
						os.chmod( dest_full, stat.S_IWRITE )
					File_Util.recursive_overwrite(os.path.join(src, f), 
										dest_full, 
										ingore_filenames)
		else:
			shutil.copyfile(src, dest)
			
	@staticmethod
	def read_client_version():
		ppath = PolarPath()
		version_path = ppath.get_version_log_folder() + 'last_version'
		fp = open(version_path,"r")
		version = int(fp.readline())  
		fp.close()
		return version
		
	@staticmethod
	def read_full_version():
		ppath = PolarPath()
		client_version = File_Util.read_client_version()
		proto_version = File_Util.read_proto_version()
		return str(proto_str_version) + '.0.' + str(client_version)
		
	@staticmethod
	def write_client_version(version):
		ppath = PolarPath()
		version_path = ppath.get_version_log_folder() + 'last_version'
		os.chmod( version_path, stat.S_IWRITE )
		fp = open(version_path,"w")
		fp.write(str(version))
		fp.close()
		
	@staticmethod	
	def read_proto_version():
		ppath = PolarPath()
		version_path = ppath.get_version_log_folder() + 'proto_version'
		fp = open(version_path,"r")
		version = fp.readline()
		return version
	
	@staticmethod	
	def write_proto_version(version):
		ppath = PolarPath()
		version_path = ppath.get_version_log_folder() + 'proto_version'
		os.chmod( version_path, stat.S_IWRITE )
		fp = open(version_path,"w")
		fp.write(str(version))
		fp.close()

		
