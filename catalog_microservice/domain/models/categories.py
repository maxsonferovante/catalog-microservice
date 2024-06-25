class Categories:
    def __init__(self, id: str, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description
        
    def __str__(self):
        return f'Category: {self.id}, {self.name}, {self.description}'
    
    def __repr__(self):
        return str(self)