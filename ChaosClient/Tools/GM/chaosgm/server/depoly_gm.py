#-*- coding: utf-8 -*-
#!/usr/bin/python
import paramiko
import threading
import sys
import os

import config

USERNAME = config.USERNAME   
PASSWD = config.PASSWD    
PORT =  config.PORT
PKGTARDIR = config.PKGTARDIR
PKGSRCDIR = config.PKGSRCDIR
SVRROOT = config.SVRROOT
# ----------------服务器信息-----------------------------
# os_type : 系统类型(0:安卓,IOS越狱混服 1:硬核联盟 2:空缺 3:IOS正版 4:苹果审核 5 应用宝) 给客户端的os_type
# wx_os_type: 用来上报wx支撑平台 (1:安卓,IOS越狱混服 2:硬核联盟 3:应用宝 4:IOS正版)

# -------------------------------------------------------

def ssh2(ip,port,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port,username,passwd,timeout=5)

        stdin, stdout, stderr = ssh.exec_command(cmd)
        print stdout.read()
        print '%s\tOK\n'%(ip)
        ssh.close()
    except Exception, detail:
        print '%s\tError'%(ip)
        print detail

def doStop(SVRLIST,*args):
    print "Begin Stop......"   
    for svr in SVRLIST:
        ip = svr['intranet']
        svrchaos = SVRROOT + svr['dir']
        cmd = 'cd ' + svrchaos + 'ChaosServer; ./stop.sh'         
        a=threading.Thread(target=ssh2,args=(ip,PORT,USERNAME,PASSWD,cmd))        
        a.start()

def doStart(SVRLIST,*args):
    print "Begin Start......"   
    for svr in SVRLIST:
        ip = svr['intranet']
        svrchaos = SVRROOT + svr['dir']
        cmd = 'cd ' + svrchaos + 'ChaosServer; ./start.sh'                
        a=threading.Thread(target=ssh2,args=(ip,PORT,USERNAME,PASSWD,cmd))        
        a.start()

def doFresh(SVRLIST, db_clean = True):
    print "Begin fresh env......"
    for svr in SVRLIST:
        ip = svr['intranet']
        svrchaos = SVRROOT + svr['dir']
        # PORT=$1 SERVER_ID=$2 SERVER_NAME=$3 OS_TYPE=$4 WX_TYPE=$5 MYSQL_DB=$6 MYSQL_OSS=$7 CHAOSSVR_IP=$8 SKIP_FRESH_DB=$9 #默认不清,0表示清
        cmd = 'cd '+svrchaos+'ChaosServer/tools; ./svr_fresh_wx.sh '+svr['port']+' '+svr['id']+' '+svr['name']+' '+svr['os_type']+' '+svr['wx_os_type']+' '+svr['db']+' '+svr['db_oss']+' '+svr['intranet']
        # 默认不清DB
        if db_clean != True:
            cmd = cmd + ' 0'

        a=threading.Thread(target=ssh2,args=(ip,PORT,USERNAME,PASSWD,cmd))        
        a.start()

def doTar(SVRLIST, filename,*args):
    print "Begin tar to ChaosServer...... filename " + filename
    pkg = PKGTARDIR + filename
    for svr in SVRLIST:
        ip = svr['intranet']
        svr_dir = svr['dir']
        svrchaos = SVRROOT + svr_dir
        cmd = 'cd ' + SVRROOT + '; mkdir ' + svr_dir + '; tar -xzf ' + pkg + ' -C ' + svrchaos        
        a=threading.Thread(target=ssh2,args=(ip,PORT,USERNAME,PASSWD,cmd))        
        a.start()

def hotfixCode(SVRLIST,*args):
    print "Begin hotfix code......"
    for svr in SVRLIST:
        ip = svr['intranet']
        svrchaos = SVRROOT + svr['dir']
        cmd = 'cd '+svrchaos+'ChaosServer/chaos_svr; ./reload.sh '

        a=threading.Thread(target=ssh2,args=(ip,PORT,USERNAME,PASSWD,cmd))        
        a.start()

def hotfixRes(SVRLIST,*args):
    print "Begin hotfix res......"
    for svr in SVRLIST:
        ip = svr['intranet']
        svrchaos = SVRROOT + svr['dir']
        cmd = 'cd '+svrchaos+'ChaosServer/chaos_svr; ./res_reload.sh '

        a=threading.Thread(target=ssh2,args=(ip,PORT,USERNAME,PASSWD,cmd))        
        a.start()

def monitor(SVRLIST,*args):
    print "Begin monitor chaos_svr......"
    for svr in SVRLIST:
        ip = svr['intranet']
        svrchaos = SVRROOT + svr['dir']
        cmd1 = 'cd '+svrchaos+'ChaosServer/chaos_svr; ./erlcall ets info [ets_actor_dirty_idx]'
        cmd2 = 'cd '+svrchaos+'ChaosServer/chaos_svr; ./erlcall ets info [ets_actor_msg_box_dirty_idx]'

        a=threading.Thread(target=ssh2,args=(ip,PORT,USERNAME,PASSWD,cmd1))        
        a.start()
        b=threading.Thread(target=ssh2,args=(ip,PORT,USERNAME,PASSWD,cmd2))        
        b.start()

def scp(ip, port, username, passwd, src, tar):    
    try:      
        ssh = paramiko.SSHClient()        
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, passwd, timeout=5)                  
        
        ftp = ssh.open_sftp()
        ftp.put(src, tar) 
        ftp.close
        
        print '%s\tOK\n'%(ip)        
        ssh.close()    
    except Exception, detail:
        print '%s\tError'%(ip)
        print detail

def doUpPkg(filename):
    src = PKGSRCDIR + filename
    if not os.path.exists(src):
        print "Can not find file %s"%(src)
        sys.exit(0)

    tar = PKGTARDIR + filename
    print "Begin Up Pkg %s ......"%(src)
    L = []
    for svr in SVRLIST:
        ip = svr['ip']
        if not L.count(ip) > 0:        
            a=threading.Thread(target=scp,args=(ip,PORT,USERNAME,PASSWD,src,tar))        
            a.start()
            L.append(ip)

def CMD(cmd):
    print "Begin Cmd %s ......"%(cmd)
    for svr in SVRLIST:
        ip = svr['ip']        
        a=threading.Thread(target=ssh2,args=(ip,PORT,USERNAME,PASSWD,cmd))        
        a.start()

def usage():
    print 'up_pkg           --send svr_pkg to all svr. (parm pkg_name)'
    print 'stop             --stop svr. '
    print 'start            --start svr. '
    print 'fresh            --fresh env. (parm default not recreate db)'
    print 'tar              --untar svr_pkg. (parm pkg_name)'
    print 'cmd              --cmd'
 
