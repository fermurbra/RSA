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



def main():
    e = int(input("Enter value for e: "))
    phi = int(input("Enter value for phi: "))
    
    mod_inverse_value = mod_inverse(e, phi)
    

    print(f"The modular inverse of {e} mod {phi} is: {mod_inverse_value}")
    
    

if __name__ == "__main__":
    main()

