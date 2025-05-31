# rsa_main.py

from rsa_setup import setup_rsa
from rsa_encrypt import encrypt
from rsa_decrypt import decrypt

import sys

usuarios = {}

def crear_usuario():
    nombre = input("Introduce un nombre de usuario: ").strip()
    if nombre in usuarios:
        print("[!] Ese usuario ya existe.")
        return
    digits = int(input("¿Cuántos dígitos deben tener los números primos? "))
    p, q, N, e, d, phi = setup_rsa(digits)
    usuarios[nombre] = {
        "public_key": (e, N),
        "private_key": (d, N)
    }
    print(f"[✓] Usuario '{nombre}' creado.")
    print(f" -> Clave pública: (N={N}, e={e})")
    print(f" -> Clave privada: (N={N}, d={d})")

def seleccionar_usuario():
    nombre = input("Introduce tu nombre de usuario: ").strip()
    if nombre not in usuarios:
        print("[!] Usuario no encontrado.")
        return None
    return nombre

def enviar_mensaje():
    emisor = seleccionar_usuario()
    if not emisor:
        return
    receptor = input("¿A quién deseas enviar el mensaje?: ").strip()
    if receptor not in usuarios:
        print("[!] Receptor no encontrado.")
        return
    mensaje = input("Escribe el mensaje a enviar: ")
    e, N = usuarios[receptor]['public_key']
    cifrado = encrypt(mensaje, e, N)
    usuarios[receptor]['ultimo_mensaje'] = cifrado
    usuarios[receptor]['de'] = emisor
    print(f"[✓] Mensaje cifrado enviado: {cifrado}")

def leer_mensaje():
    receptor = seleccionar_usuario()
    if not receptor:
        return
    if 'ultimo_mensaje' not in usuarios[receptor]:
        print("[!] No tienes mensajes nuevos.")
        return
    d, N = usuarios[receptor]['private_key']
    cifrado = usuarios[receptor]['ultimo_mensaje']
    descifrado = decrypt(cifrado, d, N)
    print(f"\n[📨] Mensaje de {usuarios[receptor]['de']}: {descifrado}")

def menu():
    print("\n🔐 Bienvenido al sistema de mensajería RSA")
    print("1. Crear nuevo usuario")
    print("2. Enviar mensaje")
    print("3. Leer mensaje")
    print("4. Ver claves de un usuario")
    print("5. Salir")

def mostrar_claves():
    nombre = seleccionar_usuario()
    if not nombre:
        return
    pub = usuarios[nombre]['public_key']
    priv = usuarios[nombre]['private_key']
    print(f"\nClave pública de {nombre}: (N={pub[1]}, e={pub[0]})")
    print(f"Clave privada de {nombre}: (N={priv[1]}, d={priv[0]})")

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            crear_usuario()
        elif opcion == '2':
            enviar_mensaje()
        elif opcion == '3':
            leer_mensaje()
        elif opcion == '4':
            mostrar_claves()
        elif opcion == '5':
            print("Saliendo del programa...")
            input("Presiona ENTER para cerrar...")
            sys.exit()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
