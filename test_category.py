import unittest
from uuid import UUID

from category import Category

class TestCategory(unittest.TestCase):
    def test_name_is_rquired(self):
        with self.assertRaisesRegex(TypeError, "missing 1 required positional argument: 'name'"):
            Category()

    def test_name_deve_ter_menos_de_255_c(self):
        with self.assertRaisesRegex(ValueError, "Nome contém mais que 255 caracteres."):
            Category(name= "a" * 254)
            
    def test_category_id_tem_que_ser_uuid(self):
        category = Category(name="Filme")
        self.assertEquals(type(category.id), UUID)
        
    def test_cria_categoria_com_valores_default(self):
        categoria = Category(name="filem")
        self.assertEquals(categoria.name, "Filem") 
        self.assertEquals(categoria.description, "") 
        self.assertEquals(categoria.is_active, True)      
        
           
           
if __name__ == "__main__": 
    unittest.main()