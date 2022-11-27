import glob

list_of_files = glob.glob('./*chat.txt')
print(list_of_files)

for file_name in list_of_files:
    with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        print(content)
    # FO = open(file_name.replace('txt', 'out'), 'r', encoding='utf-8', errors='ignore')
    # for line in FI:
    #     FI.read(line)

    # FI.close()
    # FO.close()