import OLED
import time
import SmartSWR

mode='peak'

if mode == 'peak':
    OLED.printTitle("PEAK Pwr")
if mode == 'average':
    OLED.printTitle("AVG Pwr")

while True:
    OLED.printPWR('Waiting...')
    print(SmartSWR.rf1_voltage())
    print(SmartSWR.rf2_voltage())
#    if mode == 'peak':
#        SmartPWR.rf1_ppower()
#    if mode == 'average':
#        SmartPWR.rf1_apower()
