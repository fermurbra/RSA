def encrypt(message, e, N):

    """Encrypts a message using RSA encryption with public key (e, N)"""

    # Convert the message to an integer
    message_bytes = message.encode('utf-8')
    message_int = int.from_bytes(message_bytes, byteorder='big')
    if message_int >= N:
        return "Message too long for the current key size"
    return pow(message_int, e, N)
