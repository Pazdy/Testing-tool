import pandas as pd

#importing excel file with configuration
df = pd.read_excel(r"C:\Users\HP\PycharmProjects\Testing-tool\excel\configuration.xlsx")

# df(configuration) putted to the nested list every step represents one column
nlist = df.T.reset_index().values.tolist()

#delete NaNs from nested list
configuration = [[i for i in x if pd.notnull(i)] for x in nlist]


