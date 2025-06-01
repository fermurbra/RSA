def encrypt(message, e, N):

    """Encrypts a message using RSA encryption with public key (e, N)"""

    # Convert the message to an integer using utf-8 encoding
    message_bytes = message.encode('utf-8')
    # To apply RSA, the message should be less than N but bigger than the normal value of ascii characters
    # Each byte is multiplied by 256 raised to the power of its position
    message_int = int.from_bytes(message_bytes, byteorder='big')
    if message_int >= N:
        return "Message too long for the current key size"
    return pow(message_int, e, N)
