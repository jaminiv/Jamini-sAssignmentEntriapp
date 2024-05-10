numbers = input("Enter a new list:")
print(type(numbers))
l1=list(map(int,numbers.split(",")))
print(l1)
print(type(l1))
l2=[]
try:
    for num in l1:
        if num>=0:
            l2.append(num)
    print("List without negative value:",l2)
except ValueError:
    print("There is no negative values")
