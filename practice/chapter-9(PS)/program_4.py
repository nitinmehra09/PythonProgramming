with open("contant.txt", "r") as f:
    content = f.read()
    
newcontent = (content.replace("donkey", "######" )).replace("Donkey", "######")
with open("contant.txt", "w") as f:
    f.write(newcontent)