"""Designed to process public data files, that have been processed to be '|' pipe delimited, and examine particular fields
for the presence of '-' in the data. Used successfully on 20180315 CJS"""

index_list = [89, 91, 95, 109, 111, 115, 129, 131, 139, 142, 145, 147, 149, 153, 154, 155, 156, 160, 162, 163, 164, 165, 166, 170, 171, 174, 175]
# Example: E:\DoIT_SDATRealProperty_Project\_PublicData_02.txt
public_text_file = input("Paste the file path for previously split Anne Arundel public data file\n>")
counter = 0
with open(public_text_file,'r') as fhand_publictextfile:
    for line in fhand_publictextfile:
        newlist = line.split("|")
        for index in index_list:
            if "-" in newlist[index]:
                counter+=1

print(counter)

