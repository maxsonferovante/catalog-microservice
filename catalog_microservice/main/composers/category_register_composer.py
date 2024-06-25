from catalog_microservice.infra.database.repositories.categories_repository import CategoryRepository
from catalog_microservice.data.use_cases.category_register import CategoryRegister as CategoryRegisterUseCase
from catalog_microservice.presentation.controller.categoty_register_controller import CategoryRegisterController

def category_register_composer():
    
    repository = CategoryRepository()
    use_case = CategoryRegisterUseCase(repository)
    controller = CategoryRegisterController(use_case)
    
    return controller.handle