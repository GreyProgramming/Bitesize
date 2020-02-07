Name = str(input("What is your name? "))
Phys = int(input("What is your physics score? "))
Chem = int(input("What is your chemistry score? "))
Math = int(input("What is your maths score? "))
Total = Phys+Chem+Math
Per = Total*(100/450)
print("Total marks are: ", Total)
print("Percentage: ", Per)
if Per > 70:
    print("Great work, ",Name,". Keep it up")
else:
    print("You need to work harder, ",Name,".")