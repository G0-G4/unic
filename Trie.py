

class Node:

    def __init__(self, isterminal, children=None, value=None):
        self.children = children
        self.isterminal = isterminal
        self.value = value

class Trie:

    def __init__(self):
        self.root = Node(False, {})

    def add(self, key):
        curr = self.root
        for k in key:
            if k not in curr.children:
                curr.children[k] = Node(False, {})
            curr = curr.children[k]
        curr.isterminal = True

    def check(self, key):
        curr = self.root
        for k in key:
            if k not in curr.children:
                return
            curr = curr.children[k]
        return curr.isterminal

    def search(self, root, val=None, res=None):
        if root.isterminal:
            res.append(''.join(val))
        for ch in root.children:
            val.append(ch)
            self.search(root.children[ch], val, res)
            val = []
    
    def complete(self, key):
        curr = self.root
        for k in key:
            if k not in curr.children:
                return []
            curr = curr.children[k]
        res = []
        self.search(curr, [], res)
        return res
                


# root = Node(False, {
#     't': Node(True, {'o': Node(False, {'l': Node(True)})}, None),
#     'a': Node(True)
# })
trie = Trie()
trie.add('t')
trie.add('to')
trie.add('tool')
trie.add('trir')
trie.add('toolkit')



# print(trie.complete(''))

s = ''
while True:
    print(trie.complete(s))
    s += input()

# print()

# def search(root):
#     for ch in root.children:
#         print(ch)
#         if root.children[ch].isterminal:
#             print('!')
#         search(root.children[ch])

# search(trie.root)
 