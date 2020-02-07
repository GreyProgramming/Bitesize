msg = input("What message do you want to reverse? ")
j = -len(msg)
word = ""
i=-1
while i>=j:
    if msg[i]==" ":
        print(word)
        word=""
    else:
        word=msg[i]+word
    i-=1
    if search in word:
print(word)