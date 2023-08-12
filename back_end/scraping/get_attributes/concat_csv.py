import pandas as pd 

newdata = pd.read_csv('../csvfiles/newprocesseddata.csv', header = None, index_col=False)

olddata = pd.read_csv('../csvfiles/processeddata.csv', header = None, index_col=False)

concatdata = newdata.append(olddata)


newdata.to_csv('../csvfiles/processeddata.csv', header=None)



