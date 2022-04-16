import common

zigma = ["a", "b", "c"]
lang = input("Enter language: ")
accept = ["q0", "q4"]
status = "q4"
# don't start with "abc" need 5 steps
minimumLangLen = 3

if common.checkDFALanguage(lang, zigma, True) == False:
    print("Sorry, this language is not supported")
elif len(lang) < minimumLangLen and len(lang) != 0:
    status = status
else:
    for index in range(len(lang)):
        if lang[index] == "a" and index == 0:
            status = "q1"
            if lang[index + 1] == "b":
                status = "q2"
                if lang[index + 2] == "c":
                    status = "q3"
                    break
                else:
                    status = "q4"
            else:
                status = "q4"
        else:
            status = "q4"

    if status in accept:
        print("😃 - " + status)
    else:
        print("❌ - " + status)
