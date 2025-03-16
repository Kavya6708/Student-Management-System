#StudentAdd.py<-----File Name
import pickle
from verifyDuplicateRecord import verify
class InvalidNameError(Exception):pass
class ZeroLengthError(BaseException):pass
class SpaceNameError(Exception):pass
#code for validation of Name
def Validation(name):
    if(len(name)==0):
        raise ZeroLengthError
    elif(name.isspace()):
        raise SpaceNameError
    else:
        words=name.split()#word=["Guido","van","Rossum"]
        res=True
        for word in words:
            if(not word.isalpha()):
                res=False
                break
            if(res):
                return name
            else:
                raise InvalidNameError
def Savestuddata():
    with open("STU.data","ab")as fp:
        try:
            print("---------------------")
            sno=int(input("Enter Student Number:"))
            sname=Validation(input("Enter Student Name:"))
            marks=int(input("Enter Student Marks:"))
            print("---------------------")
    #create an empty list for placing student vals
            lst=[]
            lst.append(sno)
            lst.append(sname)
            lst.append(marks)
    #save lst data to student.pick file
            pickle.dump(lst,fp)
            print("Student data saved in a file successfully")
            print("---------------------")
        except ValueError:
            print("Don't Enter Alnums,strs and symbols for stno and marks")
        except InvalidNameError:
            print("Invalid Name------>try Again")
        except ZeroLengthError:
            print("Try to enter Ur Name")
        except SpaceNameError:
            print("Don't enter space for Ur Name---->try again:")






