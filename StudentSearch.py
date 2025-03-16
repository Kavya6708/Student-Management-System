#StudentSearch
import pickle
def searchrecord():
    try:
        with open("STU.data","rb")as fp:
            records=[]
            while(True):
                try:
                    record=pickle.load(fp)
                    records.append(record)
                except EOFError:
                    break
        try:
                  sno=int(input("Enter Student Number to get other Details:"))
                  found=False
                  for record in records:
                      if(sno==record[0]):
                        found=True
                        break
                  if(found):
                     print("\tStudent Number:{}".format(record[0]))
                     print("\tStudent Name:{}".format(record[1]))
                     print("\tStudent Marks:{}".format(record[2]))
                  else:
                      print("student Record Does Not Exist")
        except ValueError:
            print("Don't enter alnums,strs and symbols for sno---try again")
    except FileNotFoundError:
        print("File Does Not Exist")




