import unittest
import servidor

class TestServidor(unittest.TestCase):
    def test_formato_variables_correcto(self):
        server = servidor.Servidor()
        with self.assertRaises(ValueError):
            server.calculo('a', 'b', 'c', 'd', '')
    
    def test_tamaño_x_correcto(self):
        server = servidor.Servidor()
        resultado = server.calculo('2', '1', '3', '4', '')
        self.assertEqual(resultado, 'X_min no puede ser mayor que X_max')
    
    def test_tamaño_y_correcto(self):
        server = servidor.Servidor()
        resultado = server.calculo('1', '2', '4', '3', '')
        self.assertEqual(resultado, 'Y_min no puede ser mayor que Y_max')
    
    def test_calculo_area_correcto(self):
        server = servidor.Servidor()
        resultado = server.area(1,2,3,4)
        self.assertEqual(resultado, '1')
    
    def test_centro_correcto(self):
        server = servidor.Servidor()
        resultado = server.centro(1,2,1,2)
        self.assertEqual(resultado, '1.5 , 1.5')
    


if __name__ == '__main__':
    unittest.main()
