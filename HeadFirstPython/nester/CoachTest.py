import io
#该函数是实现将字符串中的不规则数据改成统一格式数据
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins,secs)=time_string.split(splitter)
    return (mins+"."+secs)
#该函数是取文件的函数
def get_coach_data(filename):
    try:
        with open(filename)  as f:
            data=f.readline()
        return data.strip().split(',')
    except IOError as err:
        print("IOError is:"+str(err))
#sorted()[0:3]从0开始取三个 set()设置集合
print(sorted(set([sanitize(t) for t in get_coach_data("File/james.txt")]))[0:3])
print(sorted(set([sanitize(t) for t in get_coach_data("File/julie.txt")]))[0:3])
print(sorted(set([sanitize(t) for t in get_coach_data("File/mikey.txt")]))[0:3])
print(sorted(set([sanitize(t) for t in get_coach_data("File/sarah.txt")]))[0:3])
# with open('File/james.txt') as jaf:
#     data=jaf.readline()
# james=data.strip().split(',')
# with open('File/julie.txt') as juf:
#     data=juf.readline()
# julie=data.strip().split(',')
# with open('File/mikey.txt') as mif:
#     data=mif.readline()
# mikey=data.strip().split(',')
# with open('File/sarah.txt') as saf:
#     data=saf.readline()
# sarah=data.strip().split(',')
#
# clean_james=[sanitize(each_itme) for each_itme in james]
# clean_julie=[sanitize(each_itme) for each_itme in julie]
# clean_mikey=[sanitize(each_itme) for each_itme in mikey]
# clean_sarah=[sanitize(each_itme) for each_itme in sarah]

# 打印去重复的集合

#
# data=[1,2,6,2,41,2]
# data2=sorted(data)
# #data.sort()
# print(data)
# print(data2)
#
# #正常迭代
#
# clean_julie=[]
# clean_mikey=[]
# clean_sarah=[]
# for each_item in james:
#     clean_james.append(sanitize(each_item))
# for each_item in julie:
#     clean_julie.append(sanitize(each_item))
# for each_item in mikey:
#     clean_mikey.append(sanitize(each_item))
# for each_item in sarah:
#     clean_sarah.append(sanitize(each_item))

#列表推倒eg：meters = [ 1,2,3 ] ;feet =[m*3.281 for m in meters]

'''
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
print(clean_james[0:3])
#去重
for item in clean_james:
    if item  not in unique_james:
        unique_james.append(item)
'''



