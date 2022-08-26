headers = ["Name", "Age", "City"]

print(" ".join(headers))
for line in open("person.txt", "r"):
    line = line.strip().split(",")
    for i,word in enumerate(line):
        print(word)
    