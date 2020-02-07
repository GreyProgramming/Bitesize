found = 0
msg = input("Enter a search string: ")
find = input("What are you searching for?")
i=0
while i<len(msg):
    if msg[i]==find[0]:
        if msg[i:i+len(find)]==find:
            found+=1
            i+=len(find)-1
    i+=1
print("done! found",found,"instances.")