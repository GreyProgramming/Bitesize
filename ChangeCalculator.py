Cost = int(input("What is the price of the item? "))
Paid = int(input("What is the price paid? "))
Change = Paid-Cost

Fifty = Change // 50                # Mod base 50
Twenty = Change % 50 // 20          # Mod 50, base 20s
Ten = Change %50 %20 // 10          # Mod 50, 20, base 10
Five = Change %50 %20 %10 //5       # Mod 50, 20, 10, Base 5
Two = Change %50 %20 %10 %5 //2     # Mod 50, 20, 10, 5, Base 2
One= Change %50 %20 %10 %5 %2 //1   # Mod 50, 20, 10. 5, 2, Base 1

print("The change is:")
print(" Fifties: ",Fifty)
print("Twenties: ",Twenty)
print("    Tens: ",Ten)
print("   Fives: ",Five)
print("    Twos: ",Two)
print("    Ones: ",One)

