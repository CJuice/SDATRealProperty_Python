path = input("Paste the path to the PublicData_##.txt file\n>")

with open(path,'r') as fhandpublicdatafile:
    linecount = 0
    for line in fhandpublicdatafile:
        if linecount < 10:
            lsline = line.split("|")
            concatenated = "{}{}{}".format(lsline[0], lsline[1], lsline[2])
            if concatenated.startswith("0"):
                concatenated = concatenated[1:-1]
            print("Unique ID: {}".format(concatenated))
            linecount+=1
        else:
            break

