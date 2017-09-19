import io

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins,secs)=time_string.split(splitter)
    return (mins+"."+secs)
with open('File/james.txt') as jaf:
    data=jaf.readline()
james=data.strip().split(',')
with open('File/julie.txt') as juf:
    data=juf.readline()
julie=data.strip().split(',')
with open('File/mikey.txt') as mif:
    data=mif.readline()
mikey=data.strip().split(',')
with open('File/sarah.txt') as saf:
    data=saf.readline()
sarah=data.strip().split(',')

'''data=[1,2,6,2,41,2]
data2=sorted(data)
#data.sort()
print(data)
print(data2)'''
#正常迭代
'''
clean_julie=[]
clean_mikey=[]
clean_sarah=[]
for each_item in james:
    clean_james.append(sanitize(each_item))
for each_item in julie:
    clean_julie.append(sanitize(each_item))
for each_item in mikey:
    clean_mikey.append(sanitize(each_item))
for each_item in sarah:
    clean_sarah.append(sanitize(each_item))
'''
#列表推倒eg：meters = [ 1,2,3 ] ;feet =[m*3.281 for m in meters]
clean_james=[sanitize(each_itme) for each_itme in james]
clean_julie=[sanitize(each_itme) for each_itme in julie]
clean_mikey=[sanitize(each_itme) for each_itme in mikey]
clean_sarah=[sanitize(each_itme) for each_itme in sarah]

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
