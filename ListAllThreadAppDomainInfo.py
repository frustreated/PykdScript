import sys,os,io
import pykd
import re

path = os.path.dirname(sys.argv[0])
File = os.path.join(path,'ListAllThreadsAppDomainInfo.txt')
aFile = io.open(File, 'w', encoding='utf8')


ret = pykd.dbgCommand('!mex.mthreads')
reAddress = re.compile(r'^[(]t[)]')
aList = [line for line in ret.split('\n') if reAddress.search(line)]
#print aList
for line in aList:
    tmpList = line.split()
    cmd = r'!mex.ddt clr!THREAD %s m_pDomain' % (tmpList[4])
    tmpRet = pykd.dbgCommand(cmd)
    #print(tmpList[4])
    aFile.write('Thread ' + tmpList[2] + ':' +tmpRet+'\n')
    aFile.flush()
aFile.close()