headers = ["Name", "Age", "City"]

print("\t \t".join(headers))
print("+-------------+----------------+-------------- ")
for line in open("person.txt", "r"):
    line = line.strip().split("  ")
    print("\t \t".join(line))
    print("\n")