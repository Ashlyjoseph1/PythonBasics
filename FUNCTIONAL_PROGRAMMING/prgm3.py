string=input("enter a string")
string1=" "
vowels='aeiouAEIOU'
for i in string:
    if i not in vowels:
         string1+=i
print(string1)
