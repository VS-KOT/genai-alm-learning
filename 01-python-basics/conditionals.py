#if , else, elif (else if) are same as c++.
# logical operators are - and, or, not
statement = True
number = 9
if statement and number == 7:
    print("True stmt but not number")
elif statement and number == 9:
    print("True stmt and number")
else:
    print("Nothing true")

# is operator checks for the address in memeory rather than the value stored in it

list1 = [1,2,3]
list2 = [1,2,3]
list3 = list1

print(list1 is list2)       #will give false
print(list1 is list3)       #will print true
