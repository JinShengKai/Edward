import os
path=os.getcwd()
'''读取文件'''
os.chdir(path+'/File')
the_file = open('上古强身术.txt',encoding='utf-8')
print(the_file.readline(),end='')
the_file.seek(0)
for each_item in the_file:
    print(each_item,end=' ')
the_file.close()