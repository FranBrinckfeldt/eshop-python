from config.database import get_connection
from models.CustomerSchema import CustomerSchema
from flask import abort
import mysql.connector
import bcrypt

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