with open("log.html") as f:
    lines = f.readlines()
    
line_no = 1
for line in lines:
    if ("python" in line):
        print(line_no) 
        break
    line_no += 1

else:
    print("Python not found in the log file.")
