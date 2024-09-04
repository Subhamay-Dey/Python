tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = ()

print(f"Tuple1 before swapping: {tuple1}")
print(f"Tuple2 before swapping: {tuple2}")

tuple3 = tuple1
tuple1 = tuple2
tuple2 = tuple3

print("Tuple1 after swapping:", tuple1)
print("Tuple2 after swapping:", tuple2)

#or

tuple4 = (1, 2, 3)
tuple5 = (4, 5, 6)

print(f"Tuple1 before swapping: {tuple4}")
print(f"Tuple2 before swapping: {tuple5}")

tuple4, tuple5 = tuple5, tuple4

print("Tuple1 after swapping:", tuple4)
print("Tuple2 after swapping:", tuple5)