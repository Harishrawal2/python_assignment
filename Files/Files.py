# 1. Write a program to read text file  
# 2. Write a program to write text to .txt file using  InputStream  
# 3. Write a program to read a file stream  
# 4. Write a program to read a file stream supports random access  
# 5. Write a program to read a file a just to a particular index using seek()  
# 6. Write a program to check whether a file is having read access and write access permissions 


file1 = open("hari.txt","r")
data = file1.read()
print(data)
print()

file2 = open("anil.txt","w")
str1 = 'Python'
file2.write(str1)
print()

file3 = open("Hari.txt","r+")
print(file3.readline(11))
print()
