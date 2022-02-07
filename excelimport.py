import pandas as pd

df = pd.read_excel(files)
#importing excel file with configuration
df = pd.read_excel(r"C:\Users\HP\PycharmProjects\Testing-tool\excel\configuration.xlsx")

#drop columns which were read as unnamed (empty in excel)
df.dropna(axis='rows',how='all', inplace=True)

#df(configuration) putted to the nested list every step represents one column
nlist = df.T.reset_index().values.tolist()

#delete NaNs from nested list
configuration = [[i for i in x if pd.notnull(i)] for x in nlist]

if __name__ == '__main__':
    pass




