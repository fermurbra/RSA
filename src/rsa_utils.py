def extended_euclidean(a, b):
    lista_pasos = []
    a = abs(a)
    b = abs(b)

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



def mod_inverse(e, phi):
    gcd_value, x, y = extended_euclidean(e, phi)
    if gcd_value != 1:
        raise ValueError("Modular inverse does not exist")
    return x % phi

def text_to_number(text):

    return int.from_bytes(text.encode("utf-8"), byteorder="big")

def number_to_text(number):
    
    num_bytes = (number.bit_length() + 7) // 8
    try:
        return number.to_bytes(num_bytes, byteorder="big").decode("utf-8")
    except:
        return "[Error converting number to text]"

def is_prime(n):

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
    # Ejemplo de uso de las funciones
    a = 30
    b = 21
    gcd, x, y = extended_euclidean(a, b)
    print(f"GCD({a}, {b}) = {gcd}, x = {x}, y = {y}")

    e = 7
    phi = 40
    inv = mod_inverse(e, phi)
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

