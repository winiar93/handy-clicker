import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import analogio

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

photoPIN = 26

#Raw readed values from pin 26
#LEFT = 4832
#RIGHT = 15100
#UP = 8000
#DOWN = 65520
#ENTER = 3000
def readLight(photoGP):
    photoRes = ADC(Pin(26))
    light = photoRes.read_u16()
    return light

#Define pins on board
potentiometer = analogio.AnalogIn(board.GP26)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

def blink_led_confirmation(amount: str):
    for i in range(amount):
        led.value = True
        time.sleep(0.2)
        led.value = False
        time.sleep(0.2)

while True:
    readings = round(potentiometer.value,0)
    print(readings)
    time.sleep(0.1)
    #importatnt step: adjust time.sleep values, sometimes pc need more time to react
    # in case of bad values script probably won't work 
    if 3000 <= readings <= 3100:
        blink_led_confirmation(1)
        time.sleep(0.5)
        keyboard.send(Keycode.WINDOWS, Keycode.R)
        time.sleep(0.5)
        #rename opera with any web browser you have
        layout.write("opera https://www.youtube.com/watch?v=16y1AkoZkmQ\n")
        time.sleep(5)
        #Press F to make party on full screen :) 
        keyboard.send(Keycode.F)
        
    if 65500 <= readings <= 66000:
        blink_led_confirmation(4)
        time.sleep(0.5)
        keyboard.send(Keycode.WINDOWS, Keycode.R)
        time.sleep(0.5)
        layout.write("cmd\n")
        time.sleep(0.5)
        #In line belov replace path to your python environment, but if you don't use and got everything on default
        #just type "python {path to main.py file with proper flag } you can choose -d to disable or -e to enable
        # **
        layout.write("C:/Users/winia/anaconda3/python.exe D:\micropython_dir\smart_home_tuyaha\main.py -d\n")
        time.sleep(5)
        keyboard.send(Keycode.WINDOWS, Keycode.DOWN_ARROW)
        
    if 7800 <= readings <= 8000:
        blink_led_confirmation(5)
        time.sleep(0.5)
        keyboard.send(Keycode.WINDOWS, Keycode.R)
        time.sleep(0.5)
        layout.write("cmd\n")
        time.sleep(0.5)
        # ** same here 
        layout.write("C:/Users/winia/anaconda3/python.exe D:\micropython_dir\smart_home_tuyaha\main.py -e\n")
        time.sleep(5)
        keyboard.send(Keycode.WINDOWS, Keycode.DOWN_ARROW)
        
    if 15050 <= readings <= 15300:
        blink_led_confirmation(2)
        with open('import_all.txt') as f:
            lines = f.read().splitlines()
            
        for line in lines:
            layout.write(line)
            time.sleep(0.5)
            keyboard.send(Keycode.SPACE)
            layout.write('\n')
            time.sleep(0.5)