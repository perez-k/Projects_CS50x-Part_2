# Mario less

while True:
    try:
        H = int(input("Height: "))   # Ask the user the desired pyramid's height
        if 1 <= H <= 8:              # Ensure height between 1 and 8
            break
    except ValueError:
        continue                     # Ignore invalid input and re-prompt


for i in range(H):                   # Print out the pyramid line by line
    for j in range(H - 1 - i):       # For the current line, spaces
        print(" ", end="")
    for j in range(i + 1):           # For the current line, blocks
        print("#", end="")
    print()                          # Next line
