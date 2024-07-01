class ProductNotFoundError(Exception):
    def __init__(self, product_id: str):
        super().__init__(f'Product with id {product_id} not found.')