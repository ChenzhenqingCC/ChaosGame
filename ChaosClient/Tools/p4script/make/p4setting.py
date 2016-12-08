import platform

wallace_pc = { 'user'    : 'wallacewu',
        'host'    : '',
        'client'  : 'polar_p4--753395506',
        'password': 'Lily1234',
		'root'    : 'E:/client',
		'java_home': 'D:/Program Files/Java/jdk1.7.0_45',
		'ant_path':'E:/apache-ant-1.9.3/bin/ant.bat',
        'p4_cmd'  :'p4',
        'android_sdk':'E:/adt-bundle/adt-bundle-windows-x86_64-20131030/sdk'
       }
	   
wallace_mac = { 'user'    : 'wallacewu',
        'host'    : 'PAPA-of-Plutos-iMac.local',
        'client'  : 'polar_workplace',
        'password': 'Lily1234',
		'root'    : '/Users/plutopapa/polar_workplace',
		'java_home': 'D:/Program Files/Java/jdk1.7.0_45',
        'p4_cmd'  :'Applications/p4'
       }
	   
def get_setting():
	if platform.system() == 'Windows':
		return wallace_pc
	else:
		return wallace_mac
	end
