
lang = input("Enter language: ")
accept = 'q4'
status = "q0"

if len(lang) >= 3:
    for index in range(len(lang)):
        if lang[index] == "b" and index == 0:
            status = "q1"
            if lang[index + 1] == "b":
                status = "q2"
                if lang[index + 2] == "b":
                    status = "q3"
                    break
        elif index > 1 and lang[index] == 'c' and status == 'q2':
            status = 'q2'
        elif index > 1 and lang[index] == 'a' and status == 'q2':
            status = 'q4'
        elif index > 1 and lang[index] == 'a' and status == 'q4':
            status = 'q5'

if status == accept:
    print("😃 - " + status)
else:
    print("❌ - " + status)
