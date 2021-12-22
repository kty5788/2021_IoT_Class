from lcd import drivers
import time
import Adafruit_DHT
import RPi.GPIO as GPIO

sensor = Adafruit_DHT.DHT11
DHT_PIN = 19
LED_PIN = 4
BUZZER_PIN = 21 
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) #duty cycle(0~100) -소리 크기 조절
melody = [392,392,440,440,392,392,330,392,392,330,330,294,392,392,440,440,392,392,330,392,330,294,330,262]
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

now = datetime.datetime.now()

display = drivers.Lcd()

try:



finally:
    print('cleaning up')
    display.lcd_clear()
    pwm.stop()
    GPIO.cleanup()

    #이건 lcd 코드 이면서 우리가 합성할 코드
#lcd 코드 
print('Writing to Display')
    display.lcd_display_string(now.strftime("%x %X") , 1)
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        display.lcd_display_string('%.1f*C, %.1f%%' % (t, h), 2)
        time.sleep(0.5)

#piezo code 
for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)


#led 깜빡깜빡
import RPi.GPIO as GPIO
import time
LED_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

for i in range(10):
    GPIO.output(LED_PIN, GPIO.HIGH) #1
    print("led on")
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW) #0
    print("led off")
    time.sleep(1)

GPIO.cleanup() #초기화