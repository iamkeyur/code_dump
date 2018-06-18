import codecs
import os
import re
import Log

import Functions as F

def getAllDebugLogswithFilePath(repo):
    logList=[]
    for rp in repo:
        for root, dirs, files in os.walk(rp):
            for file in files:
                if file.endswith(".java"):
                    # print os.path.join(root, file)
                    with codecs.open(os.path.join(root, file), "r", encoding='utf-8', errors='ignore') as javaFile:
                        fileContents = javaFile.read()
                        lines = fileContents.split("\n")
                        for i  in range(0,len(lines)):
                            if ".debug(" in lines[i] or ".trace(" in lines[i]:
                                out=''
                                startLine = i;
                                while not lines[i].rstrip().strip("}").strip(")").endswith(";"):
                                    out += lines[i].lstrip().rstrip().strip("\n")
                                    i+=1
                                out += lines[i].lstrip().rstrip()+"\n"
                                logObject = Log.LogClass(out,os.path.join(root, file).replace(rp,"/"),startLine)
                                logList.append(logObject)
                                # out += lines[i].lstrip().rstrip()+"<SEP>"+str(startLine)+"<SEP>"+os.path.join(root, file)+"<SEP>"+getImports(fileContents)+"\n"

    return logList;


#repository's files path
repo = ["hadoop","camel"]

Logs = getAllDebugLogswithFilePath(repo)


def checkLibrary(imports):
    if "org.slf4j.Logger" in imports:
        return False
    else:
        return True;

count = 0
for log in Logs:
    # logObject =
    # logStatement = log.split("<SEP>")[0]
    # index = log.split("<SEP>")[1]
    # filePath = log.split("<SEP>")[2]
    # imports = log.split("<SEP>")[3].split("||")
    logStatement = log.getStatement()
    index = log.getPosition()
    filePath = log.getFileName()
    imports = log.getFileImports()
    if checkLibrary(imports):
        if log.getStatement().count("+")>4:
            fileContent = open(filePath).read().split("\n")
            i = index-1
            beforeLog=''
            while i>0 and (";" in fileContent[i]):
                beforeLog+= str(fileContent[i])+"\n"
                i-=1
            beforeLog += str(fileContent[i]) + " "
            condition = 'is'+str(log.getLevel()).title()+'Enabled()'

            if condition not in beforeLog:
                count+=1
                print count
                print filePath
                print beforeLog
                print logStatement
                print "There is no debug level guard"
                # print ("\n".join(imports.split("||")))
                print "_______________________________"


