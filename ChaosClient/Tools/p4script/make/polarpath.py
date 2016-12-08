from p4setting import get_setting
# coding=utf-8
import os  

client_root = os.getenv('client_root', 'PolarClient')
def get_p4_path(relate_to_clientroot):
	return '/CandyCarrier/Client/' + client_root + relate_to_clientroot

class PolarPath(object):
	setting = get_setting()
	res_file_scheme = 'res_file_scheme.xml'
	client_root = client_root
	android_folder = get_p4_path('/PolarClient/proj.android/')
	android_res_folder = get_p4_path('/PolarClient/proj.android/res/raw/')
	video_folder = get_p4_path('/Output/data/video/')
	client_level_folder = get_p4_path('/Output/data/table/levels/')
	version_log_folder = get_p4_path('/Build/version/')
	data_folder = get_p4_path('/Output/data/')
	output_folder = get_p4_path('/Output/')
	filescheme_folder = get_p4_path('/Build/FileScheme/')
	information_path = get_p4_path('/Output/data/script/System/Information.lua')

	tool_path = '/Client/Tools/'
	design_level_folder_1 = unicode('/polar/Doc/关卡设计存放/Polar关卡/最新关卡/', "utf8")
	design_level_folder_2 = unicode('/polar/Doc/关卡设计存放/辅线最新关卡/', "utf8")
	design_level_folder_3 = unicode('/polar/Doc/关卡设计存放/活动课/', "utf8")
	

	def get_local_path(self,relate_path):
		return self.setting['root'] + relate_path
		
	def get_client_level_folder(self):
		return self.get_local_path(self.client_level_folder)
		
	def get_design_level_folder_1(self):
		return self.get_local_path(self.design_level_folder_1)
		
	def get_design_level_folder_2(self):
		return self.get_local_path(self.design_level_folder_2)
		
	def get_design_level_folder_3(self):
		return self.get_local_path(self.design_level_folder_3)
		
	def get_version_log_folder(self):
		return self.get_local_path(self.version_log_folder)
		
	def get_data_folder(self):
		return self.get_local_path(self.data_folder)
		
	def get_output_folder(self):
		return self.get_local_path(self.output_folder)
		
	def get_filescheme_folder(self):
		return self.get_local_path(self.filescheme_folder)
		
	def get_android_folder(self):
		return self.get_local_path(self.android_folder)
		
	def get_android_res_folder(self):
		return self.get_local_path(self.android_res_folder)
		
	def get_video_folder(self):
		return self.get_local_path(self.video_folder)
		
	def get_information_path(self):
		return self.get_local_path(self.information_path)

	def get_tool_path(self):
		return self.get_local_path("/polar/Client/Tools/")

	def get_candy_android_path(self):
		return self.setting['root'] + '/CandyCarrier/Client/'+client_root  +'/PolarClient/proj.android/'
	
	