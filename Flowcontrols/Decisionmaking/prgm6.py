price=int(input("enter the cost price of bike"))

tax=0

if(price>100000):

    tax=15/100*price

elif(price>50000 and price <=1000000):

    tax=10/100*price

else:

    tax=5/100*price

print(tax)