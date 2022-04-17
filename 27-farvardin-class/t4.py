
lang = input("Enter language: ")
accept = ["q0", "q1", "q2"]
status = "q0"

for index in range(len(lang)):
    if lang[index] == "b":
        if status == "q0":
            status = "q1"  # first b
        elif status == "q1":
            status = "q2"  # second b and acceptable
        elif status == "q2":
            status = "q3"  # more two b
            break

if status in accept:
    print("😃 - " + status)
else:
    print("❌ - " + status)
