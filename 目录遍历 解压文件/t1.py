from collections import deque
import zipfile

class CountdownTask:
    def un_zip(self, file_name):
        '''
        解压ZIP文件
        :param file_name: ZIP文件路径
        :return: 0为失败，1为成功
        '''
        print('准备解压文件 %s' % (file_name.split('\\')[-1]))
        try:
            f = zipfile.ZipFile(file_name)
            f.extractall(file_name.split('.zip')[0] + "/")
            f.close()
            print('解压成功: {}'.format(file_name))
        except Exception as e:
            print(e)
            return 0
        return 1
    def check_dir(self, path):
        '''
        遍历目录
        '''
        import os
        for root, dirs, files in os.walk(path):
            for name in files:
                print(os.path.join(root, name))
                print(root)
            print(' *'*10)
            for name in dirs:
                print(os.path.join(root,name))

c = CountdownTask()
res = c.check_dir(path=r'C:\Users\pt\Desktop\python')
print(res)
