f=("Sample")
f1=("Sample 2")
file1=open(f,"r")
data=file1.read()
with open (f1,"a") as file:
    file.write(data)
print("completed")