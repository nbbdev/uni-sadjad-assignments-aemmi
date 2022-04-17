
lang = input("Enter Language:")

accept = ["q2", "q4"]
status = "q0"

for index in range(len(lang)):
    if lang[index] == 'a' and (status == 'q0' or status == 'q1'):
        status = 'q1'
    elif lang[index] == 'b' and (status == 'q1' or status == 'q2'):
        status = 'q2'

    elif lang[index] == 'b' and (status == 'q0' or status == 'q3'):
        status = 'q3'
    elif lang[index] == 'a' and (status == 'q3' or status == 'q4'):
        status = 'q4'

if status in accept:
    print("😃 - " + status)
else:
    print("❌ - " + status)
