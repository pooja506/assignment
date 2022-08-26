i=1
def inputData():
    #user input 
    name = input("Enter name:") 
    age = input("Enter age:")
    city = input("Enter city:")
    f = open("person.txt", "a") #opens the file
    f.write(f'{name} {age}  {city} \n') #write into the file
    print(f"Data saved {name} {age} {city} ")
    
inputData()

while i<3: #loop to ask user to enter the data again 
    p = input("Press Y or y to enter again: ") 
    if p=='Y'or p=="y":
        inputData() #calls the function
        i=i+1
    else:
        break 



  

