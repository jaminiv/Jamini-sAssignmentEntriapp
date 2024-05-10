try:
    file_name = input("Enter file name: ")
    file=open(file_name,"w")
    file.write("\n I AM THE HAPPIEST OF THEM ALL")
    file.close()
    print("Hello, Welcome to Python")
except FileNotFoundError:
    print('File you entered is not found')



