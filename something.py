import requests as req

import time

esp = "http://188.169.2.234:6006"

# variables

cleartime = 1
redtime = 5
greentime = 5

#off

def led0off():
    req.get(esp+"/0/off")
    print("0 OFF")

def led1off():
    req.get(esp+"/1/off")
    print("1 OFF")

def led2off():
    req.get(esp+"/2/off")
    print("2 OFF")

def led3off():
    req.get(esp+"/3/off")
    print("3 OFF")

def led4off():
    req.get(esp+"/4/off")
    print("4 OFF")

def led5off():
    req.get(esp+"/5/off")
    print("5 OFF")

def led6off():
    req.get(esp+"/6/off")
    print("6 OFF")

def led0on():
    req.get(esp+"/0/on")
    print("0 ON")

def led1on():
    req.get(esp+"/1/on")
    print("1 ON")

def led2on():
    req.get(esp+"/2/on")
    print("2 ON")

def led3on():
    req.get(esp+"/3/on")
    print("3 ON")

def led4on():
    req.get(esp+"/4/on")
    print("4 ON")

def led5on():
    req.get(esp+"/5/on")
    print("5 ON")

def led6on():
    req.get(esp+"/6/on")
    print("6 ON")

#code starts now

# clear lights

led0off()

time.sleep(cleartime)

led1off()

time.sleep(cleartime)

led2off()

time.sleep(cleartime)

led3off()

time.sleep(cleartime)

led4off()

time.sleep(cleartime)

led5off()

time.sleep(cleartime)

led6off()

time.sleep(cleartime)

# lights

# loop from here

def lights():

# red on

    led6on()
    time.sleep(redtime)

# yellow on

    led5on()
    time.sleep(3.5)

# red & yellow off

    led6off()

    led5off()

# green on & flash

    led4on()
    time.sleep(greentime)

    led4off()
    time.sleep(0.6)

    led4on()
    time.sleep(0.6)

    led4off()
    time.sleep(0.6)

    led4on()
    time.sleep(0.6)

    led4off()
    time.sleep(0.6)

# yellow after flash

    led5on()
    time.sleep(3.5)

    led5off()

    lights()

lights()

# preperations for another

#led4off()
#time.sleep(delay0)

#led5off()
#time.sleep(delay0)

#led6off()
#time.sleep(delay0)
