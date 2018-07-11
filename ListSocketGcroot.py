import sys,os,io
import pykd
import re

path = os.path.dirname(sys.argv[0])
File = os.path.join(path,'ListSocketGcroot.txt')
aFile = io.open(File, 'w', encoding='utf8')

pykd.dbgCommand('!netext.windex')
ret = pykd.dbgCommand('!wfrom -type System.Net.Sockets.Socket where($ipaddress(m_RightEndPoint)=="192.168.0.100:8888") $a("",$addr())')
reAddress = re.compile(r'^: ')
aList = [line for line in ret.split('\n') if reAddress.search(line)]
#print aList
for line in aList:
    tmpList = line.split()
    cmd = r'!gcroot %s' % (tmpList[1])
    tmpRet = pykd.dbgCommand(cmd)
    #print(cmd)
    aFile.write(tmpRet+'\n')
    aFile.flush()
aFile.close()