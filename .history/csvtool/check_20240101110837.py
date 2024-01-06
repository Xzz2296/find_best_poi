with open(r'E:\xpj\research\POI\check\d.txt') as file1, open(r'E:\xpj\research\POI\check\dd.txt') as file2:
    lines = file1.readlines()
    lines2 = file2.readlines()
    set2 = set(line.strip() for line in file2)

result = set2 - set1

with open('result.txt', 'w') as output_file:
    for item in result:
        output_file.write(f"{item}\n")
