from rsa_setup import setup_rsa
from rsa_encrypt import encrypt
from rsa_decrypt import decrypt

users = {}

def create_user():
    name = input("Write your username: ").strip()
    if name in users:
        print("This username already exists. Please choose another one")
        return None
    digits = int(input("How many digits do you want for the RSA keys? ").strip())
    p, q, N, e, d, phi = setup_rsa(digits)
    users[name] = {"public_key": (e, N), "private_key": (d, N)}
    
    print(f"User '{name}' created")
    print(f"Public key: (N={N}, e={e})")
    print(f"Private key: (N={N}, d={d})")

def select_user():
    name = input("Write your username: ").strip()
    if name not in users:
        print("The user does not exist")
        return None
    return name

def send_message():
    emitter = select_user()
    if not emitter:
        return None
    receiver = input("Who would you like to send the message to? ").strip()
    if receiver not in users:
        print("The receiver does not exist.")
        return None
    mensaje = input("Write your message: ").strip()
    e, N = users[receiver]['public_key']
    encrypted = encrypt(mensaje, e, N)
    users[receiver]['last_message'] = encrypted
    users[receiver]['from'] = emitter
    print(f"The message was encrypted and sent {encrypted}")

def read_message():
    receiver = select_user()
    if not receiver:
        return
    if 'last_message' not in users[receiver]:
        print("You have no new messages.")
        return None
    d, N = users[receiver]['private_key']
    encrypted = users[receiver]['last_message']
    decrypted = decrypt(encrypted, d, N)
    print(f"\n Messagee from {users[receiver]['from']}: {decrypted}")

def menu():
    print("\n Welcome to the RSA Messaging System")
    print("1. Create a new user")
    print("2. Send a message")
    print("3. Read a message")
    print("4. Exit")