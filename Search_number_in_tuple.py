# Search for a number X in the tuple [1,4,9,16,25,36,49,64,81,100] using loops.


X=int(input("Enter a number:"))
num=(1,4,9,16,25,36,49,64,81,100)

idx=0
for val in num:
    if val==X :
       print("Number found at index:",idx)
    idx+=1
    