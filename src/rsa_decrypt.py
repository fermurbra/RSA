
def decrypt(ciphertext, d, N):

    """Decrypts a ciphertext using RSA decryption with private key (d, N)"""
    
    message_int = pow(ciphertext, d, N)
    try:
        # Calculate the number of bytes needed to represent the integer 
        message_length = (message_int.bit_length() + 7) // 8
        message_bytes = message_int.to_bytes(message_length, byteorder='big')
        return message_bytes.decode('utf-8')
    except Exception as e:
        return "Error converting number to text"
