alpha = input("Please enter a string: ")
print(alpha)
cursor=""
answer=""
pos = 0
while pos<len(alpha):
    cursor=alpha[pos]
    if ord(cursor)>=48 and ord(cursor)<=57:
        answer=answer+str(int(cursor)*2)
    elif ord(cursor)>=65 and ord(cursor)<=90:
        answer=answer+chr(ord(cursor)+32)
    elif ord(cursor)>=97 and ord(cursor)<=122:
        answer=answer+chr(ord(cursor)-32)
    else:
        answer=answer+cursor
    pos+=1
print(len(answer)*"-")
print(answer)
