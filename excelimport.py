import pandas as pd


def e_import(file):
    # importing excel file with configuration
    df = pd.read_excel(file)

    # drop columns which were read as unnamed (empty in excel)
    df.dropna(axis='rows', how='all', inplace=True)

    # df(configuration) put to the nested list every step represents one column
    nlist = df.T.reset_index().values.tolist()

    # delete NaNs from nested list
    e_import.configuration = [[i for i in x if pd.notnull(i)] for x in nlist]
