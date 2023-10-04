choiceMessage ="Please enter e if you would like to encrypt, d if you would like to decrypt, and n if you would like to stop: " 
print("a"+ chr(22) + "space")
print(ord("▬"))
choice = input(choiceMessage)
while choice != "n":
    shiftAmount = 5 
    if choice == "e":
        plaintext = input("Plaintext: ")
        ciphertext = ""
        plaintextPosition =0
        while plaintextPosition < len(plaintext):
            plaintextChar = plaintext[plaintextPosition]
            ASCIIvalue = ord(plaintextChar)
            print(ASCIIvalue)
            ASCIIvalue -= (shiftAmount % 13)
            print(ASCIIvalue)
            shiftAmount *= 2
            ciphertext = ciphertext + chr(ASCIIvalue)
            plaintextPosition +=1
        print(ciphertext)
    elif choice == "d":
        ciphertext = input("ciphertext: ")
        plaintext = ""
        ciphertextPosition =0
        while ciphertextPosition < len(ciphertext):
            ciphertextChar = ciphertext[ciphertextPosition]
            ASCIIvalue = ord(ciphertextChar)
            print(ASCIIvalue)
            ASCIIvalue += (shiftAmount%13)
            shiftAmount *= 2
            plaintext = plaintext + chr(ASCIIvalue)
            ciphertextPosition +=1
        print(plaintext)
    else:
        print("You mistyped")
    choice = input(choiceMessage)
print("Bye!")