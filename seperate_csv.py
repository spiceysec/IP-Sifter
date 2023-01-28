##### IMPORT GAMERTAGS TO A CSV FILE #####

# import pandas as pd
# data_import = pd.read_csv('./data/data.csv', usecols = [1],index_col=False)
# print(data_import.to_string())
# data_import.to_csv("gamertags.csv", index=False)

##### IMPORT IPS TO A CSV FILE #####

# import pandas as pd
# data_import = pd.read_csv('./data/data.csv', usecols = [0],index_col=False)
# print(data_import.to_string())
# data_import.to_csv("ips.csv", index=False)


##### INSERT GAMERTAGS INTO DATABASE #####

import csv
import os
import pymysql
from dotenv import load_dotenv
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
connection = pymysql.connect(
    host,
    user,
    password,
    database
)
cursor = connection.cursor()

#### open files and store as vairbles
with open('gamertags.csv', 'r') as file1:
    reader = csv.reader(file1)
    names = [row[0] for row in reader]
    
with open('ips.csv', 'r') as file2:
    reader = csv.reader(file2)
    ip_addr = [row[0] for row in reader] 
    
for name, ip_addr in zip(names, ip_addr):
    cursor.execute("INSERT INTO Yutes (gamertag, ip) VALUES (%s, %s)", (name,ip_addr))
    connection.commit()
print('done!')