#To find the greatest of three numbers entered by the user

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input('Enter third number:'))

if num1>num2 and num1>num3:
    print(num1,"is the greatest among them ")
elif num2>num1 and num2>num3:
    print(num2,"is the greatest among them")
else:
    print(num3,"is the greatest among them")