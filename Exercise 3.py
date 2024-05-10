file1=open("Sample","r")
count=0
for line in file1:
    words = line.split(" ")
    count+=len(words)
file1.close()
print("Number of words in a Sample textfile is",count)
