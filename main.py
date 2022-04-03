# Imports

import random

# Main

def findFirst():
    numbs1 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    numb1 = (random.randint(1, 9))
    randomnpassnumb = (numbs1[numb1])
    return randomnpassnumb

while True:
    password = findFirst()
    print(password)


