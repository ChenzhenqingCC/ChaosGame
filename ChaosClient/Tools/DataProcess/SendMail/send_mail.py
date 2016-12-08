#coding=utf-8
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage  
from email.header import Header
import os
import sys

#发送方邮箱地址
sender = 'auto@maplegame.cn'  
#接收方邮箱地址 支持list
receiver = 'evence_chen@hotmail.com'  
smtpserver = 'smtp.exmail.qq.com' 
#发送方邮箱账号
username = 'auto@maplegame.cn'  
#发送方邮箱密码
password = 'MapleGame1013'  

def mail(Recv, Title, Content): 
	receivers = Recv.split(',');
	msgRoot = MIMEText(Content.decode('gbk'),'plain','utf-8') 	
	#邮件标题
	msgRoot['Subject'] = Title.decode('gbk')
			  
	smtp = smtplib.SMTP()  
	smtp.connect(smtpserver)  
	smtp.login(username, password)  
	smtp.sendmail(sender, receivers, msgRoot.as_string())  
	smtp.quit()

if __name__ == '__main__':
	Recv = sys.argv[1]
	Title = sys.argv[2]
	Content = sys.argv[3]
	mail(Recv, Title, Content)