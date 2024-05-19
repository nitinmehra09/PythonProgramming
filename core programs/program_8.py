# string slicing 

name = input("Enter a string ")

print(f"reverse of {name} is " + name[-1:-(len(name)+1):-1])