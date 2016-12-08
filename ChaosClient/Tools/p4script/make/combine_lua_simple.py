#!/usr/bin/env Python
# -*- coding: UTF-8 -*-
import os.path
import subprocess
import sys
import os
import codecs
import stat

def getTextFileContent(filename):
    f = file(filename,'rb')        
    header = f.read(3) # Read just the first four bytes.
    content=f.read()
    f.close()
    if header==codecs.BOM_UTF8:
        return content
    else:
        return header+content
    
     


# def getAllLuaFiles(inFile):
#     f=open(inFile)
#     line = f.readline()
#     retVal=[]
#     while line:
#         line=line.strip()
               
#         if line.startswith("--")==False:
#             endIndex=line.find(".lua\",") 
#             if endIndex>0:
#                 startIndex=line.find("\"")
#                 line=line[startIndex+1:endIndex+4]                
#                 retVal.append(os.path.basename(line))
#         line=f.readline()
#     f.close()
#     return retVal
    
def getAllFiles(dirPath,allFileList=None,suffixName=None,deep=100):
    if allFileList is None:
        allFileList=[]

    if os.path.exists(dirPath)==False:
        return allFileList
    
    for fileName in os.listdir(dirPath):
        targetFile = os.path.join(dirPath,  fileName)
        if os.path.isfile(targetFile):
            bSuit=False
            if suffixName==None:
                bSuit=True
            elif fileName.endswith(suffixName):
                bSuit=True
                
            if bSuit:                
                allFileList.append(targetFile)
                
        elif os.path.isdir(targetFile):
            if deep>1:
                getAllFiles(targetFile,allFileList,suffixName,deep-1)
    return allFileList    
    
def delDir(dirPath):
    for fileName in os.listdir(dirPath):
        targetFile = os.path.join(dirPath,  fileName) 
        if os.path.isfile(targetFile):
            os.chmod( targetFile, stat.S_IWRITE)
            os.remove(targetFile)
        elif os.path.isdir(targetFile):
            delDir(targetFile)
            os.chmod( targetFile, stat.S_IWRITE)
            os.rmdir(targetFile)
                        
def combineLuaFiles(inDir,inFileName, bRelease = False):
    
    #allFilesNeed=getAllLuaFiles(inDir+"/"+inFileName+".lua")
    allLuaFiles=getAllFiles(inDir,None,".lua")

   # print "all files need:" , len(allFilesNeed)
    print "all lua files:" , len(allLuaFiles)

    excludeConfigFile = ""
    if bRelease:
        excludeConfigFile = "NetConfig_Debug.lua"
    else:
        excludeConfigFile = "NetConfig_Release.lua"

    print "excludeConfigFile", excludeConfigFile

    allLuaFilesTemp={}
    for f in allLuaFiles:
        key=os.path.basename(f)
        if key=="Information.lua":
            continue
        elif key=="GameProject.lua":
            continue
        elif key=="CoreProject.lua":
            continue  
        allLuaFilesTemp[key]=f
    
    allFunList=[]

    if len(allLuaFilesTemp)<10:
        return

    print "all lua files temp: " , len(allLuaFilesTemp)
    
    
    outFileList=[]
    outFile=None
    
    index=1    
    
    for f in allLuaFilesTemp:
        if allLuaFilesTemp[f] == "":
            continue    

        print f , allLuaFilesTemp[f]
        content=getTextFileContent(allLuaFilesTemp[f])
        os.chmod( allLuaFilesTemp[f], stat.S_IWRITE)
        os.remove(allLuaFilesTemp[f])

        #不合入debug 或者release版本的config file
        if f == excludeConfigFile:
            print "reach exclude config file"
            continue
                        
        #allLuaFilesTemp[f] = ""       
        funName=f.replace('.','_')
        allFunList.append(funName)

        if outFile==None:
            
            outFileName=inFileName+str(index)+".lua"            
            outFileList.append(outFileName)
            outFileName=inDir+"/"+outFileName
            outFile=open(outFileName,"w+")
            index=index+1
        
        outFile.write('local function '+funName+"()\n")
        outFile.write(content)
        outFile.write('\nend\n')

        if len(allFunList)>180:
            for f in allFunList:
                outFile.write(f+"()\n")
            allFunList=[]
            outFile.close()
            outFile=None
    
    for f in allFunList:
        outFile.write(f+"()\n")
    
    outFile.close()
    
    #luajit -b src dest
    #cmdLine="luajit/luajit -b \"" +outFileName+"\" \""+outFileName+"\""
    #retCode=subprocess.call(cmdLine)

    # for (K,V) in allLuaFilesTemp.items():
    #     if V != "":
    #         os.chmod( V, stat.S_IWRITE)
    #         os.remove(V)
    #         print(K)
    #     else:
    #         print "no need to solve" , K

    
    outFileName=inDir+"/"+inFileName+".lua"
    os.chmod( outFileName, stat.S_IWRITE)
    
    
    outFile=open(outFileName,"w")
    
    outFile.write("Booter.Project =\n{\n")
    outFile.write("Name = \"System\",\n")
    
    if inFileName=="CoreProject":
        outFile.write("\"Information.lua\",\n")
    
    
    for f in outFileList:
        outFile.write("\""+f+"\",\n")
    outFile.write("}")
    outFile.close()
        
    




def combineProjLuaFiles(scriptRootFolder,bRelease=False):
    systemDir=scriptRootFolder+"/System"
    logicDir=scriptRootFolder+"/CandyCarrierGame"
    combineLuaFiles(systemDir,"CoreProject", bRelease)
    combineLuaFiles(logicDir,"GameProject", bRelease)

    outFileName=scriptRootFolder+"/Project.lua"
    os.chmod( outFileName, stat.S_IWRITE)
    outFile=open(outFileName,"w")
    outFile.write("Booter.ProjectSolutions =\n{\n")
    
    outFile.write("\t{\n\t\tfilename = \"CoreProject.lua\",\n")
    outFile.write("\t\t path = \"System/\",\n\t},\n")

    outFile.write("\t{\n\t\tfilename = \"GameProject.lua\",\n")
    outFile.write("\t\t path = \"CandyCarrierGame/\",\n\t},\n")
        
    outFile.write("}")    
    
    delDir(scriptRootFolder+"/UnitTest")

#if __name__ == "__main__":
#    combineProjLuaFiles(destDir)
       
