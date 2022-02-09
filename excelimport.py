from typing import List, Any
import pandas as pd
import funcionaltesting
def e_import(file):
    df = pd.read_excel(file)
    #importing excel file with configuration
    #df = pd.read_excel(r"C:\Users\HP\PycharmProjects\Testing-tool\excel\configuration.xlsx")

    #drop columns which were read as unnamed (empty in excel)
    df.dropna(axis='rows',how='all', inplace=True)

    #df(configuration) putted to the nested list every step represents one column
    nlist = df.T.reset_index().values.tolist()

    #delete NaNs from nested list
    e_import.configuration = [[i for i in x if pd.notnull(i)] for x in nlist]
#    funcionaltesting.Testcases().test_excecutions(configuration=configuration)


if __name__ == '__main__':
    pass




