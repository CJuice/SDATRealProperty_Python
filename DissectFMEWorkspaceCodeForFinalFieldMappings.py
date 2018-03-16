"""Grooms FME Workbench code into a mapping of workspace variable name to output Real Property field name"""

# E:\DoIT_SDATRealProperty_Project\RawFMEWorkbenchCode_FinalFieldMappingText.txt
import re

public_text_file = r"E:\DoIT_SDATRealProperty_Project\RawFMEWorkbenchCode_FinalFieldMappingText.txt"
lsline = []
with open(public_text_file,'r') as fhand_publictextfile:
    for line in fhand_publictextfile:
        line.strip()
        lsline = (line.split("<comma>"))

lt = "<lt>"
space = "space"
gt = "<gt>"
openparen = "openparen"
closeparen = "closeparen"
closecurly = "closecurly"
opencurly = "opencurly"
dict_values = {lt: "", space: " ", gt: "", openparen:"(", closeparen:")", opencurly: "{", closecurly: "}"}
masterlist = []
groomedlist = []

indexcounter=0
for item in lsline:
    indexcounter += 1
    if indexcounter % 2 == 0:
        masterlist.append((item,lsline[indexcounter-2]))

for variable,field in masterlist:
    for key in dict_values.keys():
        variable = re.sub(key,dict_values[key],variable)
        field = re.sub(key,dict_values[key],field)
    groomedlist.append((variable,field))

for fieldname in groomedlist:
    print(fieldname)
with open(r"E:\DoIT_SDATRealProperty_Project\FinalFieldMappingList.csv",'w') as fhand_final_field_mapping_list:
    fhand_final_field_mapping_list.write("Variable,RealPropertyField\n")
    for tup in groomedlist:
        fhand_final_field_mapping_list.write("{},{}\n".format(tup[0], tup[1]))
