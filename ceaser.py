def encrypt_decrypt(message, key):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    letters = list(alphabet)
    thisdict = {letters[i]: i for i in range(len(letters))}
    dictthis = {i: letters[i] for i in range(len(letters))}
    encryption = ""
    for i in message:
        encryption += dictthis[((thisdict[i] + key) % len(thisdict))]
    return encryption
def decrypt(message, key):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    letters = list(alphabet)
    thisdict = {letters[i]: i for i in range(len(letters))}
    dictthis = {i: letters[i] for i in range(len(letters))}
    decryption = ""
    for i in message:
        decryption += dictthis[((thisdict[i] - key) % len(thisdict))]
    return decryption









