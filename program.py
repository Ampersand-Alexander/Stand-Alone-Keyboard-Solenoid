import serial
import serial.tools.list_ports
import time
import keyboard 
import pystray
import threading

from pystray import MenuItem as item
from PIL import Image

ser = None
toggle_on = False

def set_com(icon, item):
    print("System tray icon clicked!")
    pass

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

def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        print(f'You pressed')
        send_signal('1')
        time.sleep(.016)
        send_signal('0')

def run(ser, toggle_on):
    print("thread 2")
    while True:
        if ser is not None and toggle_on:
            try:
                key = keyboard.read_key()
                keyboard.hook(on_key_event)
                keyboard.wait("")
            except KeyboardInterrupt:
                pass
            finally:
                keyboard.unhook_all()
                ser.close()
        elif ser is None:
            print("failed to connect to port")

def turn_on():
    global toggle_on
    toggle_on = True
    print("turned on")

def turn_off():
    global toggle_on 
    toggle_on = False
    print("turned off")

def quit_program():
    menu = (item('Manually Adjust COM', set_com),item('Turn on', turn_on), item('Turn off', turn_off), item('Exit', quit_program), )
    image = Image.open("C:\\Users\\Perfe\\ML\\middlemanarduino\\icon.png")
    icon = pystray.Icon("Keyboard Solenoid", image, "Keyboard Solenoid", menu)
    icon.stop()

def run_icon():
    print("thread 1")
    menu = (item('Manually Adjust COM', set_com),item('Turn on', turn_on), item('Turn off', turn_off), item('Exit', quit_program), )
    image = Image.open("C:\\Users\\Perfe\\ML\\middlemanarduino\\icon.png")
    icon = pystray.Icon("Keyboard Solenoid", image, "Keyboard Solenoid", menu)
    icon.run()

ser=init()
Thread1 = threading.Thread(target=run_icon).start()
Thread2 = threading.Thread(target=run(ser, toggle_on)).start()

Thread1.join()
Thread2.join()
