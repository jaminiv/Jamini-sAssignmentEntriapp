numbers = input("Enter a new list:")
l1=list(map(int,numbers.split(",")))
print(l1)
try:
    average = sum(l1)/len(l1)
    print("Average of list: ", round(average, 3))
except:
    print("error")
finally:
    print("The calculation has successfully processed!! Have a great day :)")