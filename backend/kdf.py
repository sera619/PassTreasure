import os
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from cryptography.exceptions import InvalidKey


def generate_salt() -> bytes:
    return os.urandom(16)


def derive_key(master_password: str, salt: bytes) -> bytes:
    """
    Derives a 256-bit key using Argon2id (modern cryptography API)
    """

    kdf = Argon2id(
        salt=salt,
        length=32,
        iterations=1,
        lanes=4,
        memory_cost=64 * 1024,
        ad=None,
        secret=None,
    )

    return kdf.derive(master_password.encode("utf-8"))


def verify_master_password(master_password: str, salt: bytes, expected_key: bytes) -> bool:
    """
    Verifies password using the updated Argon2id API.
    """
    kdf = Argon2id(
        salt=salt,
        length=32,
        iterations=1,
        lanes=4,
        memory_cost=64 * 1024,
        ad=None,
        secret=None,
    )

    try:
        kdf.verify(master_password.encode("utf-8"), expected_key)
        return True
    except InvalidKey:
        return False
