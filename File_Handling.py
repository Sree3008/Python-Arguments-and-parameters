
print("File Reading")

# Option 1
file1=open('file.txt','r')
res=file1.read()
print(res)

# Option 2
file2=open('file.txt','r')
for i in file2:
    print(i)
file2.close()

# Option 3 and good approach
with open('file.txt','r') as file:
    print(file.read())


# File Writing
print("File Writing : ")
fw=open('file.txt','w')
fw.write("Now I am ready to make contact with you")
fw.close()

with open('file.txt','r') as i:
    print(i.read())

print()
# getting input from the user and append them into the file
feedback=input("Enter feedback : ")
with open('file.txt','w') as i:
    i.write(feedback+'\n')
print("Thanks for feedback")
print()
with open('file.txt','r') as file:
    print(file.read())



