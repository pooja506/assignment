i = input("Do you want to calculate BMI. Enter yes or no: ")

if i=="yes":
    weight = float(input("Enter weight: "))
    height = float(input("Enter height: "))

    BMI = weight//(height*height)

    if BMI in range(19,26):
        print(f"Your BMI is {BMI}.You are healthy")

    if BMI in range(0,19):
        print(f"Your BMI is {BMI}.You are below healthy range")

    else:
        print(f"Your BMI is {BMI}.You are obese. Lose weight to live longer.")
else:
    print("Thank you")
    