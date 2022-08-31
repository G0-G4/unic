from pynput import keyboard
from Symbols import Symbols

class MyException(Exception): pass

controller = keyboard.Controller()

class Substitution:

    def __init__(self):
        self.symbols = Symbols
        self.curr = []
        self.inp = False

    def on_press(self, key):
        # if key == keyboard.Key.esc:
        #     raise MyException(key)
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
            print(len(self.curr))
            k = ''.join(self.curr)
            print(k)
            if k in self.symbols:
                for _ in range(len(self.curr) + 2):
                    controller.tap(keyboard.Key.backspace)
                controller.tap(self.symbols[k])
            self.inp = False
            self.curr = []

    def run(self):
        with keyboard.Listener(
                on_press = self.on_press) as listener:
            listener.join()
            
            # try:
            #     listener.join()
            # except MyException as e:
            #     print('{0} was pressed'.format(e.args[0]))

s = Substitution()
s.run()