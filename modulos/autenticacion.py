usuarios = {
    "admin": "admin123",
    "mesero": "mesero123"
}

def login(usuario, contrasena):
    if usuario in usuarios and usuarios[usuario] == contrasena:
        print(f"Usuario '{usuario}' autenticado correctamente.")
        return True
    print("x Credenciales incorrectas.")
    return False