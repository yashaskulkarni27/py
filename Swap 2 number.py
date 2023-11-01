a,b = [int(a) for a in input("Enter Tow values").split()]
temp = a
a = b
b = temp

print(f"a : {a}, b : {b}")

if a>0:
    print("Positive No")
elif a == 0:
    print("Zero")
else:
    print("Negitive No")

#With lov by BlazeRahim