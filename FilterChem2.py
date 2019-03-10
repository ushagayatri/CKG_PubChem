import pandas as pd
import os

with open("C:/Users/usha/PycharmProjects/PandasChem/input/folderC/outputC.csv","wb+") as op:
    p=os.getcwd()
    booleans  =[]
    f=pd.read_csv(p+"/input/folderC/fileC.csv")
    rows=f["ST"].count()
    for row in xrange(rows):
        if ((f.loc[row,"ST"]>=90) or (f.loc[row,"CT"])>=90):
            booleans.append(True)
        else:
            booleans.append(False)

    is_long=pd.Series(booleans)
    is_long.head()
    f[is_long].to_csv(op,index=False)


