# rsa_encrypt.py
from rsa_utils import text_to_number
def encrypt(message, e, N):
    message_bytes = message.encode('utf-8')
    message_int = int.from_bytes(message_bytes, byteorder='big')
    if message_int >= N:
        raise ValueError("Message too long for the current key size.")
    return pow(message_int, e, N)
