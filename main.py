import RPi.GPIO as GPIO

import endoplasmic_reticulum as er

try:
    GPIO.setmode(GPIO.BOARD)
    
    ribo0 = er.Ribosome(0, 7, 11, 8, True)
    ribo1 = er.Ribosome(1, 13, 15, 10, True)
    ribo2 = er.Ribosome(2, 19, 21, 33, True)
    ribo3 = er.Ribosome(3, 23, 29, 35, True)

    ribosomes = [ribo0, ribo1, ribo2, ribo3]

    FREE_RIBO_0_PIN = 37
    FREE_RIBO_1_PIN = 8
    FREE_RIBO_2_PIN = 10

    GPIO.setup(FREE_RIBO_0_PIN, GPIO.OUT)
    GPIO.setup(FREE_RIBO_1_PIN, GPIO.OUT)
    GPIO.setup(FREE_RIBO_2_PIN, GPIO.OUT)

    free_ribo_0_state = 0
    free_ribo_1_state = 0
    free_ribo_2_state = 0

    free_ribo_counter = 0
    while True:
        free_ribo_counter += 1
        for ribo in ribosomes:
            ribo.handle_button_press()

        if free_ribo_counter % 5000 == 0:
            if free_ribo_0_state == 0:
                GPIO.output(FREE_RIBO_0_PIN, GPIO.HIGH)
                free_ribo_0_state = 1
            else:
                GPIO.output(FREE_RIBO_0_PIN, GPIO.LOW)
                free_ribo_0_state = 0

        if free_ribo_counter % 7000 == 0:
            if free_ribo_1_state == 0:
                GPIO.output(FREE_RIBO_1_PIN, GPIO.HIGH)
                free_ribo_1_state = 1
            else:
                GPIO.output(FREE_RIBO_1_PIN, GPIO.LOW)
                free_ribo_1_state = 0

        if free_ribo_counter % 10000 == 0:
            if free_ribo_2_state == 0:
                GPIO.output(FREE_RIBO_2_PIN, GPIO.HIGH)
                free_ribo_2_state = 1
            else:
                GPIO.output(FREE_RIBO_2_PIN, GPIO.LOW)
                free_ribo_2_state = 0

finally:
    GPIO.cleanup()
