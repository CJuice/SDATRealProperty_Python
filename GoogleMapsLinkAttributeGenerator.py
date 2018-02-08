aaa_googlemapsprefix = r"https://www.google.com/maps/place/"
comma_space = ", "
list_24_suppl = ", MD "
path = input("Paste the path to the PublicData_##.txt file\n>")
with open(path,'r') as fhandpublicdatafile:
    linecount = 0
    for line in fhandpublicdatafile:
        if linecount < 10:
            lsline = line.split("|")
            bbb_premiseaddress_raw = "{}+{}+{}+{}+{}".format(lsline[19], lsline[20], lsline[21], lsline[22], lsline[23])
            bbb_premiseaddress = bbb_premiseaddress_raw.replace(" ", "+")
            finalgooglelink_raw = "{}{}{}{}{}{}".format(aaa_googlemapsprefix, bbb_premiseaddress, comma_space, lsline[24], list_24_suppl, lsline[25])
            finalgooglelink = finalgooglelink_raw.replace(" ", "+")
            print(finalgooglelink)
            linecount+=1
        else:
            break