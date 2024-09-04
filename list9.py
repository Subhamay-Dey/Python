world_animals = ["Anaconda", "Platypus", "Red Panda", "Killer Whale", "Snow Leopard", "King Penguin", "Polar Bear", "Lion", "Zebra", "Plains Bison", "Platypus"]

item_to_remove = "Platypus"
world_animals = [animal for animal in world_animals if animal != item_to_remove]

print(f"List after removing all occurrences of {item_to_remove}: {world_animals}")
