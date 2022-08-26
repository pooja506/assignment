
from prettytable import PrettyTable

f = open("person.txt", "r")
table = PrettyTable('Name','Age','City')
for line in f:
    line = line.strip().split(",")
    table.add(line)
    print(table)