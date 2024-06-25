class Products:
    def __init__(self, id: int, name: str, description:str, price: float, category_id : str):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id 

    def __str__(self):
        return f'Product: {self.id}, {self.name}, {self.price}, {self.category_id}'

    def __repr__(self):
        return str(self)