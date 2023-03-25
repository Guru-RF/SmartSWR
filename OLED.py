import board
import busio
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect
import time

displayio.release_displays()

# Create the I2C interface.
i2c = busio.I2C(scl=board.GP21, sda=board.GP20)

if i2c.try_lock():
    print("Starting I2C scan.")
    devices = i2c.scan()
    i2c.unlock()

    print("Found %d I2C device(s)." % (len(devices)))
    for dev in devices:
        print("  I2C address:  %d (0x%x)" % (dev, dev))

else:
    print("Unable to lock I2C interface.")

display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Make the display context
splash = displayio.Group()
display.show(splash)#

def printTitle(msg):
    global splash

    msg='{message: <6}'.format(message=msg)
    # Draw a label
    text_area = label.Label(terminalio.FONT, text=msg, color=0xFFFFFF, x=0, y=8, scale=2)
    splash.append(text_area)
    time.sleep(0.1)
    splash.remove(text_area)

def printPWR(msg):
    global splash

    # Draw a label
    text_area = label.Label(terminalio.FONT, text=msg, color=0xFFFFFF, x=10, y=40, scale=2)
    splash.append(text_area)
    time.sleep(0.1)
    splash.remove(text_area)


