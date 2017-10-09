import pickle
from Python_Class import AthleteList
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        templ = data.strip().split(",")
        return (AthleteList(templ.pop(0),templ.pop(0),templ))
    except IOError as err:
        print('File Eroor:'+str(err))
        return (None)
def put_to_store(file_list):
    all_athletes={}
    for item in file_list:
        ath=get_coach_data(item)
        #all_athletes['name']=ath
        all_athletes[ath.name]=ath
    try:
        with open('athlete_pickle','wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as err:
        print("ERROR为"+str(err))
    return (all_athletes)
def get_from_store():
    all_athletes={}
    try:
        with open("athlete_pickle",'rb') as athf:
            all_athletes=pickle.load(athf)
    except IOError as err:
        print("ERROR为"+str(err))
    return (all_athletes)
the_files=['james2.txt','sarah2.txt','julie2.txt','mikey2.txt']
data=put_to_store(the_files)
print(data)
for each_athlete in data:
    print(data[each_athlete].name+'  '+data[each_athlete].dob)