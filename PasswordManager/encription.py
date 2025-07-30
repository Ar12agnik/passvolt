def encrypt(message,key,chars):
    encrypted_message =''
    for letters in message:
        encrypted_message+= key[chars.index(letters)]
    return encrypted_message
def decrypt(en_message,key,chars):
    decrypted =''
    for letters in en_message:
        decrypted+= chars[key.index(letters)]
    return decrypted