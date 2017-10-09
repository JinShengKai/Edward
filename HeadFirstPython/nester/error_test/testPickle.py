import pickle
import nester
new_man=[]
try:
    with open("File/man_data.txt","rb") as man_file:
        new_man=pickle.load(man_file)
        nester.print_lol(new_man)
except IOError as err:
    print("IOError",str(err))
except pickle.PickleError as err:
    print("PickleError",str(err))
