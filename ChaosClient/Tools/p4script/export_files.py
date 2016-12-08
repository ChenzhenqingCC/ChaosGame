import sys
from P4 import P4
from export import Exprot
argv = sys.argv
client = argv[1]
user = argv[2]

p4 = P4()
p4.user = user
p4.client = client
p4.password = 'maple123'
p4.exception_level = 0
p4.connect()
p4.run_login()

depot_paths = []
num = len(argv)
for i in range(3, num):
	arg = argv[i]
	fstats = p4.run_fstat(arg)
	for fstat in fstats:
		depot_paths.append(fstat['depotFile'])

print(depot_paths)
Exprot(p4,depot_paths)
