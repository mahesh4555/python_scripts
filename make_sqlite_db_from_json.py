
import sqlite3
import json

from sqlite3 import Error


import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

def sql_insert_into_table(con, json_string, table_name):

    data=[]
    data.append(json_string)
   
    cursorObj = con.cursor()
    mytable ="mytable"
    query = "INSERT INTO "+ mytable + " (key) VALUES(?)"
    #INSERT INTO mytable (key) VALUES(?)
    print(query)
   
    cursorObj.execute(query,data)
    con.commit()
    print("values commited")


def sql_connection():
    try:
        con = sqlite3.connect('mydatabase1.db')
        return con
    except Error:
        print(Error)

def sql_create_table(con,db_name):
    cursorObj = con.cursor()
    query="CREATE TABLE IF NOT EXISTS " + db_name + "( key text );"
    cursorObj.execute(query)
    print("created table")


def read_json_file(device_param):
        f = open(device_param)
        readings = json.load(f)
        print(type(readings))
        f.close()
        print("current readings ")
        print(readings)
        return readings
        

#json_file_name="new.json"
json_file_name=sys.argv[1]
#create db-name from json file name
list=json_file_name.split('.')
db_name=list[0]
print("db_name : ",db_name)
table_name="mytable"

#read json and convert it to string
readings=read_json_file(json_
file_name)
print(type(readings))

json_string= json.dumps(readings)
print(type(json_string))

#create sql conn
print("sql conn")
con = sql_connection()

#create sql table
sql_create_table(con,table_name)

print("sql_insert_into_table")
sql_insert_into_table(con,json_string,table_name )



    © 2020 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help


