with open(r'E:\xpj\research\POI\check\jj.txt') as file1, open(r'E:\xpj\research\POI\check\j.txt') as file2:
    key1 =[]
    key2 =[]
    lines = file1.readlines()
    for line in lines:
        # key = line.split('/')[0]
        key =line
        key1.append(key)
    lines2 = file2.readlines()
    for line in lines2:
        key = line.split('_desc')[0]
        key2.append(key)


result = set(key1) - set(key2)

with open('result.txt', 'w') as output_file:
    for item in result:
        output_file.write(f"{item}\n")
