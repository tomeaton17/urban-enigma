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
f.write("| ID | Description | Completed |\n")
f.write("|----|-------------|-----------|\n")

counter = 0

for i in range(0, len(data)):
    if(data[i].get('project') and data[i]['project'] == 'urban-enigma' and
       data[i]['status'] != 'deleted'):
        if(data[i]['id'] != 0):
            counter += 1
            f.write("|" + str(counter) + "|" + str(data[i]['description']) +
                    "|" + "No" + "|\n")
        else:
            counter += 1
            f.write("|" + str(counter) + "|" + str(data[i]['description']) + "|"
                                                   + "Yes" + "|\n")



