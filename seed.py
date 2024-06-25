from faker import Faker
from faker_commerce import Provider as CommerceProvider
from datetime import datetime

from catalog_microservice.infra.utils.generate_uuid import generate_uuid
from catalog_microservice.infra.database.settings.connection import DBConnectionHandler 
from catalog_microservice.infra.database.entities.categorys import Categories
from catalog_microservice.infra.database.entities.products import Products

class SeedCatalog:
    def __init__(self) -> None:
        self.__faker = Faker()
        self.__faker.add_provider(CommerceProvider)
        self.__connection = DBConnectionHandler()
        self.__categories = []
        self.__products = []
    
    def __enter__(self):
        self.__connection.__enter__()
        self.__connection.session.query(Products).delete()
        self.__connection.session.query(Categories).delete()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__connection.__exit__(exc_type, exc_val, exc_tb)
        
    def create_category(self, amount: int):       
        for _ in range(amount):
            self.__categories.append(
                Categories(
                    id = generate_uuid(),
                    name = self.__faker.ecommerce_category(),
                    description = self.__faker.catch_phrase(),
                    created_at = datetime.now(),
                    updated_at = datetime.now()
                )
            )
    def create_product(self, amount: int):
        for _ in range(amount):
            self.__products.append(
                Products(
                    id = generate_uuid(),
                    name = self.__faker.ecommerce_name(),
                    description = self.__faker.catch_phrase(),
                    price = self.__faker.random_number(2),
                    category_id = self.__faker.random_element(self.__categories).id,
                    created_at = datetime.now(),
                    updated_at = datetime.now()
                )
            )
    def seed_all(self, amount_categories: int, amount_products: int):
        self.create_category(amount_categories)
        self.create_product(amount_products)
        
        self.__connection.session.add_all(self.__categories)
        self.__connection.session.add_all(self.__products)
        self.__connection.session.commit()
        
        print('Data seeded successfully!')
        
        
if __name__ == '__main__':
    with SeedCatalog() as seed:
        seed.seed_all(10, 50)
