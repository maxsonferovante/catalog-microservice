from typing import Dict

from catalog_microservice.domain.use_cases.product_finder_interface import ProductFinderInterface
from catalog_microservice.data.interfaces.product_repository_interface import ProductRepositoryInterface


class ProductFinder(ProductFinderInterface):
    def __init__(self, product_repository: ProductRepositoryInterface):
        self.product_repository = product_repository

    def find(self, product_id: int) -> Dict:
        return self.product_repository.select_product(product_id)