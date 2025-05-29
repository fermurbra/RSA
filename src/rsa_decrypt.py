# rsa_decrypt.py

from rsa_utils import number_to_text
def decrypt(ciphertext, d, N):
    message_int = pow(ciphertext, d, N)
    try:
        # Calcula cuántos bytes se necesitan
        message_length = (message_int.bit_length() + 7) // 8
        message_bytes = message_int.to_bytes(message_length, byteorder='big')
        return message_bytes.decode('utf-8')
    except Exception as e:
        return "[Error converting number to text]"
