def generateTable(n):
    table = ""
    for i in range (1,11):
        table += f"{i} X {n} = {n*i}\n"
    
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 41):
    generateTable(i)