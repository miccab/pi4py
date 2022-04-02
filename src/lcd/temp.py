import os
import glob
import time
from RPi import GPIO
from RPLCD.gpio import CharLCD


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

#CELSIUS CALCULATION
def read_temp_c():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = int(temp_string) / 1000.0 # TEMP_STRING IS THE SENSOR OUTPUT, MAKE SURE IT'S AN INTEGER TO DO THE MATH
        temp_c = str(round(temp_c, 1)) # ROUND THE RESULT TO 1 PLACE AFTER THE DECIMAL, THEN CONVERT IT TO A STRING
        return temp_c



GPIO.setwarnings(False)

lcd = CharLCD(pin_rs=37, pin_rw=None, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD, cols=16, rows=2)
lcd.clear()
n=5
while n > 0:
    lcd.write_string(u"Hello everyone")
    time.sleep(1)
    lcd.clear()
    time.sleep(1)
    n=n-1

lcd.clear()
while True:
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Temp: " + read_temp_c() + unichr(223) + "C")
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Date: %s" %time.strftime("%m/%d/%Y"))
    time.sleep(1)

lcd.close(clear=True)
