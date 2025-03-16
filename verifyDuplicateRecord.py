import pickle
def verify(sno):
    with open("STU.data","rb") as fp:
        snos=list()
        while(True):
            try:
                record=pickle.load(fp)
                snos.append(record[0])
            except EOFError:
                break
            if sno in snos:
                return True
            else:
               return False
