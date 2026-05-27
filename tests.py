import unittest
from modulos.autenticacion import login
from modulos.reservas import crear_reserva, obtener_reservas, reservas
from modulos.pedidos import crear_pedido, calcular_total, pedidos
from modulos.reportes import generar_reporte

class TestAutenticacion(unittest.TestCase):

    def test_login_correcto(self):
        resultado = login("admin", "admin123")
        self.assertTrue(resultado)

    def test_login_incorrecto(self):
        resultado = login("admin", "wrongpass")
        self.assertFalse(resultado)

class TestReservas(unittest.TestCase):

    def setUp(self):
        reservas.clear()

    def test_crear_reserva(self):
        crear_reserva("Juan Pérez", "2025-06-01", 4)
        self.assertEqual(len(obtener_reservas()), 1)

    def test_datos_reserva(self):
        crear_reserva("Ana Torres", "2025-06-02", 2)
        r = obtener_reservas()[0]
        self.assertEqual(r["cliente"], "Ana Torres")
        self.assertEqual(r["mesa"], 2)

class TestPedidos(unittest.TestCase):

    def setUp(self):
        pedidos.clear()

    def test_crear_pedido(self):
        crear_pedido("Ajiaco", 28000)
        self.assertEqual(len(pedidos), 1)

    def test_calcular_total(self):
        crear_pedido("Bandeja Paisa", 35000)
        crear_pedido("Jugo de Lulo", 8000)
        self.assertEqual(calcular_total(), 43000)

    def test_estado_pedido(self):
        crear_pedido("Sancocho", 25000)
        self.assertEqual(pedidos[0]["estado"], "Pendiente")

if __name__ == "__main__":
    unittest.main()