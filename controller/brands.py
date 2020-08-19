#TODO: Actualizar get_product_by_id.

from config.database import get_connection
from models.BrandSchema import BrandSchema
from flask import abort

brand_schema = BrandSchema()
brands_schema = BrandSchema(many=True)

def get_all_brands():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, description, created_at, updated_at FROM brands')
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    brands = []
    for item in rows:
        brands.append(
            dict(
                id=item[0],
                name=item[1],
                description=item[2],
                created_at=item[3],
                updated_at=item[4]
            )
        )
    return brands_schema.dump(brands)

def get_brand_by_id(id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, description, created_at, updated_at FROM brands WHERE id = %s', (id,))
    item = cursor.fetchone()
    cursor.close()
    connection.close()
    brand = dict(
                id=item[0],
                name=item[1],
                description=item[2],
                created_at=item[3],
                updated_at=item[4]
            )
    return brand_schema.dump(brand)

def insert_brand(brand):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'INSERT INTO brands (name, description) VALUES (%s, %s)'
        cursor.execute(stmt, (brand['name'], brand['description']))
        connection.commit()
        brand['id'] = cursor.lastrowid
        response = {'message' : 'INSERTED', 'record' : brand}, 201
        cursor.close()
        connection.close()
        return response
    except: 
        cursor.close()
        connection.close()
        abort(500)

def delete_brand(id):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'DELETE FROM brands WHERE id = %s'
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

def update_brand(brand, id):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'UPDATE brands SET updated_at = CURRENT_TIMESTAMP, name = %s, description = %s  WHERE id = %s'
        cursor.execute(stmt, (brand['name'], brand['description'], id))
        connection.commit()
        row_count = cursor.rowcount
        response = {'message' : 'UPDATED', 'rowAffected' : row_count}, 200
        cursor.close()
        connection.close()
        return response
    except: 
        cursor.close()
        connection.close()
        abort(500)