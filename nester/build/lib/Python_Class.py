import io
import os
import pickle

        #the code to initialize a "Athlete" object
# sarah=Athlete('Sarah Sweeney','2002-6-17',['2:58','2.58','1.56'])
# james=Athlete('James Jones')
# print(type(sarah))
# print(type(james))
def sanitized(time_list):
    if '-' in time_list:
        splitter = '-'
    elif ':' in time_list:
        splitter = ':'
    else :
        return  time_list
    (mins,secs)=time_list.split(splitter)
    return (mins+'.'+secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        templ = data.strip().split(",")
        #不pop就是全部

        #print(templ)
        return (Athlete(templ.pop(0),templ.pop(0),templ))
    except IOError as err:
        print('File Eroor:'+str(err))
        return (None)

class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        #类中每个方法的第一个参数都是self，下面定义了三个属性并用形参赋值
        self.name=a_name
        self.dob=a_dob
        self.time=a_times
    def top3(self):
        return (sorted(set([sanitized(t) for t in self.time]))[0:3])
    def add_time(self,time):
        self.time.append(time)
    def add_times(self,times):
        self.time.extend(times)
james=get_coach_data("File/james2.txt")
print(james.name+"'s fastest times are :"+str(james.top3()))

class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name=a_name
        self.dob=a_dob
        self.extend(a_times)
    def top3(self):
        return (sorted(set([sanitized(t) for t in self]))[0:3])

vera = AthleteList('vera vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22','1-21','2:22'])
print(vera.top3())