import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len (dac)
levels = 2**bits
maxVoltage = 3.3

def decimal2binary (decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def bin2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal

GPIO.setmode (GPIO.BCM)
GPIO.setup (dac, GPIO.OUT, initial = GPIO.LOW)

try:
    while True:
        inputStr = input("('GO' to start) and ('Q' to exit) >")
        
        if inputStr == 'GO':
            while True:
                for i in range (levels):
                    bin2dac(i)
                    time.sleep (0.02)
                for i in range (levels):
                    bin2dac(levels - i-1)
                    time.sleep(0.02)
        
                if inputStr == 'Q':
                    break 
               
except KeyboardInterrupt:
    print ("The program was stopped by the keyboard")
else:
    print ("No exceptions")
finally:
    GPIO.output(dac,GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")