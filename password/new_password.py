import random
import string
import pytest

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

def test_generate_password():
    assert len(generate_password(8)) == 8
    assert generate_password() != generate_password()
    assert isinstance(generate_password(), str)

if __name__ == "__main__":
    print("Yeni şifreniz:", generate_password(12))