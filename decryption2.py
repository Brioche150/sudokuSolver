ciphertext = input("ciphertext: ")
plaintext = ""

ciphertextPosition =0
while ciphertextPosition < len(ciphertext):
    ciphertextChar = ciphertext[ciphertextPosition]
    ASCIIvalue = ord(ciphertextChar)
    ASCIIvalue +=3
    plaintext = plaintext + chr(ASCIIvalue)
    ciphertextPosition +=1
print(plaintext)
