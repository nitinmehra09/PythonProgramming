with open("log.html", "r") as f:
    contain = f.read()
p = "python"
if p in contain :
    print("Yes, python")

else:
    print("No, python")