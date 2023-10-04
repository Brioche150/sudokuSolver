ciphertext = input("ciphertext: ")
plaintext = ""
alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
ciphertextPosition =0
while ciphertextPosition < len(ciphertext):
    ciphertextChar = ciphertext[ciphertextPosition]
    alphabetPosition =3
    while ciphertextChar != alphabet[alphabetPosition]:
        alphabetPosition += 1
    alphabetPosition +=3
    plaintext = plaintext + alphabet[alphabetPosition]
    ciphertextPosition +=1
print(plaintext)
