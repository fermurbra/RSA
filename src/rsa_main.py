# rsa_main.py

from rsa_setup import setup_rsa
from rsa_encrypt import encrypt
from rsa_decrypt import decrypt

def main():
    digits = int(input("How many digits should the prime numbers have? "))

    # Generate RSA keys
    p, q, N, e, d, phi = setup_rsa(digits)

    print("\n--- RSA KEYS ---")
    print(f"Public key (N, e): ({N}, {e})")
    print(f"Private key (N, d): ({N}, {d})")

    # Ask the user for a message to encrypt
    message = input("\nEnter the message to encrypt: ")

    # Encrypt the message
    try:
        encrypted = encrypt(message, e, int(N))
        print(f"\nEncrypted message (as number): {encrypted}")
    except ValueError as ve:
        print(f"[ERROR] {ve}")
        return

    # Decrypt the message
    decrypted = decrypt(encrypted, int(d), int(N))
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
