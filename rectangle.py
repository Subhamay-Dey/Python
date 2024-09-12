import math
l=float(input("Enter the length of the rectangle:"))
b=float(input("Enter the breadth of the rectangle:"))
ar=l*b
p=2*(l+b)
dg=math.sqrt(l**2+b**2)
print(f"Area:{ar}")
print(f"Perimeter:{p}")
print(f"Diagonal:{dg:2f}")
