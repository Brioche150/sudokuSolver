plaintext = input("Plaintext: ")
ciphertext = ""
alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
plaintextPosition =0
while plaintextPosition < len(plaintext):
    plaintextChar = plaintext[plaintextPosition]
    alphabetPosition =3
    while plaintextChar != alphabet[alphabetPosition]:
        alphabetPosition += 1
    alphabetPosition -=3
    ciphertext = ciphertext + alphabet[alphabetPosition]
    plaintextPosition +=1
print(ciphertext)
