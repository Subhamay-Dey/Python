class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        current = self.root
        for i in range(31, -1, -1):  # 32-bit integers
            bit = (num >> i) & 1
            if bit not in current.children:
                current.children[bit] = TrieNode()
            current = current.children[bit]
        current.value = num
    
    def find_max_xor(self, num):
        current = self.root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggled_bit = 1 - bit  # Prefer the opposite bit for max XOR
            if toggled_bit in current.children:
                max_xor = (max_xor << 1) | 1
                current = current.children[toggled_bit]
            else:
                max_xor = (max_xor << 1)
                current = current.children[bit]
        return max_xor

def max_xor_subarray(arr):
    trie = Trie()
    trie.insert(0)  # Insert prefix XOR 0 for the case where subarray starts from the beginning
    max_xor = float('-inf')
    prefix_xor = 0

    for num in arr:
        prefix_xor ^= num
        trie.insert(prefix_xor)
        max_xor = max(max_xor, trie.find_max_xor(prefix_xor))
    
    return max_xor

# Test
arr = [8, 1, 2, 12, 7, 6]
print("Maximum XOR Subarray:", max_xor_subarray(arr))
