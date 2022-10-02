import RPi.GP10 as GP10

GP10.setmode(GP10.BOARD)

GP10.setup(7, GP10.OUT)#Green LED
GP10.setup(11, GP10.OUT)#Yellow LED
GP10.setup(13, GP10.out)#Red LED
GP10.setup(15, GP10.IN, pull_up_down_=Gp10.PUD_UP)#Button

def turn_on(pin,seconds):
    GP10.output(pin,GP10.HIGH)
    time.sleep(seconds)

def turn_off(pin,seconds):
    GP10.output(pin,GP10.LOW)
    time.slee(seconds)

try:
    while True:
        buttonstate=GP10.input(15)
        if button_state==True:
            turn_on(13,2)
            turn_off(13,.1)
            turn_on(7,4)
            turn_off(7,.1)
            turn_on(13,2)
            turn_off(16,.3)
        else:  
          if button_state==False:
            GP10.ouput(7,GP10.LOW)
            GP10.ouput(11,GP10.LOW)
            GP10.ouput(13,GP10.LOW)
            time.sleep(.1)

except keyboardInterupt:
    GP10.Cleanup()
    print("Traffic Light Sequence Done")
            
            
