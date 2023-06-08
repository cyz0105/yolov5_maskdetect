import serial
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def __init__(self, serial_port):
        self.serial_port = serial_port

    def on_modified(self, event):
        if event.src_path == '/Users/c/commands':
            with open(event.src_path, 'r') as f:
                data = f.readline()
                print("文件更改，下发指令")
                self.serial_port.write(data.encode())

import os
import time

while not os.path.exists('/dev/tty.usbserial-1110'):
    print('Waiting for /dev/tty.usbserial-1110')
    time.sleep(1)

# 继续执行其他代码
print("serial detected!")
ser = serial.Serial('/dev/tty.usbserial-1110', 9600)
event_handler = MyHandler(ser)
observer = Observer()
observer.schedule(event_handler, path='/Users/c', recursive=False)
observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()

observer.join()
