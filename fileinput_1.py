i=1

def inputData():
    name = input("Enter name:")
    age = input("Enter age:")
    city = input("Enter city:")
    f = open("person.txt", "a")
    f.write(f'{name} {age}  {city} "\n"')
    print(f"Data saved {name} {age} {city} ")
inputData()

while i<3:
    p = input("Press Y or y to enter again: ") 
    if p=='Y'or p=="y":
        inputData()
        i=i+1
    else:
        break



  

