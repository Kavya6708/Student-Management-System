#StudentDelete.py<----------File Name and Module Name
import pickle
def deleterecord():
    try:
        with open("STU.data","rb") as rp:
            records=list()
            while(True):
                try:
                    record=pickle.load(rp)
                    records.append(record)
                except EOFError:
                       break
        sno=int(input("Enter Student Number to Remove the Record:"))
        found=False
        for record in records:
            if(record[0]==sno):
                found=True
                delrec=record
                break
        if(found):
            records.remove(delrec)
            print("Student Record Deleted Successfully")
            with open("STU.data","wb")as wp:
                for record in records:
                    pickle.dump(record,wp)
        else:
            print("Record Does Not Exist")
    except FileNotFoundError:
        print("File Not Found Exist")


