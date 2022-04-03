import time
from RPi import GPIO
from RPLCD.gpio import CharLCD

GPIO.setwarnings(False)

lcd = CharLCD(pin_rs=37, pin_rw=None, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD, cols=16, rows=2)

lcd.clear()
lcd.write_string('Hello everyone')
time.sleep(5)
lcd.clear()
n=5
while n > 0:
    lcd.write_string(u"Hello world!")
    time.sleep(1)
    lcd.clear()
    time.sleep(1)
    n=n-1

lcd.close(clear=True)
