from p4setting import get_setting
from P4 import P4
from file_util import File_Util
from polarpath import PolarPath
import os

class P4Controller(object):
	setting = {}
	ppath = PolarPath()
	def __init__(self):
		self.setting = get_setting()
		p4 = P4()
		p4.user = self.setting['user']
		p4.host = self.setting['host']
		p4.client = self.setting['client']
		p4.password = self.setting['password']
		p4.exception_level = 0
		p4.connect()
		p4.run_login()
		self.p4 = p4
		
	#relate_path: /Client/Build/Test/
	def get_p4_path(self,relate_path):
		return '//' + self.setting['client'] + relate_path
	
	#path must end with '/'
	def reconcile_fold_ea(self,relate_path):
		if not relate_path[-1] == '/':
			raise Exception("path " + relate_path + " not end with / ")
		p4_path = self.get_p4_path(relate_path)
		p4_path = p4_path + '...'
		print "p4 reconcile fold " + p4_path
		self.p4.run_reconcile('-e','-a',p4_path)
		
	def reconcile_fold_ead(self,relate_path):
		if not relate_path[-1] == '/':
			raise Exception("path " + relate_path + " not end with / ")
		p4_path = self.get_p4_path(relate_path)
		p4_path = p4_path + '...'
		print "p4 reconcile fold -e -a -d" + p4_path
		self.p4.run_reconcile('-e','-a','-d',p4_path)
		
	def reconcile_file_ea(self,relate_file_path):
		p4_path = self.get_p4_path(relate_file_path)
		self.p4.run_reconcile('-e','-a',p4_path)

	def clean(self,relate_file_path):
		ticket = self.p4.run_tickets()[0]['Ticket']
		local_path = self.ppath.get_local_path(relate_file_path)
		File_Util.remove_fold(local_path,True)
		p4_path = self.get_p4_path(relate_file_path) + '...'
		print 'run_sync ' + p4_path
		os.system('p4 -P ' + ticket + ' diff -sd ' + p4_path + '| p4 -P ' + ticket + ' -x - sync -f -q ' )
		#self.p4.run_sync('-f',p4_path)

	def submit(self,description):
		print self.p4.run_submit('-f', 'revertunchanged', '-d', description)