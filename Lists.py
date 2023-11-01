#a. Put even and odd elements into two different lists
lstEven = [x for x in range(10) if x%2 == 0]
lstOdd = [x for x in range(10) if x%2 == 1]
print(f"Odd lst: {lstOdd}")
print(f"Even lst : {lstEven}")


#b. Merge and sort the two list
lst =[]
lst.extend(lstOdd)
lst.extend(lstEven)
lst.sort()
print(f"B : {lst}")

#c. Update first element with X value and delete the middle element of list.
lst[0] = 100
lst.pop(int(len(lst)/2))
print(f"C : {lst}")

#d. Find max and min element from the list.
print(max(lst))
print(min(lst))

#e. Add N names into the existing number list and check if word python is present in list.
itter = int(input("Enter how many names u wanna add"))
for i in range(itter):
    lst.append(input(f"Enter your {i+1} name: ").lower())

try:
    if lst.index("python"):
        print("Python is in the list")
except:
        print("Python is not there")