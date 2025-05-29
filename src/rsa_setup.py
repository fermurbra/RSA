# rsa_setup.py

import random
import secrets
import math
from itertools import compress
from rsa_utils import mod_inverse, is_prime, prim_num_find


def setup_rsa(digits):
    """
    Genera claves RSA:
    - Dos primos aleatorios p y q
    - Clave pública: (e, N)
    - Clave privada: (d, N)
    """
    p = prim_num_find(digits)
    q = prim_num_find(digits)
    while q == p:
        q = prim_num_find(digits)

    N = p * q
    phi = (p - 1) * (q - 1)

    
    # Elige e = 65537 si es válido, si no, busca otro impar pequeño
    if 1 < 65537 < phi and math.gcd(65537, phi) == 1:
        e = 65537
    else:
        e = 3
        while e < phi and math.gcd(e, phi) != 1:
            e += 2
        if e >= phi:
            raise ValueError("No se encontró un 'e' adecuado.")

    if math.gcd(e, phi) != 1:
        e = 3
        while math.gcd(e, phi) != 1:
            e += 2

    d = mod_inverse(e, phi)

    print(f"p   = {p}")
    print(f"q   = {q}")
    print(f"N   = {N}")
    print(f"phi = {phi}")
    print(f"e   = {e}")
    print(f"d   = {d}")

    return p, q, N, e, d, phi


def main():

    digits = int(input("Enter the number of digits for the prime numbers: "))
    p, q, N, e, d, phi = setup_rsa(digits)

    print("\nPublic Key (e, N):")
    print(f"e = {e}, N = {N}")

    print("\nPrivate Key (d, N):")
    print(f"d = {d}, N = {N}")

if __name__ == "__main__":
    main()
