class Product:
    def __init__ (self, name, description, price, id_category, id_brand):
        self.name = name
        self.description = description
        self.price = price
        self.id_category = id_category
        self.id_brand = id_brand

    def with_id (self, id):
        self.id = id
        return self    

    def with_timestamps (self, created_at, updated_at):
        self.created_at = created_at
        self.updated_at = updated_at
        return self

    def serialize (self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'id_category': self.id_category,
            'id_brand': self.id_brand,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }