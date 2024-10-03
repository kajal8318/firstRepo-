#import libreries
import mysql.connector
from mysql.connector import Error
import pandas as pd
def create_server_connection(hostname,username, userpassword):
    connection=None
    try:
        connection=mysql.connector.connect()
        host=hostname
        name=username
        password=userpassword
        print("database server is connected") 
    except Error as err:
        print(f"Error ,'{err}'")
        return connection
    
    #put password to your server
pw="k@j@l123"
    
    #database name 
db="my_python"

connection=create_server_connection("localhost","root",pw)

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

# Create a new database
create_database_query = "CREATE DATABASE IF NOT EXISTS my_python"
create_database(connection, create_database_query)




#create mysql python

# def create_database(connection, query):
#     if connection is not None:
#        cursor=connection.cursor()
#     try:
#         cursor.execute(query)
#         print("database created successfully")
#     except Error as err:
#        print(f"Error ,'{err}'") 
#     else:
#         print("Connection failed. Cannot create database.")   
# create_database_query="create database mysql_python"
# create_database(connection,create_database_query)    
   