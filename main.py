# Write a Python Program to read numbers stored in a file and separate the even and odd numbers to two files named Even.txt and Odd.txt respectively. Display both the files 
f = open("file.txt", "r")
r=[]
even=""
odd=""
r=f.read().split()
e=open("Even.txt","w")
o=open("Odd.txt","w")
for i in r:
  if(int(i)%2==0):
    e.write(str(i+" "))
  else:
    o.write(str(i+" "))
e.close()
o.close()
f.close()