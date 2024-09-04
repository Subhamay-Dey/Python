sample_tuple = (1, 2, 3, 1, 4, 2, 5, 1)
print(f"Tuple data: {sample_tuple}")

repeated_items = {item for item in sample_tuple if sample_tuple.count(item) > 1}
print(f"The repeated items are: {repeated_items}")
