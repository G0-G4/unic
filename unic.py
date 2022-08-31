from pynput import keyboard
from Symbols import Symbols
from Trie import Trie

trie = Trie()
for k, v in Symbols.items():
    trie.add(k, v)

class MyException(Exception): pass

controller = keyboard.Controller()

class Substitution:

    def __init__(self):
        self.symbols = Symbols
        self.curr = []
        self.inp = False

    def on_press(self, key):
        if key == keyboard.KeyCode.from_char('\\'):
            self.inp = True
        if self.inp and key == keyboard.Key.backspace:   
            if self.curr:
                del self.curr[-1]
            else:
                self.inp = False
            
        if self.inp:
            if hasattr(key, 'char') and key.char != '\\':
                self.curr.append(key.char)
            print(key)
        if key == keyboard.Key.space and self.inp:
            k = ''.join(self.curr)
            print(k)
            values = trie.complete(k)
            print(values)
            if values:
                for _ in range(len(self.curr) + 2):
                    controller.tap(keyboard.Key.backspace)
                controller.tap(values[0][1])
            self.inp = False
            self.curr = []

    def run(self):
        with keyboard.Listener(
                on_press = self.on_press) as listener:
            listener.join()

s = Substitution()
s.run()