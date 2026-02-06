# WAP to enter the marks of threee subjects from the user and store them in a dictionary.Start with an empty dictionary and add one by one.
# Use subject name as key and marks as value .


mark1=(input("Enter subject1 mark:"))
mark2=(input("Enter subject2 mark:"))
mark3=(input("Enter subject3 mark:"))
dict={}
dict.update({"subject1":mark1})
dict.update({"subject2":mark2})
dict.update({"subject3":mark3})

print(dict)