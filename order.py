
import mysql.connector
from mysql.connector import Error
import pandas as pd
def create_db_connection(host_name, user_name, user_password, database_name):
    connection=None
    try:
         connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=database_name
        )
         print("mysql database connection is successfull")     
    except Error as err:
        print(f"Error: '{err}'") 
    return connection    


#execut sql queries



def execute_queries(connection, queries):
    cursor = connection.cursor()
    try:
        cursor.execute(queries)
        connection.commit()
        print("Query was successfull")
    except Error as err:
        print(f"Error: '{err}'") 


    #create table

    create_table_order="""
    create table order(
    order_id int primary key,
    product_name varchar(20) not null, 
    cutomer_name varchar(30) not null,
    date_ordered date,
    quantity int,
    unit_price float,
    phone_number varchar(20)
    );   """ 

    #connect to database
    create_db_connection("localhost", "root", pw, db)
    execute_queries(connection,create_table_order )