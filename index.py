value=input("enter the number to find armstrong or not: ")

temp=0
for i in value:
    temp=temp+int (i)**int(len(value) )

if(temp==int(value)):
    print("it is Armstrong")

else:
    print("Not Armstrong")