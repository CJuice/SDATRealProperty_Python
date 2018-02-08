""" 20180207 CJS
This script processes the publicdata_#.txt fixed-width delimited text files. It uses the format string from
the FME workspace attribute splitter. I wanted to examine the data and understand what was split. This python script
will output a pipe delimited text file that you can open with excel. It does what the attribute splitter does.
"""
import os
# Example: E:\DoIT_SDATRealProperty_Project\RealPropAllData\PublicData_06.txt
public_text_file = input("Paste the PublicData_##.txt file path\n>")
os.path.basename(public_text_file)
newdatafile = r"E:\DoIT_SDATRealProperty_Project\_{}".format(os.path.basename(public_text_file))
SDAT_TXT_FILE_FORMAT_STRING = "2s2s12s2s2s1s34s34s25s30s30s22s2s5s4s4s20s24s24s5s1s2s22s5s22s5s4s6s3s5s4s3s5s4s1s3s4s6s3s5s5s5s5s5s5s1s1s1s3s2s1s1s4s4s1s6s2s2s2s1s5s3s1s1s1s1s1s1s1s1s1s1s1s1s5s3s2s2s6s34s3s5s4s3s5s4s1s1s8s9s1s9s5s1s9s9s2s12s6s34s3s5s4s3s5s4s1s1s8s9s1s9s5s1s9s9s2s12s6s34s3s5s4s3s5s4s1s1s8s9s1s9s5s1s9s9s2s12s3s9s4s3s9s4s3s9s4s9s4s9s4s9s4s9s9s9s9s6s6s4s9s9s9s9s9s9s9s6s6s4s9s9s9s9s9s9s9s9s9s9s9s9s9s9s9s9s9s1s4s40s8s9s9s9s1s9s9s9s9s9s9s1s1s9s9s9s1s8s8s8s8s8s10s1s8s9s8s8s10s1s8s8s2s8s8s8s8s8s1s1s2s2s1s2s4s5s5s1s4s2s7s12s1s8s8s4s9s9s9s9s9s9s7s7s7s1s8s150s1s8s3s3s3s4s4s2s7s4s18s2s12s6s3s1s8s1s8s1s8s8s8s4s1s"
lsline = SDAT_TXT_FILE_FORMAT_STRING.split("s")
lsline.remove('')
lsformatstringlengths = list(map(int,lsline))

def split_line_into_data(line, formatbreaklist = lsformatstringlengths):
    old, new = 0, 0
    data=""
    for i in range(len(formatbreaklist)):
        old = new
        new = old + int(formatbreaklist[i])
        if i > 0:
            data = "{}|{}".format(data, line[old:new].strip())
        else:
            data = "{}".format(line[old:new].strip())
    return data

with open(public_text_file,'r') as fhand_publictextfile, open(newdatafile,'w') as fhand_newfile:
    for line in fhand_publictextfile:
        fhand_newfile.write("{}\n".format(split_line_into_data(line)))


