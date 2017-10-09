import nester
#pickle 腌制数据，将数据腌制到文件，持久储存，还可以从文件读到内存load()恢复数据,dump()保存数据
import pickle
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
    #打开文件显示一行数据
    #with open('File/man_data.txt') as mdf:
    #    print(mdf.readline())
    with open("File/man_data.txt",'wb') as man_file,open("File/other_data.txt",'wb') as other_file:
        #nester.print_lol(man, fn=man_file)
        #nester.print_lol(other, fn=other_file)
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)
    '''with open("File/man_data.txt",'rb') as test:
       list=pickle.load(test)
    print(list)'''
except IOError as err:
    print('File Error',str(err))
except pickle.PickleError as err:
    print('Pickle Error' , str(err))