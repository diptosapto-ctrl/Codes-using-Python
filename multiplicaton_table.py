#function to print its multiplication table:

num=int(input("Enter any number to calculate it's table:"))
i=1
def multiplication(num):
    for i in range(1,11):
        print(i,"X",num,"=",i*num)
        
multiplication(num)        

