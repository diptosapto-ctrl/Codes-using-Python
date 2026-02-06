#Check if a list contains a palindrom of elements

number=[1,2,3,2,1,2]

copy_number=number.copy()
copy_number.reverse()

if copy_number==number:
    print("Its a palindrom")
else:
    print("Its not palindrom")