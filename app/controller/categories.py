#TODO: Error Handling

from flask import abort
from ..config import get_connection
from ..models import CategorySchema

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

def get_all_categories():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, description, created_at, updated_at FROM categories')
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    categories = []
    for item in rows:
        categories.append(
            dict(
                id=item[0],
                name=item[1],
                description=item[2],
                created_at=item[3],
                updated_at=item[4]
            )
        )
    return categories_schema.dump(categories)

def get_category_by_id(id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, description, created_at, updated_at FROM categories WHERE id = %s', (id,))
    item = cursor.fetchone()
    cursor.close()
    connection.close()
    category = dict(
                id=item[0],
                name=item[1],
                description=item[2],
                created_at=item[3],
                updated_at=item[4]
            )
    return category_schema.dump(category)

def insert_category(category):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'INSERT INTO categories (name, description) VALUES (%s, %s)'
        cursor.execute(stmt, (category['name'], category['description']))
        connection.commit()
        category['id'] = cursor.lastrowid
        response = {'message' : 'INSERTED', 'record' : category}, 201
        cursor.close()
        connection.close()
        return response
    except: 
        cursor.close()
        connection.close()
        abort(500)

def delete_category(id):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'DELETE FROM categories WHERE id = %s'
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

def update_category(category, id):
    try:
        connection = get_connection()
        cursor = connection.cursor(prepared=True)
        stmt = 'UPDATE categories SET updated_at = CURRENT_TIMESTAMP, name = %s, description = %s  WHERE id = %s'
        cursor.execute(stmt, (category['name'], category['description'], id))
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