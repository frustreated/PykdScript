import sys,os,io
import pykd
import re

path = os.path.dirname(sys.argv[0])
File = os.path.join(path,'ModuleReferenceInKernelDump.txt')
aFile = io.open(File, 'w', encoding='utf8')

ret = pykd.dbgCommand('!process 0 0')
reAddress = re.compile(r'^PROCESS+')
aList = [line for line in ret.split('\n') if reAddress.search(line)]
#print aList
for line in aList:
    tmpList = line.split()
    cmd = r'.process /p  %s;!peb' % (tmpList[1])
    tmpRet = pykd.dbgCommand(cmd)
    #print(tmpRet)
    aFile.write(tmpRet+'\n')
    aFile.flush()
aFile.close()