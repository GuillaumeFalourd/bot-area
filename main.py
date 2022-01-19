from os import read
import request
import time


while True:
    out = request.getOutValue()

    lineSplit = open("log", "r").readline().split(' ')
    
    print("U", lineSplit[0])
    print("P", lineSplit[1])

    timeToSleep = request.vote(lineSplit[0], lineSplit[1], out)

    time.sleep(timeToSleep)
