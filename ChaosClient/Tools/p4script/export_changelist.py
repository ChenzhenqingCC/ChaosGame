import sys
from P4 import P4
from export import Exprot
argv = sys.argv
client = argv[1]
user = argv[2]
changelist_no = argv[3]
print('export changelist')


p4 = P4()
p4.user = user
p4.client = client
p4.password = 'maple123'
p4.exception_level = 0
p4.connect()
p4.run_login()

info = p4.run_describe('-s',changelist_no)[0]
depotFiles = info['depotFile']
Exprot(p4,depotFiles)