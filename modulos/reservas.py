reservas = []

def crear_reserva(cliente, fecha, mesa):
    reserva = {"id": len(reservas) + 1, "cliente": cliente, "fecha": fecha, "mesa": mesa}
    reservas.append(reserva)
    print(f"Reserva creada: {cliente} - Mesa {mesa} - {fecha}")

def obtener_reservas():
    return reservas