import os
import traceback
#得到当前路径
path=os.getcwd()
#更换文件夹
os.chdir(path+'/File')
#打开文件并指定编码格式
the_file = open('sketch.txt',encoding='utf-8')
print(the_file.readline(),end='')
the_file.seek(0)
for each_item in the_file:
    try:
        #find 可以查找一个字符串子串如果没找到就返回-1找到了就返回索引地址
        if not each_item.find(':') == -1:
            # split方法返回一个字符串列表，这会赋值给一个目标标识符列表。这称之为多重赋值 multiple assignment
            #并且split可以分解成尽可能多的字段，所以可以指定参数分成几部分，1 就是分两部分我只取第一个：有效

            (role,line_spoken) = each_item.split(':',1)
            print(role,end='')
            print(' said: ',end='')
            #print(each_item,end='')
            print(line_spoken)
    except:
        pass
the_file.close()