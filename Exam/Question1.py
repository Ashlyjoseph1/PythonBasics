#check given string is palindrome or not
string=(input("enter a string"))
if(string==string[::-1]):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
