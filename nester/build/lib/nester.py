import sys
#coding=utf-8
#定义个列表
#movies = ["a", "b", "c", ["d", "e", "f", ["g", "e"]]]
"""这个函数是用来进行多维列表遍历输出的"""
def print_lol(The_List):
     for i in The_List:
        #判断是否是列表
        if isinstance(i, list):
            #如果是，递归调用这个函数。python默认递归深度不超过100
            print_lol(i)
        else:
            #如果不是，打印元素
            print(i)
#调用函数
#print_lol(movies)
#indent 为控制缩进
#增加对标准输出的设置
def print_lol(the_list,indent=False,level=0,fn=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fn)
        else:
            if indent:
                for range_item in range(level):
                    #使fn参数被使用，print 到 输出 到文件
                    print("\t",end='',file=fn)
            print(each_item,file=fn)