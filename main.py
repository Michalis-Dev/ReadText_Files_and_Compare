

def my_function(file1, file2):
    f1 = open(file1, mode="r", encoding="utf-8")
    dataString = f1.read()
    #print(dataString)
    list1 = dataString.split("\n")

    f2 = open(file2, mode="r", encoding="utf-8")
    dataString = f2.read()
    #print(dataString)
    list2 = dataString.split("\n")

    list3 = []
    list4 = []
    for i in list1:
        for j in list2:
            if i == j:
                list3.append(i)

        list4 = (set(list1) - set(list2))

    print("τα αρχεία εχουν κοινά " + str(len(list3)) + " στοιχεία")
    print(list3)
    print("τα αρχεία έχουν διαφορετικά  " + str(len(list4)) + " στοιχεία")
    print(list4)

    return
