import request
import time


username = 'eni34310'
password = 'areahello34'

while True:
    out = request.getOutValue()

    timeToSleep = request.vote(username, password, out)

    time.sleep(timeToSleep)
