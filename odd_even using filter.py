seq=[1,2,3,4,5]
odd=lambda X:True if X%2!=0 else False
filtered_output=filter(odd,seq)
print(list(filtered_output))


seq=[1,2,3,4,5]
odd=list(filter(lambda X:X%2!=0,seq))
print(odd)