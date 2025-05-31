import random

def extended_euclidean(a, b):

    """Calculate the gcd(a,b) and solve the equation ax + by = gcd(a,b) using the Extended Euclidean Algorithm"""
    steps = []
    c = True
    
    # Ensure a is the larger number
    if a < b:
        a, b = b, a
        c = False
    mod = a

    # Apply and store steps of the Euclidean algorithm
    while b != 0:
        q = a // b
        r = a % b
        steps.append((a, b, q, r))
        a, b = b, r

    # Calculate x and y using the steps
    x1, y1 = 1, 0
    x2, y2 = 0, 1

    for a, b, q, r in steps:
        x = x1 - q * x2
        y = y1 - q * y2
        x1, x2 = x2, x
        y1, y2 = y2, y

    gcd = steps[-1][1]

    # Swap if we swapped a and b

    if c == False:
        x1, y1 = y1, x1  

    if x1 < 0:
        x1 = mod - abs(x1)

    return gcd, x1, y1


def modulo_inverse(e, phi):

    """Calculate the modular inverse of e modulo phi, the private key d in RSA"""

    gcd, x, y = extended_euclidean(e, phi)
    # gcd should be 1 because e and phi are coprime
    if gcd != 1:
        return "Error modular inverse does not exist"
    return x % phi

def miller_rabin(n, k=5):

    """Miller-Rabin primality test to check if n is prime"""

    # Check for small values of n
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Write n as d * 2^r
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Try k times
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

def find_prime(k):

    """Find a random prime number with k digits using the Miller-Rabin test"""

    if k < 1:
        return "Error k must be at least 1"

    lower = 10**(k - 1)
    upper = 10**k - 1

    # Apply the Miller-Rabin test to find a prime number

    while True:
        candidate = random.randint(lower, upper)
        if candidate % 2 == 0:
            candidate += 1
        if miller_rabin(candidate):
            return int(candidate)



def main():
    # Example usage of the functions
    a = 7
    b = 11
    gcd, x, y = extended_euclidean(a, b)
    print(f"GCD({a}, {b}) = {gcd}, x = {x}, y = {y}")

    e = 7
    phi = 60
    inv = modulo_inverse(e, phi)
    print(f"Inverse of {e} mod {phi} is {inv}")

    text = "Hello"
    num = text_to_number(text)
    print(f"Text '{text}' to number: {num}")    
    
    recovered_text = number_to_text(num)
    print(f"Number {num} to text: '{recovered_text}'")

    prime_candidate = find_prime(2)
    print(f"Random 3-digit prime: {prime_candidate}")
    
    

if __name__ == "__main__":
    main()

