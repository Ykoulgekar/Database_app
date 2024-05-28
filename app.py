import mysql.connector
import streamlit as st
from flask import Flask,request,render_template,jsonify,redirect, url_for

app = Flask(__name__)

# established db connection
mydb ={
    'host':'localhost',
    'user':'root',
    'password':'Yogesh@6291',
    'database':'data'
}

# mycursor = mydb.cursor()
# print("Connection Established")

@app.route('/')
def home():
    return render_template('home.html')

# Inser rout
@app.route('/insert',methods =['POST'])
def insert():
    user_id =request.form['PersonID']
    Lastname =request.form['LastName']
    Firstname =request.form['FirstName']
    Address =request.form['Address']
    city =request.form['City']
    connector= mysql.connector.connect(**mydb)
    mycursor = connector.cursor()
    mycursor.execute("INSERT INTO Persons (PersonID,LastName,FirstName,Address, City) VALUES (%s, %s, %s, %s, %s)", (user_id, Lastname,Firstname,Address,city))
    connector.commit()
    mycursor.close()
    connector.close()
    return redirect(url_for('home'))

# update rout
@app.route('/update',methods =['POST'])
def update():
    user_id =request.form['PersonID']
    Lastname =request.form['LastName']
    Firstname =request.form['FirstName']
    Address =request.form['Address']
    city =request.form['City']
    connector= mysql.connector.connect(**mydb)
    mycursor = connector.cursor()
    mycursor.execute("UPDATE Persons SET LastName=%s,FirstName=%s,Address=%s, City=%s WHERE PersonID=%s",(Lastname,Firstname,Address,city,user_id))
    connector.commit()
    mycursor.close()
    connector.close()
    return redirect(url_for('home'))

# Read
@app.route('/read')
def read():
    # user_id =request.form['PersonsID']
    # Lastname =request.form['LastName']
    # Firstname =request.form['FirstName']
    # Address =request.form['Address']
    # city =request.form['City']
    connector= mysql.connector.connect(**mydb)
    mycursor = connector.cursor()
    mycursor.execute("SELECT * FROM Persons")
    users = mycursor.fetchall()
    connector.commit()
    mycursor.close()
    connector.close()
    return render_template("read.html",users=users)




if __name__=='__main__':
    app.run(debug=True)
