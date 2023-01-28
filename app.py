import os
import pandas as pd

df_list = []
dirname='./data/'
def iterate_files():
    for file in os.listdir(dirname):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"):
            name = "./data/" + filename
            df_list.append(pd.read_csv(name,names=["Gamertag", "IP Address"]))
    final_df = df_list.usecols = [1]
    print(final_df)

# def get_gt():
#     just_gt = []
#     for item in range(len(df_list["Gamertag"])):
#         just_gt.append(df_list["Gamertag"])

# iterate_files()
# get_gt()
# print(just_gt)
   
iterate_files()

