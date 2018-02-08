aaa_realpropertyprefix = r"https://sdat.dat.maryland.gov/RealProperty/Pages/viewdetails.aspx?County="
list_0_afterstring = r"&SearchType=ACCT&District="
list_1_afterstring = r"&AccountNumber="

path = input("Paste the path to the PublicData_##.txt file\n>")

with open(path,'r') as fhandpublicdatafile:
    linecount = 0
    for line in fhandpublicdatafile:
        if linecount < 10:
            lsline = line.split("|")
            finalrealproplink = "{}{}{}{}{}{}".format(aaa_realpropertyprefix, lsline[0], list_0_afterstring, lsline[1], list_1_afterstring, lsline[2])
            print(finalrealproplink)
            linecount+=1
        else:
            break

