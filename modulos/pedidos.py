pedidos = []

def crear_pedido(plato, precio):
    pedido = {"id": len(pedidos) + 1, "plato": plato, "precio": precio, "estado": "Pendiente"}
    pedidos.append(pedido)
    print(f"Pedido creado: {plato} - ${precio:,}")

def calcular_total():
    return sum(p["precio"] for p in pedidos)