def encrypt(text, key):
    """
    Encrypts the given text using a simple Caesar cipher with the provided key.

    Parameters:
    text (str): The plaintext to be encrypted.
    key (int): The encryption key, which is an integer value.

    Returns:
    str: The encrypted text (ciphertext).
    """
    result = ""
    for char in text:
        result += chr((ord(char) + key) % 256)
    return result

def decrypt(text, key):
    """
    Decrypts the given text using a simple Caesar cipher with the provided key.

    Parameters:
    text (str): The ciphertext to be decrypted.
    key (int): The decryption key, which is an integer value.

    Returns:
    str: The decrypted text (plaintext).
    """
    result = ""
    for char in text:
        result += chr((ord(char) - key) % 256)
    return result


# Example usage of encrypt and decrypt functions

text = "Hello, World!"
key = 5

# Encrypt the text
encrypted_text = encrypt(text, key)
print("Encrypted text:", encrypted_text)

# Decrypt the text
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)