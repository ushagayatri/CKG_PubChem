import pandas as pd
from pandas import ExcelWriter
import os
import csv




with open("C:/Users/usha/PycharmProjects/PandasChem/input/folderA/outputA.csv","wb+") as op:
    # op.writelines("CID1,LID1,CID2,LID2,ST,CT,Rxx,Rxy,Rxz,Ryx,Ryy,Ryz,Rzx,Rzy,Rzz,Tx,Ty,Tz")

    p=os.getcwd()
    print p
    f=pd.read_csv(p+"/input/folderA/fileA.csv")

    # print f.head()
    # print f.index
    # print f.columns
    # print f.loc[0:221530,"ST":"CT"]
    rows= f["ST"].count()
    data= f.loc[1,"ST"]
    # print data
    print f["ST"].count()

    f2=f.loc[(f["ST"]>=90)]
    f2=f2.loc[(f2["CT"]>=90)]
    print f2
    # exwriter=pd.ExcelWriter("C:/Users/usha/PycharmProjects/PandasChem/input/folderA/outputA.xlsx")
    # f2.to_excel(exwriter,f2)
    # /f2.to_clipboard("C:/Users/usha/PycharmProjects/PandasChem/input/folderA/outputA.xlsx", excel=True,sep=None)
    f2.to_csv(op)
    # for row in xrange(rows):
    # # for row in range(67402,rows):
    #     print row
    #     dataST= f.loc[row,"ST"]
    #     dataCT=f.loc[row,"CT"]
    #     print dataCT , dataST
    #
    #     print dataFrame
    #
    #     # if int(dataST)<=90 or int(dataCT)<=90:
    #     #     print "Deleted row : ",row
    #     #     dataCID1=f.loc[row,"CID1"]
    #     #     op.writelines(dataCID1)
    #     #     # f.drop(row)
    #     #     # f.truncate(row)
    #
    #




# print data
