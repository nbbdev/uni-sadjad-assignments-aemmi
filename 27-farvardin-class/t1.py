
lang = input("Enter Language:")

accept = "az-bz"
status = "az-bz"

for index in range(len(lang)):
    if lang[index] == 'a' and status == "az-bz":
        status = "af-bz"
    elif lang[index] == 'a' and status == "af-bz":
        status = "az-bz"
    elif lang[index] == 'a' and status == "az-bf":
        status = "az-bz"
    elif lang[index] == 'a' and status == "af-bf":
        status = "az-bf"

    elif lang[index] == 'b' and status == "az-bz":
        status = "az-bf"
    elif lang[index] == 'b' and status == "az-bf":
        status = "az-bz"
    elif lang[index] == 'b' and status == "af-bz":
        status = "af-bf"
    elif lang[index] == 'b' and status == "af-bf":
        status = "af-bz"

if status == accept:
    print("😃 - " + status)
else:
    print("❌ - " + status)
