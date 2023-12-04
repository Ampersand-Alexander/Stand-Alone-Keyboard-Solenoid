import serial
import serial.tools.list_ports
import time
import keyboard 


ser= None

def set_com():
    pass

def send_signal(signal):
    ser.write(signal.encode()) 

def init():
    try:
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if "Arduino" in p.description:
                print("attempting connection to ", p.device)
                ser = serial.Serial(p.device, 9600)  
                print(p.device, " has been connected")
                return ser
    except RuntimeError:
        print("we tried to connect to the port, but it was blocked or already taken. Attempt Manual serial connection instead")

def run(ser):
    if ser is not None:
        try:
            while True:
                key = keyboard.read_key()
                if key != None:
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
    else:
        print("failed to connect to port")

ser=init()
run(ser)
