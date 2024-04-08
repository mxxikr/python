from cryptography.fernet import Fernet

fernet = Fernet.generate_key()

fernet_key = fernet.decode().replace("=","")
print(fernet_key[16:])