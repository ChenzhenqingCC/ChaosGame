set P4CLIENT=blueice_MAODINGDING-PC_client
set P4PORT=192.168.1.251:1999
set P4USER=blueice

set BRANCH_NAME=b1
set P4_BRANCH_LOCAL_DIR=c:\Users\blueicemao\Perforce\%P4CLIENT%\branch\%BRANCH_NAME%
set DIR_TEMP=d:
set P4_LABEL=0.4.8440.8440_1

p4 sync -k %P4_BRANCH_LOCAL_DIR%\... > %DIR_TEMP%\DeleteAndBranchLog.txt
p4 delete %P4_BRANCH_LOCAL_DIR%\... >> %DIR_TEMP%\DeleteAndBranchLog.txt
p4 resolve -ay >> %DIR_TEMP%\DeleteAndBranchLog.txt
p4 submit -d "Delete old branch" >> %DIR_TEMP%\DeleteAndBranchLog.txt

p4 integrate -b %BRANCH_NAME% -v -f //...@%P4_LABEL% >> %DIR_TEMP%\DeleteAndBranchLog.txt
p4 resolve -at >> %DIR_TEMP%\DeleteAndBranchLog.txt
p4 submit -d "Integrate new branch" >> %DIR_TEMP%\DeleteAndBranchLog.txt 