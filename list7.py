world_animals = ["Anaconda", "Platypus", "Red Panda", "Killer Whale", "Snow Leopard", "King Penguin", "Polar Bear", "Lion", "Zebra", "Plains Bison"]

position = 4
item_to_add = "Elephant"

print(f"List before insertion: {world_animals}")

world_animals.insert(position, item_to_add)

print(f"List after insertion: {world_animals}")