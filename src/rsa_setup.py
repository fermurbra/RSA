import math
from rsa_utils import modulo_inverse, find_prime


def setup_rsa(digits):
    
    """ Generate RSA parameters: two distinct prime numbers p and q, modulus N, public exponent e, private exponent d, and Euler's totient phi"""

    # Find two distinct prime numbers p and q with the specified number of digits
    p = find_prime(digits)
    q = find_prime(digits)
    while q == p:
        q = find_prime(digits)

    # Calculate N and phi
    N = p * q
    phi = (p - 1) * (q - 1)

    
    # Choose e such that 1 < e < phi and gcd(e, phi) = 1   For example, e can be 65537, which is a common choice.
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

    # Calculate the modular inverse of e modulo phi to find d
    d = modulo_inverse(e, phi)

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
