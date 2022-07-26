import hashlib
from simplecrypt import encrypt, decrypt

value="Me: Hello"

def SHA256():
    result=hashlib.sha256(value.encode())
    print("SHA256 Encrypted Data:",result.hexdigest())
SHA256()

def MD5():
    result= hashlib.md5(value.encode())
    print("MD5 Encrypted Data:",result.hexdigest())
MD5()

message="You: Hello"
hex_string=''

def encryption():
    global hex_string
    ciphercode=encrypt('AIM',message)
    hex_string=ciphercode.get()
    print("Encryption: ",hex_string)

def decryption():
    global hex_string
    byte_str=bytes.formhex(hex_string)
    original=decrypt('AIM',message)
    final_message=original.decode("utf-8")
    print("Decryption: ",final_message)

encryption()
decryption()