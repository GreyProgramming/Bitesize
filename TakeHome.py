Name = str(input("What is your name? "))
Sal = int(input("What is your monthly salary? "))
Tax = 0
if Sal>=3000:
    Tax=Sal*35/100
if Sal >= 2000 and Sal < 3000:
    Tax=Sal*25/100
if Sal >= 1000 and Sal < 2000:
    Tax=Sal*15/100
Net = Sal - Tax
print("Your tax is: ",Tax)
print("Takehome: ",Net)