from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def encrypt(key: bytes, plaintext: str) -> tuple[bytes, bytes]:
    """
    Encrypts a plaintext string using AES-GCM and returns (nonce, cyphertext)
    """
    aes = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aes.encrypt(nonce, plaintext.encode("utf-8"), None)
    return nonce, ciphertext

def decrypt(key: bytes, nonce: bytes, ciphertext: bytes) -> str:
    """
    Decrypts AES-GCM ciphertext
    """
    aes = AESGCM(key)
    plaintext = aes.decrypt(nonce, ciphertext, None)
    return plaintext.decode("utf-8")
    