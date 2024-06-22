
class CategoryNotFoundError(Exception):
     def __init__(self, category_id):
        super().__init__("Category with ID {} not found.".format(category_id))
        self.category_id = category_id