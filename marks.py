import math
marks=float(input("Enter the marks in percentage:"))
if marks>=90:
    print(f"First division")
elif marks>=70:
     print(f"Second division")
elif marks>=40:
    print(f"Third division")
else:
    print(f"Fail")
