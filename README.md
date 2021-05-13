# Technical test to Scrumers

## Table of content
1. Project description
2. Requirements
3. Setup

## 1. Project description
Visualize and manipulate the sold books data in a Book Store. Where there are multiple books and multiple clients but each of the books has a unique id to identify it. Each of these books is a copy, that means it could be several copies of the same book with different and unique ids. All the books in this dataset have been sold, that means all of them have a buyer. 

• Create a MySQL DataBase with 2 tables 
• Create a simple web interface to access to the data base 
• Make online data manipulation 

## 2. Requirements
1. Python 3.9.5
2. pip install flask
3. pip install flask-mysqldb
4. mySQL

## 3. Setup
1. Clone this repo 
2. Execute [database/book_store_database_creation.sql](database/book_store_database_creation.sql) for the data base creation
3. Execute [database/client_table_creation.sql](database/client_table_creation.sql) for the client table creation
4. Execute [database/book_table_creation.sql](database/book_table_creation.sql) for the book table creation
5. Execute [database/data_insertion_creation.sql](database/data_insertion.sql) for the data insertion
7. Open [data_manipulation_web/app.py]data_manipulation_web/(app.py) and set up ap.py in the section:
            ##Mysql connection
            #Current connection
    With your current host, user and password
6. Execute [data_manipulation_web/app.py](data_manipulation_web/app.py) for the client table creation
7. Open the navigation tab and type localhost:3000
8. Manipulate the book store data


Credits to Scrummers technical test and Fazt Code