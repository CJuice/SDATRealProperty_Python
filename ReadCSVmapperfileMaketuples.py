path = r"E:\DoIT_SDATRealProperty_Project\TEMP\dwellingtype.txt"
lines_list=[]
with open(path,'r') as fhand:
    for line in fhand:
        line = line.strip()
        lines_list.append(line)

counter = 1
for item in lines_list:
    # print(item)
    if counter % 2 == 0:
        output = "('{}','{}'),".format(lines_list[counter-1],lines_list[counter])
        print(output)
    counter+=1