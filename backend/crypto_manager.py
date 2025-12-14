from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from cryptography.exceptions import InvalidKey
import os

class CryptoManager:    
    @staticmethod
    def encrypt(key: bytes, plaintext: str) -> tuple[bytes, bytes]:
        """
        Encrypts a plaintext string using AES-GCM and returns (nonce, cyphertext)
        """
        aes = AESGCM(key)
        nonce = os.urandom(12)
        ciphertext = aes.encrypt(nonce, plaintext.encode("utf-8"), None)
        return nonce, ciphertext
    
    @staticmethod
    def decrypt(key: bytes, nonce: bytes, ciphertext: bytes) -> str:
        """
        Decrypts AES-GCM ciphertext
        """
        aes = AESGCM(key)
        plaintext = aes.decrypt(nonce, ciphertext, None)
        return plaintext.decode("utf-8")

    @staticmethod
    def generate_salt() -> bytes:
        return os.urandom(16)

    @staticmethod
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

    @staticmethod
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