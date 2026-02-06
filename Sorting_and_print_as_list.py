#Count the number of countries strarting with "I"
#Print the names as a list



countries=["India","United States","Srilanka","Australia","Cuba","Iceland"]
l1=[]
count=0
for country in countries:
    if country.startswith("I"):
        count+=1
        l1.append(country)
print("The number of country name starting with'I'is:",count)        
print("Country name starting with'I'is:",l1)        