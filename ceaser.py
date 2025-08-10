alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
letters = list(alphabet)
thisdict = {letters[i]: i for i in range(len(letters))}
dictthis = {i: letters[i] for i in range(len(letters))}
n = len(alphabet)

def encrypt(message, key):
    encryption = ""
    for ch in message:
        if ch not in thisdict:
            raise ValueError(f"Invalid character: {ch}")
        encryption += dictthis[(thisdict[ch] + key) % n]
    return encryption

def decrypt(message, key):
    decryption = ""
    for ch in message:
        if ch not in thisdict:
            raise ValueError(f"Invalid character: {ch}")
        decryption += dictthis[(thisdict[ch] - key) % n]
    return decryption

# Example
msg = ""
key = 7
enc = encrypt(msg, key)
dec = decrypt(enc, key)
print("Encrypted:", enc)
print("Decrypted:", dec)
