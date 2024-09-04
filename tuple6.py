sample_tuple = (5, 5, 5, 5)
all_identical = all(item == sample_tuple[0] for item in sample_tuple)

print(f"Identical?: {all_identical}")
