# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
import this
import time
import math
import sys
from datetime import datetime as dt
import greet

def wait (seconds):
    time.sleep(seconds)
    return None

print("Waiting for 3 seconds...")
wait(3)
print("Done waiting!")

#volgende module
def my_sin(x):
    return math.sin(x)

x=3
result=my_sin(x)
print(f"sin(x) = {result}")

#volgende module
def iso_now():
    now=dt.now()
    return now.isoformat(timespec='minutes')
print(iso_now())

#volgende module
def platform():
    return sys.platform
print(platform())

#volgende module
def supergreeting_wrapper(name):
    message = greet.super_greeting(name)
    return message
print(supergreeting_wrapper("Bob"))