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
sarah=get_coach_data('File/sarah2.txt')
sarah_data={}
sarah_data['NAME']=sarah.pop(0)
sarah_data['DOB']=sarah.pop(0)
sarah_data['TIME']=sarah
print(sarah_data['NAME'])