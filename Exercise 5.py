word=input("Enter a value:")
try:
    w=int(word)
    print("The value into 2 = ", (w*2))
    print("This has been INTIFIED!!!!!!!!!")
except ValueError:
    print("Error its a word kid!")

