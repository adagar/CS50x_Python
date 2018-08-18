from cs50 import get_char

c = get_char("answer: ")

if c == "Y" or c=="y":
    print("Yes")
elif c == "N" or c == "n":
    print("No")