aaa_finderprefix = r"http://planning.maryland.gov/finderonline?find="
# aaa_finderprefix = r"http://mdpgis.mdp.state.md.us/finderonlinejs/pi/index.html?address="

separatorstring = "%20" # represents a space in percent encoding
# path = input("Paste the path to the PublicData_##.txt file\n>")
path = r"E:\DoIT_SDATRealProperty_Project\_PublicData_22.txt"
with open(path,'r') as fhandpublicdatafile:
    linecount = 0
    for line in fhandpublicdatafile:
        if linecount < 10 :
            lsline = line.split("|")
            # x = enumerate(lsline)
            # for t in x:
            #     print(t[0], t[1])

            aaa_address = lsline[9]
            FINDER_address = "{}%20{}%20{}%20{}".format(aaa_address, lsline[11], lsline[12], lsline[13])
            # ccc_premiseaddress = "{}%20{}%20{}%20{}%20{}".format(lsline[19],lsline[20],lsline[21],lsline[22],lsline[23])
            ccc_premiseaddress = "{}%20{}%20{}%20{}%20{}%20{}%20{}-{}".format(lsline[19],lsline[20],lsline[21],lsline[22],lsline[23],lsline[24],lsline[25],lsline[26])
            finalFINDERlink = "{}{}".format(aaa_finderprefix,ccc_premiseaddress)
            finalFINDERlink =  finalFINDERlink.replace(" ","%20")

            print("This data appear to be based on Mailing Address")
            print("\taaa_address: {}".format(aaa_address))
            print("\tFINDER_address: {}".format(FINDER_address))
            print("This data/link is output to the table and appears to be based on Premise Address")
            print("\tccc_premiseaddress: {}".format(ccc_premiseaddress))
            print("\tFinal FINDER Link: {}\n".format(finalFINDERlink))

            # x = [lsline[9],lsline[11],lsline[12],lsline[13],lsline[19],lsline[20],lsline[21],lsline[22],lsline[23]]
            # .replace(" ", separatorstring)
            # x = separatorstring.join(x)
            # FINDER_address = "".format(lsline[9],lsline[11],lsline[12],lsline[13],lsline[19],lsline[20],lsline[21],lsline[22],lsline[23])
            # print(x)
            # print("{}{}".format(aaa_finderprefix,x))
            linecount+=1
        else:
            break
# http://mdpgis.mdp.state.md.us/finderonlinejs/pi/index.html?address=%20%20%20%20MD
