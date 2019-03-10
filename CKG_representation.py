import pandas as pd
import os


path="C:/Users/usha/Desktop/JingSS/pubchem/"
with open("C:/Users/usha/Desktop/JingSS/pubchem/op/opTextA.txt","wb+") as op:
    p=os.getcwd()
    # print p
    textStr=""
    listFile = os.listdir("C:/Users/usha/Desktop/JingSS/pubchem/ip/")
    for f in listFile:
        # print os.path.join(path, f)
        f= pd.read_csv("C:/Users/usha/Desktop/JingSS/pubchem/ip/"+f)
        rows=f["ST"].count()
        # print rows
        # print f["CID1"]


        for x in range(rows):
            # print x
            # x=x+1
            textStr="pc:compound?id="+str(f.iloc[x,0])+" &pc:lid="+str(f.iloc[x,1])+" pc:has_3D_similarity?ds=pcneighbour&id="+str(x)+" &pc:has_ST_score="+str(f.iloc[x,4])+" &pc:has_CT_score="+str(f.iloc[x,5])+" Pc:compund?id="+str(f.iloc[x,2])+" &pc:lid="+str(f.iloc[x,3])
            print "\n"
            print textStr
            op.write(textStr)
            op.write("\n")

