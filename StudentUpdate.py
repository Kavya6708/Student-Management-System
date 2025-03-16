#StudentUpdate.py
import pickle
from StudentAdd import Validation,InvalidNameError,ZeroLengthError,SpaceNameError
def Updaterecord():
    try:
        with open("STU.data","rb") as rp:
            records=list()
            while(True):
              try:
                 record=pickle.load(rp)
                 records.append(record)
              except EOFError:
                 break
    except FileNotFoundError:
        print("File Does not Exist")
#out-off 'with open() as' Indendation
#accept the Student Number for updating sname and marks
    try:
        sno=int(input("Enter student Number to Update the Records:"))
        found=False
        for i in range(len(records)):
            if(records[i][0]==sno):
                recno=i
                found=True
                break
        if(found):
            records[recno][1]=Validation(input("Enter New Name for updating its old Name:"))
            records[recno][2]=float(input("Enter New Marks for Updating its old Marks:"))
            with open("STU.data","wb") as fp:
                for record in records:
                    pickle.dump(record,fp)
                    print("Student Record Updated Successfully")
        else:
            print("Record Does Not Exist")
    except ValueError:
        print("Don't enter alnums,strs and symbols for sno,marks")
    except InvalidNameError:
        print("Invalid name----try Again")
    except ZeroLengthError:
        print("Try to enter ur Name")
    except SpaceNameError:
        print("Don't enter space for ur name---try again:")







