#STEP 2
#Reference database book_store
use book_store;

#Create table called client with all variables (PK) 
create table client (
	client_id int not null,
    client_firstname varchar(25),
    client_lastname varchar(25),
    client_email varchar(50),
    client_phone varchar(50),
    client_birthday date,
    primary key (client_id)
    );