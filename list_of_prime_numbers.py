# List of prime numbers of an user defined list

numbers=list(map(int,input("Enter the numbers of the list by sapcing:").split()))
prime_number=[]

for num in numbers:
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            prime_number.append(num)
print("The list of prime numbers is:",prime_number)            
                


