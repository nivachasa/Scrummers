#Reference database book_store
use book_store;

#Insert data into client table
insert into client (client_id, client_firstname, client_lastname, client_email, client_phone, client_birthday) 
	values 
		(52202010, 'Veronica', 'Sanchez', 'veronica@yahoo.es', '3144011210' , '1972-02-02'),
        (52202011, 'Valentina', 'Chacon', 'valentina@yahoo.es', '3144011211' , '1996-10-11'),
        (52202012, 'Cindy', 'Mendieta', 'cindy@yahoo.es', '3144011212' ,'1989-09-07'),
        (79616110, 'Ricardo', 'Gonzalez', 'ricardo@yahoo.es', '3144011213' , '1972-02-26'),
        (79616111, 'Daniel', 'Casas','daniel@yahoo.es', '3144011214' ,  '1995-10-25');


#Insert data into book table
insert into book (book_id, book_name, book_gender, book_sold_date, fk_client_id) 
	values 
		(1596, 'El beso de la mujer araña', 'fiction', '2020-02-15', 52202011),
        (1266, 'The notebook', 'Romance', '2020-02-15', 52202011),
        (1240, 'The notebook', 'Romance', '2020-10-11', 79616111),
        (1236, 'Ingenieria en produccion para principiantes', 'Academic','2020-05-01', 52202012),
        (1472, 'Barbie y el castillo flotante', 'Child', '2020-12-29', 79616110);