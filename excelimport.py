import pandas as pd

#importing CSV file with configuration
df = pd.read_excel(r"C:\Users\HP\PycharmProjects\Testing-tool\excel\configuration.xlsx")

#list that store actions like URL, button ... putted in csv
actions = []

#list that store arguments for actions like specific URL, button on page putted in csv
arguments = []

#get actions from df
for column in df.columns:
    actions.append(column)

#get arguments for actions from df
for row in df.iloc[0]:
    arguments.append(row)

#create dict for arguments and actions
actarg = {}

#2 lists into dict -> dict key: actions ; values: arguments
for i in range(len(actions)):
    actarg[actions[i]] = arguments[i]