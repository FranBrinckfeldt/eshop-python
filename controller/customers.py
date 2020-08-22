from config.database import get_connection
from models.CustomerSchema import CustomerSchema
from flask import abort
import mysql.connector
import bcrypt
from utils import generate_token

def customer_register(customer):
    try:
        CustomerSchema().load(customer)
        hashed_password = bcrypt.hashpw(customer['password'].encode('utf-8'), bcrypt.gensalt())
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'INSERT INTO customers (email, password, firstname, lastname, birth) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(stmt, (
            customer['email'], 
            hashed_password.decode('utf-8'), 
            customer['firstname'], 
            customer['lastname'], 
            customer['birth']))
        connection.commit()
        customer['id'] = cursor.lastrowid
        customer['password'] = hashed_password.decode('utf-8')
        response = {'message' : 'REGISTERED', 'record' : customer}, 201
        cursor.close()
        connection.close()
        return response
    except:
        cursor.close()
        connection.close()
        abort(500)

def customer_login(email, password):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        stmt = 'SELECT id, email, password, active FROM customers WHERE email = %s'
        cursor.execute(stmt, (email,))
        row = cursor.fetchone()
        if row is None:
            abort(403)
        is_valid = bcrypt.checkpw(password.encode('utf-8'), row[2].encode('utf-8'))
        if is_valid:
            token = generate_token({'email' : email,'sub' : row[0], 'active' : row[3]})
        else: 
            abort(403)
        cursor.close()
        connection.close()
        return {'accessToken' : token.decode('utf-8')}
    except:
        cursor.close()
        connection.close()
        abort(500)