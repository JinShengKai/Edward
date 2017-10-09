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
    out_man=open("File/man_data.txt","w")
    out_other=open("File/other_data.txt","w")
    print(man,file=out_man)
    print(other,file=out_other)
except IOError:
    print("File error")
finally:
    out_man.close()
    out_other.close()

