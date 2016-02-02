import RPi.GPIO as GPIO

try:
    GPIO.setmode(GPIO.BOARD)

    # Each array in this array is of the form
    # [pushbutton input pin, LED drive high/low pin]
    ribos = [[7, 11], [13, 15], [19, 21], [23, 29]]

    for ribo in ribos:
        GPIO.setup(ribo[0], GPIO.IN)
        GPIO.setup(ribo[1], GPIO.OUT)
    
    litLED = -1
    while True:
        for ribo in ribos:
            if GPIO.input(ribo[0]) == GPIO.HIGH:
                GPIO.output(ribo[1], GPIO.HIGH)
                litLED = ribo[1]

        for ribo in ribos:
            if ribo[1] != litLED:
                GPIO.output(ribo[1], GPIO.LOW)

finally:
    GPIO.cleanup()
