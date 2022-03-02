import random

vet = []

maxLen = int(input("enter list len: "));

def unique_fill():
    rand = random.randint(1, maxLen * 2)
    unique_fill() if rand in vet else vet.append(rand)

for _ in range(maxLen):
    unique_fill()

print(vet)
