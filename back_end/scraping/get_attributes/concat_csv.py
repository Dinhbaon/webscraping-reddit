import pandas as pd

olddata = pd.read_csv("back_end/csvfiles/processeddata.csv", header= None, index_col=False)

newdata = pd.read_csv("back_end/csvfiles/newprocesseddata.csv", header = None, index_col=False)

combined_data = newdata.append(olddata)

print(combined_data)

combined_data.to_csv("back_end/csvfiles/processeddata.csv", header = None, index = False)