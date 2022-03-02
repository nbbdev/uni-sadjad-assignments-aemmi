pythonLen = int(input("enter python len: "))
state = 0
for index in range(pythonLen):
    if(state == 0):
        state = 1
        print("🟩", end="")
    else:
        state = 0
        print("🟨", end="")
print() # enter last line