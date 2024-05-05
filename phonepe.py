# !pip install streamlit
# !pip install mysql.ConnectionRefusedError
# !pip install plotly
# !pip install os
# !pip install gitpython
# !pip install pymysql

import os
import json
from PIL import Image
import pandas as pd
import mysql.connector
import streamlit as st
import plotly.express as px

#cloning the data from github
#os.environ['GIT_PYTHON_REFRESH'] = 'quiet'
#import git
#from git.repo.base import Repo

# Step 1: Data cloning

# Check if the 'pulse' directory exists
if not os.path.exists('pulse'):
# Clone the repository if it doesn't exist
        os.system('git clone https://github.com/PhonePe/pulse.git')
else:
        print ('Repository "pulse" already exists. Skipping cloning process.')
#******************************************************************************************************************* 
#  Dataframe of agreegated transactions

path1 = 'C:/Users/premi/Desktop/Premila/projects/Phonepe/pulse/data/aggregated/transaction/country/india/state/'
agg_trans_list = os.listdir(path1)

clm1 = {'State':[], 'Year':[], 'Quarter':[],'Transaction_type':[],'Transaction_count':[], 'Transaction_amount':[]}

for state in agg_trans_list:
        state_path = path1 + state + '/'
        agg_year_list = os.listdir(state_path)

        for year in agg_year_list:
            year_path = state_path + year + '/'
            agg_file_list = os.listdir(year_path)

            for file in agg_file_list:
                curr_file = year_path + file
                
                data =  open(curr_file, 'r')
                A = json.load(data)
                

                for i in A['data']['transactionData']:
                        name = i['name']
                        
                        count = i['paymentInstruments'][0]['count']
                        amount = i['paymentInstruments'][0]['amount']
                        type1 = i['paymentInstruments'][0]['type']
                        
                        clm1['State'].append(state)
                        clm1['Year'].append(year)
                        clm1['Quarter'].append(int(file.strip('.json')))
                        
                        clm1['Transaction_type'].append(type1)
                        clm1['Transaction_count'].append(count)
                        clm1['Transaction_amount'].append(amount)

df_agg_trans =  pd.DataFrame(clm1)
print ("1. Aggregate transactions")
print(df_agg_trans)

# ********************************************************************************
# data frame of aggregated user

path2 = 'C:/Users/premi/Desktop/Premila/projects/Phonepe/pulse/data/aggregated/user/country/india/state/'

agg_user_list = os.listdir(path2)

clm2 = {'State': [], 'Year': [], 'Quarter': [], 'Brands': [], 'Count': [],
            'Percentage': []}
for state in agg_user_list:
    state_path = path2 + state + "/"
    agg_year_list = os.listdir(state_path)
    
    for year in agg_year_list:
        year_path = state_path + year + "/"
        agg_file_list = os.listdir(year_path)

        for file in agg_file_list:
            cur_file = year_path + file
            data = open(cur_file, 'r')
            B = json.load(data)

            try:
                for i in B["data"]["usersByDevice"]:
                    brand_name = i["brand"]
                    counts = i["count"]
                    percents = i["percentage"]
                    clm2["Brands"].append(brand_name)
                    clm2["Count"].append(counts)
                    clm2["Percentage"].append(percents)
                    clm2["State"].append(state)
                    clm2["Year"].append(year)
                    clm2["Quarter"].append(int(file.strip('.json')))
            except:
                pass
df_agg_user = pd.DataFrame(clm2)
print("2.Aggregated users")
print(df_agg_user)


# *****************************************************************************
# Data frame of map transactions

path3 = 'C:/Users/premi/Desktop/Premila/projects/Phonepe/pulse/data/map/transaction/hover/country/india/state/'
map_trans_list = os.listdir(path3)

clm3 = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Count': [],
            'Amount': []}

for state in map_trans_list:
    state_path = path3 + state + '/'
    map_year_list = os.listdir(state_path)
    
    for year in map_year_list:
        year_path = state_path + year + '/'
        map_file_list = os.listdir(year_path)
        
        for file in map_file_list:
            cur_file = year_path + file
            
            data = open(cur_file, 'r')
            C = json.load(data)
            
            for i in C['data']['hoverDataList']:
                district = i['name']
                count = i['metric'][0]['count']
                amount = i['metric'][0]['amount']
                clm3['District'].append(district)
                clm3['Count'].append(count)
                clm3['Amount'].append(amount)
                clm3['State'].append(state)
                clm3['Year'].append(year)
                clm3['Quarter'].append(int(file.strip('.json')))
                
df_map_trans = pd.DataFrame(clm3)
print("3.Map transaction")
print(df_map_trans)

# *****************************************************************************
# Data frame of map user

path4 = "C:/Users/premi/Desktop/Premila/projects/Phonepe/pulse/data/map/user/hover/country/india/state/"
map_user_list = os.listdir(path4)


clm4 = {
    "State": [],
    "Year": [],
    "Quarter": [],
    "District": [],
    "RegisteredUser": [],
    "AppOpens": []
}

# Iterate over directories in the path
for state in map_user_list:
    state_path = path4 + state + '/'
    map_year_list = os.listdir(state_path)
    
    for year in map_year_list:
        year_path = state_path + year + '/'
        map_file_list = os.listdir(year_path)
        
        for file in map_file_list:
            cur_file = year_path + file
            print(f"Processing file: {cur_file}")
            
            data =  open(cur_file, 'r')
            D = json.load(data)
            
            for i in D["data"]["hoverData"].items():
                        district = i[0]
                        registereduser = i[1]["registeredUsers"]
                        appOpens = i[1]['appOpens']
                        clm4["District"].append(district)
                        clm4["RegisteredUser"].append(registereduser)
                        clm4["AppOpens"].append(appOpens)
                        clm4['State'].append(state)
                        clm4['Year'].append(year)
                        clm4['Quarter'].append(int(file.strip('.json')))
                
df_map_user = pd.DataFrame(clm4)

print("4.Map users")
print(df_map_user)

# ****************************************************************************

# Data frame of top transactions
path5 = "C:/Users/premi/Desktop/Premila/projects/Phonepe/pulse/data/top/transaction/country/india/state/"

top_trans_list = os.listdir(path5)
clm5 = {'State': [], 'Year': [], 'Quarter': [], 'Pincode': [], 'Transaction_count': [],
            'Transaction_amount': []}

for state in top_trans_list:
    state_path = path5 + state + "/"
    top_year_list = os.listdir(state_path)
    
    for year in top_year_list:
        year_path = state_path + year + "/"
        top_file_list = os.listdir(year_path)
        
        for file in top_file_list:
            cur_file = year_path + file
            data = open(cur_file, 'r')
            E = json.load(data)
            
            for i in E['data']['pincodes']:
                name = i['entityName']
                count = i['metric']['count']
                amount = i['metric']['amount']
                clm5['Pincode'].append(name)
                clm5['Transaction_count'].append(count)
                clm5['Transaction_amount'].append(amount)
                clm5['State'].append(state)
                clm5['Year'].append(year)
                clm5['Quarter'].append(int(file.strip('.json')))
df_top_trans = pd.DataFrame(clm5)
print("5.Top transaction")
print(df_top_trans)

# ********************************************************************************************

# Data frame of top users
path6 = "C:/Users/premi/Desktop/Premila/projects/Phonepe/pulse/data/top/user/country/india/state/"
top_user_list = os.listdir(path6)
clm6 = {'State': [], 'Year': [], 'Quarter': [], 'Pincode': [],
            'RegisteredUsers': []}

for state in top_user_list:
    state_path = path6 + state + "/"
    top_year_list = os.listdir(state_path)
    
    for year in top_year_list:
        year_path = state_path + year + "/"
        top_file_list = os.listdir(year_path)
        
        for file in top_file_list:
            cur_file = year_path + file
            data = open(cur_file, 'r')
            F = json.load(data)
            
            for i in F['data']['pincodes']:
                name = i['name']
                registeredUsers = i['registeredUsers']
                clm6['Pincode'].append(name)
                clm6['RegisteredUsers'].append(registeredUsers)
                clm6['State'].append(state)
                clm6['Year'].append(year)
                clm6['Quarter'].append(int(file.strip('.json')))
df_top_user = pd.DataFrame(clm6)
print("6.Top User")
print(df_top_user)

# *************************************************************************
# converting files to csv files

df_agg_trans.to_csv('agg_trans.csv',index=False)
df_agg_user.to_csv('agg_user.csv',index=False)
df_map_trans.to_csv('map_trans.csv',index=False)
df_map_user.to_csv('map_user.csv',index=False)
df_top_trans.to_csv('top_trans.csv',index=False)
df_top_user.to_csv('top_user.csv',index=False)

# ************************************************************************
# Creating connection with MySQL
# Connecting with SQL

myconn =mysql.connector.connect(
        host ='localhost',
        user =  'root',
        password= 'Jesus@2525',
        database='youtube'
        )
cursor = myconn.cursor()
mycursor = myconn.cursor(buffered=True)

# Creating new database and tables

mycursor.execute("CREATE DATABASE Phonepe")
mycursor.execute("USE Phonepe")

# Creating agg_trans table

mycursor.execute("create table agg_trans (State varchar(100), Year int, Quarter int, Transaction_type varchar(100), Transaction_count int, Transaction_amount double)")

for i,row in df_agg_trans.iterrows():
   
    sql = "INSERT INTO agg_trans VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
   
    myconn.commit()

# Creating agg_user table

mycursor.execute("create table agg_user (State varchar(100), Year int, Quarter int, Brands varchar(100), Count int, Percentage double)")

for i,row in df_agg_user.iterrows():
    sql = "INSERT INTO agg_user VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    myconn.commit()


# Creating map_trans table

mycursor.execute("create table map_trans (State varchar(100), Year int, Quarter int, District varchar(100), Count int, Amount double)")

for i,row in df_map_trans.iterrows():
    sql = "INSERT INTO map_trans VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    myconn.commit()

# Creating map_user table

mycursor.execute("create table map_user (State varchar(100), Year int, Quarter int, District varchar(100), Registered_user int, App_opens int)")

for i,row in df_map_user.iterrows():
    sql = "INSERT INTO map_user VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    myconn.commit()

# Creating top_trans table

mycursor.execute("create table top_trans (State varchar(100), Year int, Quarter int, Pincode int, Transaction_count int, Transaction_amount double)")

for i,row in df_top_trans.iterrows():
    sql = "INSERT INTO top_trans VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    myconn.commit()

# Creating top_user table

mycursor.execute("create table top_user (State varchar(100), Year int, Quarter int, Pincode int, Registered_users int)")

for i,row in df_top_user.iterrows():
    sql = "INSERT INTO top_user VALUES (%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    myconn.commit()

# List of tables

mycursor.execute("show tables")
mycursor.fetchall()
[('agg_trans',),
 ('agg_user',),
 ('map_trans',),
 ('map_user',),
 ('top_trans',),
 ('top_user',)]
 