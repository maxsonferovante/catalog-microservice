from catalog_microservice.infra.database.repositories.products_repository import ProductRepository
from catalog_microservice.data.use_cases.product_get_all import ProductGetAll as ProductGetAllUseCase
from catalog_microservice.presentation.controller.product_get_all_controller import ProductGetAllController


def product_get_all_composer():
    
    repository = ProductRepository()
    use_case = ProductGetAllUseCase(repository)
    controller = ProductGetAllController(use_case)
    
    return controller.handle