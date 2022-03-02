checkSortedList = input("enter list spliting by space:").split(" ")

if(len(checkSortedList) < 2):
    print("you must be enter begerthan 2 list")
else:
    before = float(checkSortedList[0]) - 1 # alway less than after
    for index in range(len(checkSortedList)):
        after = float(checkSortedList[index])
        if(before < after):
            before = after
            continue
        else:
            break
    if(before == after):
        print("your list is sorted")
    else:
        print("your list not sorted")