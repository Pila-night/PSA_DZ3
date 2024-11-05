import random

def Polymorphic_Cipher_encrypt(text,alphabet,key):
    text = text.upper()
    format_text = ""
    for char in text:
        if char in alphabet:
            format_text += char
    random.seed(key)
    sdvig = [random.randrange(len(alphabet)) for i in range(len(text))]
    i = 0
    encrypted_text = ""
    for char in format_text:
        index = alphabet.find(char)
        new_index = (index + sdvig[i]) % len(alphabet)
        encrypted_text += alphabet[new_index]
        i += 1                
    return encrypted_text

def Polymorphic_Cipher_decrypt(text,alphabet,key):
    text = text.upper()
    format_text = ""
    for char in text:
        if char in alphabet:
            format_text += char
    random.seed(key)
    sdvig = [random.randrange(len(alphabet)) for i in range(len(text))]
    i = 0
    encrypted_text = ""
    for char in format_text:
        index = alphabet.find(char)
        new_index = (index - sdvig[i]) % len(alphabet)
        encrypted_text += alphabet[new_index]
        i += 1                
    return encrypted_text  
    

alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
key = 27092
text = "ПОБЕДА!!!"

encrypted_text = Polymorphic_Cipher_encrypt(text, alphabet, key)
print("Алфавит:", alphabet)
print("Ключ:", key)
print("Исходный текст:", text)
print("Зашифрованный текст:", encrypted_text)
print("Расшифрованный текст:", Polymorphic_Cipher_decrypt(encrypted_text, alphabet, key))
    
    
