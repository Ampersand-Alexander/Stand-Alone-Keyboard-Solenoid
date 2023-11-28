import serial
import time
import keyboard 

ser = serial.Serial('COM7', 9600)  

def send_signal(signal):
    ser.write(signal.encode()) 

try:
    while True:
        key = keyboard.read_key()
        if key != "F7":
            print(f'You pressed {key}')
            send_signal('1')
            time.sleep(.05)
            send_signal('0')
        if key == "=": 
            print(f'Safe exit')
            send_signal('0')
            break

except KeyboardInterrupt:
    pass

finally:
    ser.close()
