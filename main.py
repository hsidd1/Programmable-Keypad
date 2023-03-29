#Import necessary libraries -- obtain adafruit lib from repository or website
import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio

#Map GPIO Pins to keycaps based on wiring configuration
btn1_pin = board.GP9
btn2_pin = board.GP8
btn3_pin = board.GP7
btn4_pin = board.GP19
btn5_pin = board.GP20
btn6_pin = board.GP21

#Configure buttons
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

#Init keyboard
keyboard = Keyboard(usb_hid.devices)

#Define keycap sequences to combine based on datasheet layout
#These are based on the client request, you can make these do anything you want
def copy():
    keyboard.send(Keycode.CONTROL, Keycode.F7) 

def paste():
    keyboard.send(Keycode.CONTROL, Keycode.F8) 

def screenshot():
    keyboard.send(Keycode.CONTROL, Keycode.F9) 

def save():
    keyboard.send(Keycode.CONTROL, Keycode.F10) 

def power_control():
    keyboard.send(Keycode.CONTROL, Keycode.F11) 

#Execute client's requested commands based on button pressed
#Call corresponding command and map it to button of choice
while True:
    if btn1.value:
        copy() 
        time.sleep(0.1)
        
    if btn2.value:
        paste()
        time.sleep(0.1)

    if btn3.value:
        screenshot()
        time.sleep(0.1)

    if btn4.value:
        save()
        time.sleep(0.1)

    if btn5.value:
        power_control()
        time.sleep(0.1)
        
    if btn6.value:
        keyboard.send(Keycode.CONTROL, Keycode.F12) 
        time.sleep(0.1)
    time.sleep(0.1)
