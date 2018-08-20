import sys
import string
from cs50 import get_string


def main():
    key = getKey()
    plainText = get_string("plaintext: ")
    cipherText = ""
    keyCounterIndex = 0

    # print(key)

    for i in range(len(plainText)):
        if plainText[i] in string.ascii_letters:
            plainTextAlphaIndex = string.ascii_uppercase.index(plainText[i].upper())
        else:
            cipherText += plainText[i]
            continue

        # print(plainTextAlphaIndex, end="    ")
        while key[keyCounterIndex % len(key)] not in string.ascii_uppercase:
            keyCounterIndex += 1

        keyTextAlphaIndex = string.ascii_uppercase.index(key[keyCounterIndex % len(key)])
        keyCounterIndex += 1
        # print(keyTextAlphaIndex, end="    ")

        plainTextAlphaIndex = (plainTextAlphaIndex + keyTextAlphaIndex) % 26
        if plainText[i].isupper():
            cipherText += string.ascii_uppercase[plainTextAlphaIndex]
        elif plainText[i].islower():
            cipherText += string.ascii_lowercase[plainTextAlphaIndex]

    print("ciphertext: " + cipherText)


def getKey():
    if(len(sys.argv) == 2):
        keyWord = sys.argv[1].upper()
        for c in keyWord:
            if c not in string.ascii_uppercase:
                print("Usage: ./vigenere k")
                sys.exit(1)
        return keyWord

    print("Usage: ./vigenere k")
    sys.exit(1)


if __name__ == "__main__":
    main()