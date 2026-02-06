#Print the sum of n natural numbers:


n=int(input("Enter any number:"))
sum=0

for el in range(n+1):
    sum+=el
print("Total sum is:",sum)