import shutil 
import os 
import stat
from polarpath import PolarPath

def on_rm_error( func, path, exc_info):
    os.chmod( path, stat.S_IWRITE )

class VersionConfig(object):
	@staticmethod
	def remove_fold(full_path):
		if os.path.exists(full_path):
			print 'remove ' + full_path
			shutil.rmtree( full_path, onerror = on_rm_error )
		return full_path



		
