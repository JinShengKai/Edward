#with 是使用上下文协议来执行的，帮助关闭文件
man = []
other = []
try:
    data=open('File\sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            line_spoken=line_spoken.strip()
            if role=='Man':
                man.append(line_spoken)
            elif role=='Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is not missing')
#print(man)
#print(other)
try:
    with open("File/man_data.txt",'w') as man_file:
        print(man,file=man_file)
    with open("File/other_data.txt",'w') as other_file:
        print(other,file=other_file)
except IOError as err:
    print('File Error',str(err))