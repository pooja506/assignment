headers = ["Name", "Age", "City"]

print("\t \t".join(headers)) # header added to format with tab
print("+-------------+----------------+-------------- ") # design format
for line in open("person.txt", "r"): # using loop to read data from each line from text file person.txt
    line = line.strip().split("  ")
    print("\t \t".join(line)) # displaying data in formatted form
    print("\n")
