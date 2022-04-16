import common

zigma = ["a", "b", "c"]
lang = input("Enter language: ")
accept = "q0"  # even
status = "q0"
# even characters need 2 steps
minimumLangLen = 0

if common.checkDFALanguage(lang, zigma) == False:
    print("Sorry, this language is not supported")
elif len(lang) < minimumLangLen:
    status = status
else:
    for index in range(len(lang)):
        if status == "q0":
            status = "q1"
        else:
            status = "q0"

    if status == accept:
        print("😃 - " + status)
    else:
        print("❌ - " + status)
