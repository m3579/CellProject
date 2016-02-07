import RPi.GPIO as GPIO
import time


NUCLEUS_CAP_PIN = 31

DNA_1_THRESHHOLD = 100
DNA_2_THRESHHOLD = 50
DNA_3_THRESHHOLD = 0

DNA_1_PIN = 12
DNA_2_PIN = 16

def initForNucleusReading():
    global NUCLEUS_CAP_PIN
    
    GPIO.setup(NUCLEUS_CAP_PIN, GPIO.OUT)
    GPIO.output(NUCLEUS_CAP_PIN, GPIO.LOW)    

def getNucleusReading():
    global NUCLEUS_CAP_PIN

    GPIO.setup(NUCLEUS_CAP_PIN, GPIO.OUT)
    GPIO.output(NUCLEUS_CAP_PIN, GPIO.HIGH)
    time.sleep(0.1)

    GPIO.setup(NUCLEUS_CAP_PIN, GPIO.IN)

    counter = 0
    while GPIO.input(NUCLEUS_CAP_PIN) == GPIO.HIGH:
        counter += 1

    return counter
    
class Ribosome:

    def __init__(self, id_number, button_pin, led_pin, handler_pin, proteins_go_to_golgi):
        self.id_number = id_number
        self.button_pin = button_pin
        self.led_pin = led_pin
        self.handler_pin = handler_pin

        if proteins_go_to_golgi:
            self.handle_button_press = self.golgi_app_proteins_handler
        else:
            self.handle_button_press = self.free_proteins_handler

        GPIO.setup(self.button_pin, GPIO.IN)
        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.setup(self.handler_pin, GPIO.OUT)
        
        GPIO.output(self.led_pin, GPIO.LOW)
        GPIO.output(self.handler_pin, GPIO.LOW)

        GPIO.setup(DNA_1_PIN, GPIO.OUT)
        GPIO.setup(DNA_2_PIN, GPIO.OUT)

        GPIO.output(DNA_1_PIN, GPIO.LOW)
        GPIO.output(DNA_2_PIN, GPIO.LOW)


    def free_proteins_handler(self):
        if GPIO.input(self.button_pin) == GPIO.HIGH:
            self.flash_led()

            for i in range(5):
                GPIO.output(self.handler_pin, GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(self.handler_pin, GPIO.LOW)
                time.sleep(0.3)

    def golgi_app_proteins_handler(self):
        if GPIO.input(self.button_pin) == GPIO.HIGH:
            self.flash_led()

            GPIO.output(DNA_1_PIN, GPIO.LOW)
            GPIO.output(DNA_2_PIN, GPIO.LOW)

            dna = getNucleusReading()
            print(dna)
            if dna >= DNA_1_THRESHHOLD:
                GPIO.output(DNA_1_PIN, GPIO.HIGH)
                print("Dna1")
            elif dna >= DNA_3_THRESHHOLD:
                GPIO.output(DNA_2_PIN, GPIO.HIGH)
                print("Dna2")

    def flash_led(self):
        for i in range(3):
            GPIO.output(self.led_pin, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(self.led_pin, GPIO.LOW)
            time.sleep(0.2)
