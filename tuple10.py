tuple_list = [(1, 'a', 3), (2, 'b', 2), (3, 'c', 1)]
print(tuple_list)
sorted_tuples = sorted(tuple_list, key=lambda x: x[2])
print(sorted_tuples)
