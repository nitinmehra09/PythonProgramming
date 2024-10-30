p = "little"

f = open("poem.txt", "r")
text = f.read()

if(p in text):
    print("Yes")

else:
    print("No")
    
f.close()