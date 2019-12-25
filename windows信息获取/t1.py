import platform
from collections import deque
import zipfile

class CountdownTask:
    def run(self,file):
        '''
        遍历目录
        '''

        sys1= ''.join(platform.platform().split('-')[0:2])
        sys2 = platform.architecture()[0]  # 取出系统位数
        sys = sys1 + '-'+sys2
        print(sys1,sys2,sys)

c = CountdownTask()
res = c.run(file=r'D:\ShadowsocksR-win-4.9.0\ShadowsocksR-dotnet2.01.exe')
print(res)
