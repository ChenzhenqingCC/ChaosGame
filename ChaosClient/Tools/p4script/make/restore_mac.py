import os
import os.path
from subprocess import Popen, PIPE, STDOUT
workplace = "polar_workplace"
os.system('/Application/p4 set P4CLIENT ' + workplace)

#get p4 ticket
p = Popen(['/Applications/p4', 'login','-a','-p'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
grep_stdout = p.communicate(input='PIR5363pi')[0]
lines = grep_stdout.split('\n') 
ticket = lines[len(lines) - 2]

p4FilePath = '//' + workplace + '/Client/PolarClientVersion/Output/data/script/...'

filePath = '/Users/plutopapa/polar_workplace/Client/PolarClientVersion/Output/data/script/'

if not os.path.exists(filePath):
	raise Exception("script already removed!")

os.system('rm -rf ' + filePath )

os.system('/Applications/p4 -P ' + ticket + ' diff -sd ' + p4FilePath + '| /Applications/p4 -P ' + ticket + ' -x - sync -f' )

p4FilePath = '//' + workplace + '/Client/PolarClientVersion/Output/data/table/...'

filePath = '/Users/plutopapa/polar_workplace/Client/PolarClientVersion/Output/data/table/'

if not os.path.exists(filePath):
	raise Exception("script already removed!")

os.system('rm -rf ' + filePath )

os.system('/Applications/p4 -P ' + ticket + ' diff -sd ' + p4FilePath + '| /Applications/p4 -P ' + ticket + ' -x - sync -f' )
#restore lua done
print "restore lua done"
