import random


def extended_euclidean(a, b):

    """Calculate the gcd(a,b) and solve the equation ax + by = gcd(a,b) using the Extended Euclidean Algorithm"""
    lista_pasos = []
    c = True
    
    if a < b:
        a, b = b, a
        c = False
    mod = a
    while b != 0:
        q = a // b
        r = a % b
        lista_pasos.append((a, b, q, r))
        a, b = b, r

    # Ahora hacia atrás: coeficientes de Bézout
    x1, y1 = 1, 0
    x2, y2 = 0, 1

    for a, b, q, r in lista_pasos:
        x = x1 - q * x2
        y = y1 - q * y2
        x1, x2 = x2, x
        y1, y2 = y2, y

    gcd = lista_pasos[-1][1]
    if c== False:
        x1, y1 = y1, x1  # Swap if we swapped a and b

    if x1 < 0:
        x1 = mod - abs(x1)

    return gcd, x1, y1



def mod_inverse(e, phi):

    """Calculate the modular inverse of e modulo phi"""
    gcd_value, x, y = extended_euclidean(e, phi)
    if gcd_value != 1:
        raise ValueError("Modular inverse does not exist")
    return x % phi

def text_to_number(text):

    """Calculate the number in ascii of a text"""
    return int.from_bytes(text.encode("utf-8"), byteorder="big")

def number_to_text(number):

    """Calculate the ascii text from a number"""
    num_bytes = (number.bit_length() + 7) // 8
    try:
        return number.to_bytes(num_bytes, byteorder="big").decode("utf-8")
    except:
        return "[Error converting number to text]"

def is_prime(n):

    """Check if a number is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def miller_rabin(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Escribimos n-1 como 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Prueba k veces
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def prim_num_find(k):
    if k < 1:
        raise ValueError("El número de cifras debe ser al menos 1")

    lower = 10**(k - 1)
    upper = 10**k - 1

    while True:
        candidate = random.randint(lower, upper)
        if candidate % 2 == 0:
            candidate += 1
        if miller_rabin(candidate):
            return int(candidate)



def main():
    # Example usage of the functions
    a = 7
    b = 60
    gcd, x, y = extended_euclidean(a, b)
    print(f"GCD({a}, {b}) = {gcd}, x = {x}, y = {y}")

    e = 7
    phi = 60
    inv = mod_inverse(e, phi)
    print(f"Inverse of {e} mod {phi} is {inv}")

    text = "Hello"
    num = text_to_number(text)
    print(f"Text '{text}' to number: {num}")    
    
    recovered_text = number_to_text(num)
    print(f"Number {num} to text: '{recovered_text}'")

    prime_check = is_prime(29)
    print(f"Is 29 prime? {prime_check}")

    prime_candidate = prim_num_find(2)
    print(f"Random 3-digit prime: {prime_candidate}")
    
    

if __name__ == "__main__":
    main()

