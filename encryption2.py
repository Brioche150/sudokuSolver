plaintext = input("Plaintext: ")
ciphertext = ""
plaintextPosition =0
while plaintextPosition < len(plaintext):
    plaintextChar = plaintext[plaintextPosition]
    ASCIIvalue = ord(plaintextChar)
    ASCIIvalue -=3
    ciphertext = ciphertext + chr(ASCIIvalue)
    plaintextPosition +=1
print(ciphertext)