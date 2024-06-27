import pytest
from cryptography.encryption import encrypt, decrypt

def test_encrypt_A():
    assert encrypt("abc", 1) == "bcd"

def test_encrypt_B():
    assert encrypt("xyz", 1) == "yz{"

def test_encrypt_C():
    assert encrypt("a b c", 1) == "b!c!d"

def test_decrypt_D():
    assert decrypt("bcd", 1) == "abc"

def test_decrypt_E():
    assert decrypt("yz{", 1) == "xyz"

def test_decrypt_F():
    assert decrypt("b!c!d", 1) == "a b c"
