# Cryptography

## Overview

This lab involves creating simple encryption and decryption functions using Python. The objective is to develop a basic understanding of cryptographic principles by implementing a Caesar cipher, a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Project Structure

The project is structured as follows:

```
├── .venv
├── cryptography
│   ├── __init__.py
│   ├── encryption.py
├── test
│   ├── __init__.py
│   ├── test_encryption.py
├── .gitignore
├── README.md
├── requirements.txt
```

- **cryptography/**: Contains the main module code.
  - `__init__.py`: Initializes the module.
  - `encryption.py`: Contains the `encrypt` and `decrypt` functions.
- **test/**: Contains the test code.
  - `__init__.py`: Initializes the test module.
  - `test_encryption.py`: Contains tests for the `encrypt` and `decrypt` functions.
- **.gitignore**: Specifies files and directories to be ignored by git.
- **README.md**: Provides an overview and explanation of the project.
- **requirements.txt**: Lists the Python dependencies for the project.

## Functions

### encrypt

```python
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
```

### decrypt

```python
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
```

## Tests

The tests are written using `pytest` and are located in `test/test_encryption.py`. The tests verify that the `encrypt` and `decrypt` functions work correctly.

### Example Tests

```python
import pytest
from cryptography.encryption import encrypt, decrypt

def test_encrypt_simple():
    assert encrypt("abc", 1) == "bcd"

def test_encrypt_wraparound():
    assert encrypt("xyz", 1) == "yza"

def test_encrypt_with_space():
    assert encrypt("a b c", 1) == "b!c!"

def test_decrypt_simple():
    assert decrypt("bcd", 1) == "abc"

def test_decrypt_wraparound():
    assert decrypt("yza", 1) == "xyz"

def test_decrypt_with_space():
    assert decrypt("b!c!", 1) == "a b c"
```

