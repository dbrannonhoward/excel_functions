from string import ascii_lowercase
from time import sleep

for number in range(4):
    print(number)
    sleep(0.25)

for character in ascii_lowercase:
    if character == 'd':
        break
    print(character)
    sleep(0.25)

name = input("what is your name")
if 'e' in name:
    print("\n" + name + " : \nthere is an e in your name")
else:
    print("\n" + name + " : \nthere is not an e in your name")