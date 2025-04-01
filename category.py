
import uuid

class Category:
    def __init__(
        self,
        name,
        id = "",
        description = "",
        is_active = True,
    ):
        self.id = id or uuid.UUID4()
        self.name = name
        self.description = description
        self.is_active = is_active
        
        if len(self.name) > 255: 
            raise ValueError("Nome contém mais que 255 caracteres.")
        
    def __str__(self):
        return f"{self.name} {self.description} {self.is_active}"
    
    def __repr__(self):
        return  f"<Category {self.name} ({self.id})>"
