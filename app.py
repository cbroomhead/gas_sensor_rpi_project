  
from mq135 import *
import sys, time

try:
    print("Press CTRL+C to abort.")
    
    mq = MQ();
    while True:
        perc = mq.MQPercentage()
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("CO: %g ppm, CO2: %g ppm, NH4: %g ppm" % (perc["CO"], perc["CO2"], perc["NH4"]))
        sys.stdout.flush()
        time.sleep(0.1)

except:
    print("\nAbort by user")