import os

#to get current working directry
a = os.getcwd()
print(a)

#create folder
os.mkdir('New')

#to check folder is exist or not
ar = os.path.exists('New')
print(ar)

# for create file 
open('file.txt','a').close()
 
#create folder in diffrent directry 
os.mkdir(r'new\dos2')


# change directary
os.chdir('D:\github\PythonProgramming\Core Programs\Modules and Packages\OS Module')
# to get current working directry
a = os.getcwd()
print(a)


#make a list of all files/folder
print(os.listdir())


# for path in this list 
for item in os.listdir():
    print(os.path.join(os.getcwd(),item))

x = os.walk(r'')
for cp, fn, Fn in x:
    print(f"Folder = {Fn}")
    print(f"current path = {cp}")
    print(f"file name = {fn}")
    
    
    
