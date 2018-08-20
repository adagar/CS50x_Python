from cs50 import get_int

height = -1
while height < 0 or height > 23:
    height = get_int("Height: ")

for i in range(height):
    for j in range(height - (1 + i)):
        print(" ", end="")
    for k in range(0, 2 + i):
        print("#", end="")
    print()
