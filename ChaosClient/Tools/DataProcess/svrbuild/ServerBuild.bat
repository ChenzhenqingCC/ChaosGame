set ZONE=%1%
set VERSION=%2%
set BRANCH=%3%
set LANLOC=%4%
net use Y:  /del 
net use Y:  \\192.168.1.249\maple /persistent:yes 1234 /user:maple

plink -auto_store_key_in_cache -l maple   -P  36000   -pw  maple   192.168.1.249 ./autobuild.sh %ZONE% %VERSION% %BRANCH% %LANLOC%

xcopy /y Y:\package\chaos_release_%ZONE%_%VERSION%* \\192.168.1.248\share\publish\versions\%ZONE%\%VERSION%\server\

net use Y:  /del 