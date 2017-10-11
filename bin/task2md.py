import json, os

os.system("task export > task.json")

with open('task.json') as data_file:
    data = json.load(data_file)

f = open("../README.md", "r")
lines = f.readlines()
f.close()

f = open("../README.md", "w")
for line in lines:
    if line[0] != '|':
        f.write(line)
f.close()

f = open("../README.md", "a")
f.write("| ID | Description |\n")
f.write("|----|-------------|\n")

for i in range(0, len(data)):
    if(data[i]['id'] != 0):
        if(data[i]['project'] == 'urban-enigma'):
            f.write("|" + str(data[i]['id']) + "|" + str(data[i]['description']) +
                    "|\n")


