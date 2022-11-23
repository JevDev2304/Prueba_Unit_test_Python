from funcion import obtener_valor
import unittest
class pruebas_obtener_valor(unittest.TestCase):
  def test_lista_cosas_1_int(self):
    self.assertEqual(type(obtener_valor(0)),type(6))
  def test_lista_cosas_2_str(self):
    self.assertEqual(type(obtener_valor(1)),type("eo"))
  def test_lista_cosas_3_None(self):
    self.assertEqual((type(obtener_valor(2))),type(None))
  def test_lista_cosas_4_list(self):
    self.assertEqual(type(obtener_valor(3)),type([]))
  def test_lista_cosas_5_tuple(self):
    self.assertEqual(type(obtener_valor(4)),type((5,7,9)))
  def test_lista_cosas_6_dict(self):
    self.assertEqual(type(obtener_valor(5)),type({}))
if __name__ == "__main__":
  unittest.main()
