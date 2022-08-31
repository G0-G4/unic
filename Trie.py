

class Node:

    def __init__(self, isterminal, children=None, value=None):
        self.children = children
        self.isterminal = isterminal
        self.value = value

class Trie:

    def __init__(self):
        self.root = Node(False, {})

    def add(self, key, value):
        curr = self.root
        for k in key:
            if k not in curr.children:
                curr.children[k] = Node(False, {})
            curr = curr.children[k]
        curr.isterminal = True
        curr.value = value

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
from Symbols import Symbols
trie = Trie()
for k, v in Symbols.items():
    trie.add(k, v)

def search(root):
    for ch in root.children:
        # print(ch)
        if root.children[ch].isterminal:
            print(root.children[ch].value)
        search(root.children[ch])

search(trie.root)
 