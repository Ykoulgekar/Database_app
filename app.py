import mysql.connector
import streamlit as st
from flask import Flask,request,render_template,jsonify,redirect, url_for

app = Flask(__name__)

# established db connection
mydb =mysql.connector.connect(
    host='localhost',
    user='root',
    password='Yogesh@6291',
    database='data'
)

mycursor = mydb.cursor()
print("Connection Established")

@app.route('/')
def home():
    return render_template('home.html')

# # Inser rout
# @app.route('/insert',methods =['POST'])
# def insert():
#     user_id =request.form['PersonsID']
#     Lastname =request.form['LastName']
#     Firstname =request.form['FirstName']
#     Address =request.form['Address']
#     city =request.form['City']
#     mycursor.execute("INSERT INTO Persons (PersonsID,LastName,FirstName,Address, City) VALUES (%s, %s, %s, %s, %s)", (user_id, Lastname,Firstname,Address,city))
#     mydb.commit()
#     mycursor.close()
#     mydb.close()
#     return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)
