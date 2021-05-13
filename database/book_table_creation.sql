#STEP 3
#Reference database book_store
use book_store;

#Create table called book with all variables (PK and FK) with references to client 
create table book (
	book_id int not null,
    book_name varchar(50),
    book_gender varchar(25),
    book_sold_date date,
    fk_client_id int,
    primary key (book_id),
    foreign key (fk_client_id) references client(client_id)
    );