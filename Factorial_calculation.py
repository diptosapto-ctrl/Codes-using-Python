#Calculate factorial without using recursion:
num=int(input("Enter a number & we will calculate its factorial:"))

def factorial(num):
    i = 1
    fact=1

    while i<=num:
        
        fact=fact*i
        i+=1
    print("The factorial is:",fact)

factorial(num)


#Calculate factorial using recursion:

num=int(input("Enter a number to calculate factorial:"))
def rec_fact(num):
    if num==1:
        return 1
    else:
        fact=num*rec_fact(num-1)
        return fact
    
print("The factorial is:", rec_fact(num))      

