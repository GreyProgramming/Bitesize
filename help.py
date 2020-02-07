def missing(find_me):
    int_list = []
    new_text = find_me.read()
    new_list = []
    for i in new_text.split(","):
        int_list.append(int(i))
    for length_numbs in range(1,int_list[len(int_list)-1]+1):
        new_list.append(length_numbs)
    for q in new_list:
        if q not in int_list:
            print(q)
            new_list.append(int(q))
            test = open("test.txt","w")
            test.write(new_list)
    test.close()
new_txt = open("test.txt","r")
missing(new_txt)