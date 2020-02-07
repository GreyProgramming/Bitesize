Raw = int(input("Feed me 3 digit nums, please: "))
Hun = int(Raw/100)              #1 for 123
Ten = int((Raw-(Hun*100))/10)   #2 for 123
Sin = Raw%10                    #3 for 123
print(Hun+Ten+Sin)
