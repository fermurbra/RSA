def extended_euclidean(a, b):

    """Calculate the gcd(a,b) and solve the equation ax + by = gcd(a,b) using the Extended Euclidean Algorithm"""
    lista_pasos = []
    
    if a < b:
        a, b = b, a

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
    return gcd, x1, y1



def modulo_inverse(e, phi):

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



def main():
    # Example usage of the functions
    a = 30
    b = 21
    gcd, x, y = extended_euclidean(a, b)
    print(f"GCD({a}, {b}) = {gcd}, x = {x}, y = {y}")

    e = 7
    phi = 40
    inv = modulo_inverse(e, phi)
    print(f"Inverse of {e} mod {phi} is {inv}")

    text = "Hello"
    num = text_to_number(text)
    print(f"Text '{text}' to number: {num}")
    
    recovered_text = number_to_text(num)
    print(f"Number {num} to text: '{recovered_text}'")

    prime_check = is_prime(29)
    print(f"Is 29 prime? {prime_check}")
    
    

if __name__ == "__main__":
    main()

