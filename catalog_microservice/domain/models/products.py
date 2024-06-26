class Products:
    def __init__(self, id: int, name: str, description:str, price: float, stock:int ,category_id : str):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category_id = category_id 

    def __str__(self):
        return f'Product(id={self.id}, name={self.name}, description={self.description}, price={self.price}, stock={self.stock}, category_id={self.category_id})'

    def __repr__(self):
        return str(self)