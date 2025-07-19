import time
import json
import Adafruit_ADS1x15
import os
import RPi.GPIO as GPIO

# Setup ADC for pH
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

# Setup DS18B20
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
temp_sensor_path = '/sys/bus/w1/devices/' + [d for d in os.listdir('/sys/bus/w1/devices/') if d.startswith('28')][0] + '/w1_slave'

# Setup JSN-SR04T
TRIG = 23
ECHO = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def read_temp():
    with open(temp_sensor_path, 'r') as f:
        lines = f.readlines()
    temp_string = lines[1].split('t=')[1]
    return float(temp_string) / 1000

def read_ph():
    value = adc.read_adc(0, gain=GAIN)
    voltage = value * 4.096 / 32767  # Convert to volts
    ph = 7 + ((2.5 - voltage) / 0.18)  # Calibrate for your sensor
    return round(ph, 2)

def read_level():
    GPIO.output(TRIG, False)
    time.sleep(0.5)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    duration = pulse_end - pulse_start
    distance = duration * 17150  # in cm
    return round(distance / 100, 2)  # in meters

data = {
    "temperature": read_temp(),
    "ph": read_ph(),
    "level": read_level()
}

print(json.dumps(data))
