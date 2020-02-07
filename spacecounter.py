msg = input("This is a rudimentary word counter, though the logic could do with some tweaking. Enter a message: ")
space = 0
i=0
while i<len(msg):
    if msg[i]==" ":
        space+=1
    i+=1
print ("In your message: '",msg,"' you have",(space+1),"words, with a total message length of",len(msg),"characters.")