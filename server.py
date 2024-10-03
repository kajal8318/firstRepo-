import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(hostname, username, userpassword):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=userpassword
        )
        if connection.is_connected():
            print("Database server is connected")
        else:
            print("Failed to connect to the database server")
    except Error as err:
        print(f"Error: '{err}'")
        return None
    return connection

def create_database(connection, query):
    if connection is None:
        print("Connection failed. Cannot create database.")
        return
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

# Your password
pw = "k@j@l123"  
db = "my_python"  # Database name

# Create server connection
connection = create_server_connection("localhost", "root", pw)

# Define the query to create the database
create_database_query = "CREATE DATABASE IF NOT EXISTS my_python"

# Check the connection and create the database
if connection:
    create_database(connection, create_database_query)


#connect to database

# def create_db_connection(host_name, user_name, user_password, database_name):
#     connection=None
#     try:
#          connection = mysql.connector.connect(
#             host=host_name,
#             user=user_name,
#             password=user_password,
#             database=database_name
#         )
#          print("mysql database connection is successfull")     
#     except Error as err:
#         print(f"Error: '{err}'") 
#     return connection    


# #execut sql queries



# def execute_queries(connection, queries):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(queries)
#         connection.commit()
#         print("Query was successfull")
#     except Error as err:
#         print(f"Error: '{err}'") 


#     #create table

#     create_table_order="""
#     create table order(
#     order_id int primary key,
#     product_name varchar(20) not null, 
#     cutomer_name varchar(30) not null,
#     date_ordered date,
#     quantity int,
#     unit_price float,
#     phone_number varchar(20)
#     );   """ 

#     #connect to database
#     create_db_connection("localhost", "root", pw, db)
#     execute_queries(connection,create_table_order )
import mysql.connector
from mysql.connector import Error

# Create database connection
def create_db_connection(host_name, user_name, user_password, database_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=database_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

# Execute SQL queries
def execute_queries(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query was successful")
    except Error as err:
        print(f"Error: '{err}'")

# SQL query to create table
# create_table_order = """
# CREATE TABLE orders (
#     order_id INT PRIMARY KEY,
#     product_name VARCHAR(20) NOT NULL, 
#     customer_name VARCHAR(30) NOT NULL,
#     date_ordered DATE,
#     quantity INT,
#     unit_price FLOAT,
#     phone_number VARCHAR(20)
# );   
# """

# # Connect to the database and execute the query
# pw = "k@j@l123"  # Your MySQL password
# db = "my_python"  # Your MySQL database

# connection = create_db_connection("localhost", "root", pw, db)
# if connection:
#     execute_queries(connection, create_table_order)

#insert into table order

# data_insert="""
# insert into orders values
# ( 101, "laptop", "parul", "2024-06-14", 1, 36000, 9517691854),
# ( 102, "earing", "kajal", "2023-06-16", 4, 400, 9519347295),
# ( 103, "shirt", "shalu", "2022-04-12", 2, 5000, 3857395944),
# ( 104, "cargo", "saloni", "2020-06-14", 1, 6000, 9546691854),
# ( 105, "kurta", "pallavee", "2018-10-04", 5, 6500, 8318678755);
# """
# connection = create_db_connection("localhost", "root", pw, db)
# execute_queries(connection,data_insert )

#read query and display the result

def read_query(connection, query):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

# q1="""
# select *from orders"""        
# connection = create_db_connection("localhost", "root", pw, db)
# results=read_query(connection, q1)
# for result in results:
#     print(result)


q2="""
select customer_name ,order_id, product_name from orders"""        
connection = create_db_connection("localhost", "root", pw, db)
results=read_query(connection, q2)
for result in results:
    print(result)