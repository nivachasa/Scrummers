#Import lybrary flask and flask_mysqldb
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app= Flask(__name__)

##Mysql connection
#Current connection
app.config['MYSQL_HOST']= 'localhost' #Host = Localhost
app.config['MYSQL_USER']= 'root' #User = root
app.config['MYSQL_PASSWORD']= 'password' # Pasword = password
app.config['MYSQL_DB']= 'book_store' # Database name in mysql = book_store
mysql= MySQL(app)

#Session settings
app.secret_key='mysecretkey'

#Routes declarations
@app.route('/')
def comprobation():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT * FROM client') #It shows all clients data
    data_clients= cursor.fetchall() #Clients query result
    cursor.execute('SELECT * FROM book') #It shows all books data
    data_books= cursor.fetchall() #Books query result
    cursor.execute('SELECT client.client_id, client.client_lastname, book.book_id, book.book_name, book.book_gender, book.book_sold_date FROM client JOIN book ON client.client_id = book.fk_client_id ORDER BY client.client_id ;') #It shows relation between clients and books data
    data_relations= cursor.fetchall() #All relations query result
    #Redirect to main view and
    #Send query result to index template 
    return render_template('index.html', clients= data_clients, books= data_books, relations=data_relations)


@app.route('/add_client', methods=['POST'])
#Function to add new client
def add_client():
    if request.method=='POST':
        #Get the data from the form
        id = request.form['client_id']
        firstname = request.form['client_firstname']
        lastname = request.form['client_lastname']
        email = request.form['client_email']
        phone = request.form['client_phone']
        birthday = request.form['client_birthday']
        #Get the cursor
        cursor=mysql.connection.cursor()
        #Query execution
        cursor.execute(
            'insert into client (client_id, client_firstname, client_lastname, client_email, client_phone, client_birthday) values (%s, %s, %s, %s, %s, %s)',
            (id, firstname, lastname, email, phone, birthday)
        )
        #Update database
        mysql.connection.commit()
        #Announcement for final user
        flash('Client added successfully')
    #Redirect to main view
    return redirect(url_for('comprobation'))

@app.route('/delete_client/<string:id>')
#Function to delete client
def delete_client(id):
    #Get the cursor
    cursor=mysql.connection.cursor()
    #Query execution
    cursor.execute('DELETE FROM client WHERE client_id={0}'.format(id))
    #Update database
    mysql.connection.commit()
    #Announcement for final user
    flash('Client deleted successfully')
    #Redirect to main view
    return redirect(url_for('comprobation'))

@app.route('/get_client/<id>', methods =['POST', 'GET'])
#Function to get data of specific client
def get_client(id):
    #Get the cursor
    cursor=mysql.connection.cursor()
    #Query execution
    cursor.execute('SELECT * FROM client WHERE client_id = {0}'.format(id))
    data = cursor.fetchall() #Save query result
    #Update database
    mysql.connection.commit()
    #Announcement for final user
    flash('Client gotten successfully')
    #Redirect to edit_client template and send query result
    return render_template('edit_client.html', client = data[0])

@app.route('/edit_client/<id>', methods=['POST'])
#Function to edit a specific client
def edit_client(id):
    if request.method == 'POST':
        #Get the data from the form
        firstname = request.form['client_firstname']
        lastname = request.form['client_lastname']
        email = request.form['client_email']
        phone = request.form['client_phone']
        birthday = request.form['client_birthday']
        #Get the cursor
        cursor=mysql.connection.cursor()
        #Query execution
        cursor.execute("""
            UPDATE client 
                SET client_firstname = %s, 
                    client_lastname = %s, 
                    client_email = %s, 
                    client_phone = %s, 
                    client_birthday = %s 
                WHERE client_id = %s 
        """, (firstname, lastname, email, phone, birthday, id))
        #Update database
        mysql.connection.commit()
        #Announcement for final user
        flash('Client edited successfully')  
    #Redirect to main view
    return redirect(url_for('comprobation'))





@app.route('/add_book', methods=['POST'])
#Function to add new book and make the relation with client
def add_book():
    if request.method=='POST':
        #Get the data from the form
        id = request.form['book_id']
        name = request.form['book_name']
        gender = request.form['book_gender']
        sold_date = request.form['book_sold_date']
        client = request.form['book_fk_client_id']
        #Get the cursor
        cursor=mysql.connection.cursor()
        #Query execution
        cursor.execute(
            'INSERT INTO book (book_id, book_name, book_gender, book_sold_date, fk_client_id) VALUES (%s, %s, %s, %s, %s)',
            (id, name, gender, sold_date, client)
        )
        #Update database
        mysql.connection.commit() 
        #Announcement for final user
        flash('Book added successfully')
    #Redirect to main view
    return redirect(url_for('comprobation'))

@app.route('/get_book/<id>', methods =['POST', 'GET'])
#Function to get data of specific book
def get_book(id):
    #Get the cursor
    cursor=mysql.connection.cursor()
    #Query execution
    cursor.execute('SELECT * FROM book WHERE book_id = {0}'.format(id))
    data = cursor.fetchall() #Save query result
    #Update database
    mysql.connection.commit()
    #Announcement for final user
    flash('Book gotten successfully')
    #Redirect to edit_book template and send query result
    return render_template('edit_book.html', book = data[0])

@app.route('/edit_book/<id>', methods=['POST'])
##Function to edit a especific book
def edit_book(id):
    if request.method == 'POST':
        #Get the data from the form
        name = request.form['book_name']
        gender = request.form['book_gender']
        sold_date = request.form['book_sold_date']
        #Get the cursor
        cursor=mysql.connection.cursor()
        #Query execution
        cursor.execute("""
            UPDATE book 
                SET book_name = %s, 
                    book_gender = %s, 
                    book_sold_date = %s
                WHERE book_id = %s 
        """, (name,gender, sold_date,  id))
         #Update database
        mysql.connection.commit()
        #Announcement for final user
        flash('Book edited successfully')  
    #Redirect to main view
    return redirect(url_for('comprobation'))

#Main function
if __name__ == '__main__':
    #This app is running at localhost:3000
    app.run(port=3000, debug=True)