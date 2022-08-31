

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

    def search(self, root, key=None, res=None):
        if root.isterminal:
            res.append((''.join(key), root.value))
        for ch in root.children:
            key.append(ch)
            self.search(root.children[ch], key, res)
            key = []
    
    def complete(self, key):
        curr = self.root
        for k in key:
            if k not in curr.children:
                return []
            curr = curr.children[k]
        res = []
        self.search(curr, [], res)
        return res
 