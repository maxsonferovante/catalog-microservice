from catalog_microservice.infra.database.repositories.products_repository import ProductRepository
from catalog_microservice.data.use_cases.product_register import ProductRegister as ProductRegisterUseCase
from catalog_microservice.presentation.controller.product_register_controller import ProductRegisterController

def product_register_composer():
    
    repository = ProductRepository()
    register_use_case = ProductRegisterUseCase(repository)
    controller = ProductRegisterController(use_case)
    
    return controller.handle


