from catalog_microservice.infra.database.repositories.products_repository import ProductRepository
from catalog_microservice.data.use_cases.product_get_stock import ProductGetStockUseCase
from catalog_microservice.presentation.controller.product_get_stock_controller import ProductGetStockController

def product_get_stock_composer():
    repositories = ProductRepository()
    use_case = ProductGetStockUseCase(repositories)
    controller = ProductGetStockController(use_case)