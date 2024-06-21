from catalog_microservice.infra.database.repositories.products_repository import ProductRepository
from catalog_microservice.data.use_cases.product_finder import ProductFinder as ProductFinderUseCase
from catalog_microservice.presentation.controller.product_finder_controller import ProductFinderController


def product_finder_composer():
    
    repository = ProductRepository()
    use_case = ProductFinderUseCase(repository)
    controller = ProductFinderController(use_case)
    
    return controller.handle
