# handy-clicker
Circuitpython HID emulator device with smart home functions
# handy-clicker

## circuitpython hid emulator with smart home functions

### Description:

Handy clicker is raspberry pi pico based device with additional keyboard for fpv cameras.

Example keyboard --> [LINK] <--

How does it work?

OSD camerea pilot on circuitboard got different resistors combined with buttons.
So if you push "UP" button there occour e.g. 6000 m ohm when down e.g 2000 m ohm.

I connected keyboard to pico pin's no 26 which is used to read analog values.
After that I measured all values corresponding to each button and save results.

Remember when want read analog values must add additional resistor.

Whole tutorial : [HOW READ ANALOG VALUE] 

## Libraries and software:
- CircuitPython - 6.3.0
- Python - 3.8
- [tuyapy] - api for smart home devices
- optparse - 1.5.3 - to use flags in cmd 


## Wiring
![Alt text](connection_photo.jpg?raw=true)




[LINK]: <https://www.amazon.com/RunCam-Key-Board-FPV-Camera/dp/B0874GPT4W>
[HOW READ ANALOG VALUE]: <https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/potentiometer-and-pwm-led>
[tuyapy]: <https://pypi.org/project/tuyapy/>
