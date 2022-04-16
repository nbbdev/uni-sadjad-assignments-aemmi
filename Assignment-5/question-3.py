import common

zigma = ["a", "b"]
lang = input("Enter language: ")
accept = "q2"
status = "q0"
# at least two "b" need 3 steps
minimumLangLen = 2

if common.checkDFALanguage(lang, zigma) == False:
    print("Sorry, this language is not supported")
elif len(lang) < minimumLangLen:
    status = status
else:
    for index in range(len(lang)):
        if lang[index] == "b" and status != "q2":
            if status == "q0":
                status = "q1"  # first b
            elif status == "q1":
                status = "q2"  # second b and acceptable

    if status == accept:
        print("😃 - " + status)
    else:
        print("❌ - " + status)
