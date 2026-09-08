import base64
from pathlib import Path

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa


MESSAGE = "Hello, this is my secret message!"


def symmetric_demo(message):
    # Reminder: Symmetric encryption should use the same secret key for both operations.
    key = Fernet.generate_key()
    cipher = Fernet(key)

    encrypted = cipher.encrypt(message.encode("utf-8"))
    decrypted = cipher.decrypt(encrypted).decode("utf-8")

    if decrypted != message:
        raise RuntimeError("Symmetric decryption did not match the input.")

    return (
        "=== SYMMETRIC ENCRYPTION (FERNET) ===\n"
        f"Key used for encryption and decryption: {key.decode('ascii')}\n"
        f"Input: {message}\n"
        f"Encrypted output: {encrypted.decode('ascii')}\n"
        # Remove hashtag from the next line if you want to see the decrypted output in results.txt 
        # f"Decrypted output: {decrypted}\n"
    )


def asymmetric_demo(message):
    # Asymmetric encryption uses a public key and a separate private key.
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()

    # RSA-OAEP with SHA-256 is used for this short message.
    oaep_padding = padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    )

    encrypted = public_key.encrypt(message.encode("utf-8"), oaep_padding)
    decrypted = private_key.decrypt(encrypted, oaep_padding).decode("utf-8")

    if decrypted != message:
        raise RuntimeError("Asymmetric decryption did not match the input.")

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode("ascii")

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode("ascii")

    encrypted_text = base64.b64encode(encrypted).decode("ascii")

    return (
        "=== ASYMMETRIC ENCRYPTION (RSA-OAEP) ===\n"
        "Public key used for encryption:\n"
        f"{public_pem}\n"
        "Private key used for decryption:\n"
        f"{private_pem}\n"
        f"Input: {message}\n"
        f"Encrypted output (Base64): {encrypted_text}\n"
        # Remove hashtag from the next line if you want to see the decrypted output in results.txt 
        # f"Decrypted output: {decrypted}\n"
    )


def main():
    report = (
        "ENCRYPTION AND DECRYPTION DEMO\n"
        "These keys are generated only for this class.\n"
        + symmetric_demo(MESSAGE)
        + "\n"
        + asymmetric_demo(MESSAGE)
    )

    output_file = Path(__file__).resolve().parent / "results.txt"
    output_file.write_text(report, encoding="utf-8")

    print("Symmetric encryption and decryption: successful")
    print("Asymmetric encryption and decryption: successful")
    print(f"Input message: {MESSAGE}")
    print(f"Results saved to: {output_file}")
    print("Open results.txt to see the keys, inputs, and outputs.")


if __name__ == "__main__":
    main()