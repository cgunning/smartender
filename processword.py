f = open("oj2.txt","r")
shit = f.readlines()
k = open("test.txt", "w")
for word in shit:
    #print("\"" + word.strip() + "\"")
    k.write("\"" + word.strip() + "\",\n")