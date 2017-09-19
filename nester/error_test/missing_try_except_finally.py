'''标准try except finally'''
try:
    data=open("missing.txt")
    print(data.readline(),end='')
#except IOError:
#为异常对象命名为err然后做输出
except IOError as err:
    #print('File error'+err)失败，出现一个TypeError因为err变量并不是字符串类型，使用str()进行强制类型转换
    print("File error"+str(err))
finally:
    #locals()BIF返回当前作用域中定义的所有名的一个集合
    #因为文件不存在，所以data对象并未创建，locals返回的集合中没有搜索到字符串data
    if 'data' in locals():
        data.close()