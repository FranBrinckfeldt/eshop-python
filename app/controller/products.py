from flask import abort
import mysql.connector
from ..config import get_connection
from ..models import ProductSchema

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

def get_all_products():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT p.id, p.name, p.description, p.price, p.id_category, c.name, c.description, p.id_brand, b.name, b.description, p.created_at, p.updated_at FROM products p LEFT JOIN brands b ON p.id_brand = b.id LEFT JOIN categories c ON p.id_category = c.id')
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        products = []
        for item in rows:
            category = dict(id=item[4], name=item[5], description=item[6])
            brand = dict(id=item[7], name=item[8], description=item[9])
            product = dict(
                id=item[0],
                name=item[1],
                description=item[2],
                price=item[3],
                created_at=item[10],
                updated_at=item[11],
                category=category,
                brand=brand
            )
            products.append(product)
        return products_schema.dump(products)
    except:
        cursor.close()
        connection.close()
        abort(500)

def get_product_by_id(id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT p.id, p.name, p.description, p.price, p.id_category, c.name, c.description, p.id_brand, b.name, b.description, p.created_at, p.updated_at FROM products p LEFT JOIN brands b ON p.id_brand = b.id LEFT JOIN categories c ON p.id_category = c.id WHERE p.id = %s', (id,))
        item = cursor.fetchone()
        cursor.close()
        connection.close()
        category = dict(id=item[4], name=item[5], description=item[6])
        brand = dict(id=item[7], name=item[8], description=item[9])
        product = dict(
            id=item[0],
            name=item[1],
            description=item[2],
            price=item[3],
            created_at=item[10],
            updated_at=item[11],
            category=category,
            brand=brand
        )
        return product_schema.dump(product)
    except:
        cursor.close()
        connection.close()
        abort(500)


def insert_product(product):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'INSERT INTO products (name, description, price, id_category, id_brand) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(stmt, (product['name'], product.get('description'), product['price'], product['category']['id'], product['brand']['id']))
        connection.commit()
        product['id'] = cursor.lastrowid
        response = {'message' : 'INSERTED', 'record' : product}, 201
        cursor.close()
        connection.close()
        return response
    except KeyError: 
        cursor.close()
        connection.close()
        abort(400)
    except mysql.connector.Error as err:
        cursor.close()
        connection.close()
        print(f'db_error : {err.msg}')
        if err.errno == 1452 or err.errno == 1366:
            abort(400)
        else: 
            abort(500)
    except: 
        cursor.close()
        connection.close()
        abort(500)

def delete_product(id):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'DELETE FROM products WHERE id = %s'
        cursor.execute(stmt, (id,))
        connection.commit()
        response = {'message' : 'DELETED', 'id' : id}, 200
        cursor.close()
        connection.close()
        return response
    except: 
        cursor.close()
        connection.close()
        abort(500)

def update_product(product, id):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'UPDATE products SET updated_at = CURRENT_TIMESTAMP, name = %s, description = %s, price = %s, id_category = %s, id_brand = %s WHERE id = %s'
        cursor.execute(stmt, (product['name'], product.get('description'), product['price'], product['category']['id'], product['brand']['id'], id))
        connection.commit()
        row_count = cursor.rowcount
        response = {'message' : 'UPDATED', 'rowAffected' : row_count}, 200
        cursor.close()
        connection.close()
        return response
    except mysql.connector.Error as err:
        cursor.close()
        connection.close()
        print(f'db_error : {err.msg}')
        if err.errno == 1452 or err.errno == 1366:
            abort(400)
        else: 
            abort(500)
    except Exception as err: 
        print(err)
        cursor.close()
        connection.close()
        abort(500)
