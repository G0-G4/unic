from pynput import keyboard
from Symbols import Symbols
from Trie import Trie

trie = Trie()
for k, v in Symbols.items():
    trie.add(k, v)

class MyException(Exception): pass

class Substitution:

    def __init__(self):
        self.symbols = Symbols
        self.curr = []
        self.complements = []
        self.i = 0
        self.inp = False
        self.iterate = False
        self.status = ''
        self.controller = keyboard.Controller()

    def delete(self, n = 1):
        for _ in range(n):
            self.controller.tap(keyboard.Key.left)
            self.controller.tap(keyboard.Key.delete)

    def on_press(self, key):
        if key == keyboard.KeyCode.from_char('\\'):
            self.status = 'inp'
        if self.status == 'iter' and key == keyboard.Key.backspace:
            self.status = ''
        if self.status == 'inp' and key == keyboard.Key.backspace:   
            if self.curr:
                del self.curr[-1]
            else:
                self.status = ''
            
        if self.status == 'inp':
            if hasattr(key, 'char') and key.char != '\\':
                self.curr.append(key.char)
        if key == keyboard.Key.space and self.status == 'inp':
            k = ''.join(self.curr)
            self.complements = []
            values = trie.complete(k)
            if values:
                self.delete(len(self.curr) + 2)
                self.controller.tap(values[0][1])
            self.status = ''
            self.curr = []
        if key == keyboard.Key.space and self.status == 'iter':
            self.status = ''
            self.curr = []
            self.complements = []
        if key == keyboard.Key.tab and self.status == 'inp':
            self.delete()
            k = ''.join(self.curr)
            self.complements = trie.complete(k)
            if self.complements:
                self.i = 0
                self.status = 'iter'
                self.delete(len(self.curr) + 1)
                self.controller.tap(self.complements[self.i][1])
                self.curr = []
        elif key == keyboard.Key.tab and self.status == 'iter':
            self.delete(2)
            self.i = (self.i + 1 ) % len(self.complements)
            self.controller.tap(self.complements[self.i][1])



    def run(self):
        with keyboard.Listener(
                on_press = self.on_press) as listener:
            listener.join()

s = Substitution()
s.run()