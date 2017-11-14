import sys,os,io
import pykd
import re

path = os.path.dirname(sys.argv[0])
File = os.path.join(path,'NonMicrosoftModule.txt')
aFile = io.open(File, 'w', encoding='utf8')

ret = pykd.dbgCommand('lm')
reAddress = re.compile(r'^\d+')
aList = [line for line in ret.split('\n') if reAddress.search(line)]
for line in aList:
    tmpList = line.split()
    cmd = r'lmvm %s' % (tmpList[2])
    #print(cmd)
    #aFile.write(cmd+'\n')
    tmpRet = pykd.dbgCommand(cmd)
    if 'CompanyName:      Microsoft Corporation' in tmpRet:
        #print(tmpList[2])
        continue
    #else:
        #print(tmpList[2])
    print(tmpRet)
    aFile.write(tmpRet+'\n')
    aFile.flush()

aFile.close()