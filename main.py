from modulos.autenticacion import login
from modulos.reservas import crear_reserva, obtener_reservas
from modulos.pedidos import crear_pedido, calcular_total
from modulos.reportes import generar_reporte

print("=== SISTEMA DE RESTAURANTE ===\n")

# Autenticacion
login("admin", "admin123")

# Reservas
print("\n--- Módulo Reservas ---")
crear_reserva("Carlos López", "2025-06-01", 5)
crear_reserva("María García", "2025-06-02", 3)

# Pedidos
print("\n--- Módulo Pedidos ---")
crear_pedido("Bandeja Paisa", 35000)
crear_pedido("Ajiaco", 28000)
crear_pedido("Jugo de Lulo", 8000)

# Reportes
print("\n--- Módulo Reportes ---")
generar_reporte("Pedidos", 3, calcular_total())