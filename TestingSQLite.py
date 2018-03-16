import os
import sqlite3
# Example: E:\DoIT_SDATRealProperty_Project\RealPropAllData\PublicData_15.txt
public_text_file = input("Paste the PublicData_##.txt file path\n>")
os.path.basename(public_text_file)
newdatafile = r"E:\DoIT_SDATRealProperty_Project\_{}".format(os.path.basename(public_text_file))
SDAT_TXT_FILE_FORMAT_STRING = "2s2s12s2s2s1s34s34s25s30s30s22s2s5s4s4s20s24s24s5s1s2s22s5s22s5s4s6s3s5s4s3s5s4s1s3s4s6s3s5s5s5s5s5s5s1s1s1s3s2s1s1s4s4s1s6s2s2s2s1s5s3s1s1s1s1s1s1s1s1s1s1s1s1s5s3s2s2s6s34s3s5s4s3s5s4s1s1s8s9s1s9s5s1s9s9s2s12s6s34s3s5s4s3s5s4s1s1s8s9s1s9s5s1s9s9s2s12s6s34s3s5s4s3s5s4s1s1s8s9s1s9s5s1s9s9s2s12s3s9s4s3s9s4s3s9s4s9s4s9s4s9s4s9s9s9s9s6s6s4s9s9s9s9s9s9s9s6s6s4s9s9s9s9s9s9s9s9s9s9s9s9s9s9s9s9s9s1s4s40s8s9s9s9s1s9s9s9s9s9s9s1s1s9s9s9s1s8s8s8s8s8s10s1s8s9s8s8s10s1s8s8s2s8s8s8s8s8s1s1s2s2s1s2s4s5s5s1s4s2s7s12s1s8s8s4s9s9s9s9s9s9s7s7s7s1s8s150s1s8s3s3s3s4s4s2s7s4s18s2s12s6s3s1s8s1s8s1s8s8s8s4s1s"
parseddata = SDAT_TXT_FILE_FORMAT_STRING.split("s")
parseddata.remove('')
lsformatstringlengths = list(map(int, parseddata))
# print(len(lsformatstringlengths))

header_list = ["SDATField_{} text".format(i + 1) for i in range(len(lsformatstringlengths))]
questionmarkstring = ",".join(["?" for i in range(len(header_list))])
# print(header_list)
header_string = ",".join(header_list)
# print(header_string)
# exit()
conn = sqlite3.connect('testdb.db')
c = conn.cursor()
c.execute("CREATE TABLE table1 ({})".format(header_string))

def parse_line_into_data(line, formatbreaklist = lsformatstringlengths):
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
    count = 0
    for line in fhand_publictextfile:
        if count < 200:
            parseddata = parse_line_into_data(line)
            # print(parseddata)
            lslinedata = parseddata.split("|")
            newstring = "','".join(lslinedata)
            # print("SQL string\n'{}'".format(newstring))
            c.execute("INSERT INTO table1 VALUES ({})".format(questionmarkstring), lslinedata)
            # fullsqlstring = "INSERT INTO table1 VALUES ('{}')".format(newstring)
            # c.execute(fullsqlstring)
            conn.commit()
            # print(count)
            count+=1
        else:
            break
        # fhand_newfile.write("{}\n".format(split_line_into_data(line)))

for row in c.execute('SELECT * FROM table1'):
        print(row)

conn.close()
print(count)
# #EXAMPLE
# import sqlite3
# conn = sqlite3.connect('example.db')
# c = conn.cursor()
#
# # Create table
# c.execute('''CREATE TABLE stocks
#              (date text, trans text, symbol text, qty real, price real)''')
#
# # Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#
# # Save (commit) the changes
# conn.commit()
#
# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# conn.close()
# del conn
#
# import sqlite3
# conn = sqlite3.connect('example.db')
# c = conn.cursor()
#
# # Never do this -- insecure!
# # symbol = 'RHAT'
# # c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
#
# # Do this instead
# t = ('RHAT',)
# c.execute('SELECT * FROM stocks WHERE symbol=?', t)
# print(c.fetchone())
#
# # Larger example that inserts many records at a time
# purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#              ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#             ]
# c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
# for row in c.execute('SELECT * FROM stocks ORDER BY price'):
#         print(row)