from polarpath import PolarPath
from p4controller import P4Controller

ppath = PolarPath()
p4c = P4Controller()

p4c.clean(ppath.data_folder + 'script/')
print "restore script done"
p4c.clean(ppath.data_folder + 'table/')
print "restore table done"
