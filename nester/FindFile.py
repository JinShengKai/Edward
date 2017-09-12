import os
#得到当前路径
path=os.getcwd()
#更换文件夹
os.chdir(path+'/File')
#打开文件并指定编码格式
the_file = open('sketch.txt',encoding='utf-8')
print(the_file.readline(),end='')
the_file.seek(0)
for each_item in the_file:
    print(each_item,end=' ')
the_file.close()