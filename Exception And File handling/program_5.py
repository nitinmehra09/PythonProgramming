words = ["donkey", "bag", "mc", "bc", "cutiya","bad"]

with open("contant.html", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"*len(word))

with open("contant.txt", "w") as f:
    f.write(content)