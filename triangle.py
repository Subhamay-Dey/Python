import math
side1=float(input("Enter the first side of the triangle:"))
side2=float(input("Enter the second side of the triangle:"))
side3=float(input("Enter the third side of the triangle:"))
if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
    print("A triangle can be formed with these sides")
else:
    print(f"A triangle cannot be formed with these sides")
    
