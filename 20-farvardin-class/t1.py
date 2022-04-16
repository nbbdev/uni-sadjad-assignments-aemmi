inp = input("enter sixma {a,b}: ")

accept = "q2"
status = "q3"

for index in range(len(inp) - 1):
    if inp[index] == "b" and inp[index + 1] == "b" and index >= len(inp) - 2:
        status = "q2"

if status == accept: 
    print("😃 - " + status)
else:
    print("❌ - " + status)
