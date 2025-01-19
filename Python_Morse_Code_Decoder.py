# morse code translator programme

# create dictionary of alphabet and corresponding morse code
morse_dict = {
        "A":".-",
        "B":"-...",
        "C":"-.-.",
        "D":"-..",
        "E":".",
        "F":"..-.",
        "G":"--.",
        "H":"....",
        "I":"..",
        "J":".---",
        "K":"-.-",
        "L":".-..",
        "M":"--",
        "N":"-.",
        "O":"---",
        "P":".--.",
        "Q":"--.-",
        "R":".-.",
        "S":"...",
        "T":"-",
        "U":"..-",
        "V":"...-",
        "W":".--",
        "X":"-..-",
        "Y":"-.--",
        "Z":"--.."
}

# input message (written in alphabet) encrypted into morse code
def encrypt(input):
        encrypted_message = ''
        for letter in input:
                if letter != " ":
                        encrypted_message += morse_dict[letter] + " "
                else:
                        encrypted_message += " "
        return encrypted_message

# input message (written in morse code) decyphered into alphabet letters
def decypher(input):
        input = input + " "
        decyphered_message = ''
        index = ""
        i = 0
        for letter in input:
                if (letter != " "):
                        i = 0
                        index += letter
                else:
                        if index: # if index contains code
                                for key, value in morse_dict.items():
                                        if index == value:
                                                decyphered_message += key
                                                break
                                index = "" # reset index after translating code
                        i += 1
                        if i == 2:
                                decyphered_message += " "
                                i = 0
        if index:
                for key, value in morse_dict.items():
                        if index == value:
                                decyphered_message += key
                                break
                index = ""
        return decyphered_message

def main():
        print("Do you want to decrypt from morse code or encrypt into morsecode?")
        decision = input("Type encrypt or decrypt: ").lower()
        print(decision)
        if decision == "encrypt":
                message = input("Enter your message to encrypt into morse code: ").upper()
                print("The translation for: ",message)
                result = encrypt(message)
                print(f"Your encrypted message is: {result}".format(result))
        elif decision == "decrypt":
                message = input("Enter your morse code to decrypt: ").upper()
                print("The translation for: ",message)
                result = decypher(str(message))
                print(f"Your decrypted message is: {result}".format(result))
        else:
                print("Invalid input.")

# call main function
main()
