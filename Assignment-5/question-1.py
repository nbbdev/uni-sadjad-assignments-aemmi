import common

zigma = ["a", "b"]
lang = input("Enter language: ")
accept = "q3"
status = "q0"
# Start with "aba" need 4 steps
minimumLangLen = 3

if common.checkDFALanguage(lang, zigma) == False:
    print("Sorry, this language is not supported")
elif len(lang) < minimumLangLen:
    status = status
else:
    for index in range(len(lang)):
        if lang[index] == "a" and index == 0:
            status = "q1"
            if lang[index + 1] == "b":
                status = "q2"
                if lang[index + 2] == "a":
                    status = "q3"

    if status == accept:
        print("😃 - " + status)
    else:
        print("❌ - " + status)
