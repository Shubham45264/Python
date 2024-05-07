print("welcome to the calculator made by Shubham")
num1 = int(input("Please enter your number1: \n"))
num2 = int(input("Please enter the number2: \n"))
print("Enter the Operation "+"+,-,*,/,**")
choice = input("Please enter your operation\n")
if choice=='*':
    print(num1*num2)
elif choice=="+":
    print(num1+num2)
elif choice=="-":
    print(num1-num2)
elif choice=="/":
    print(num1/num2)
elif choice=="**":
    print(num1**num2)
else:
    print("Invalid Operation")
