import webbrowser
import serial
import argparse
import time

parser = argparse.ArgumentParser()z
parser.add_argument("--port")
args = parser.parse_args()
print(args.port)
ser = serial.Serial(args.port, '9600')
isRead = False
timer = time.time()

while True:
    if (time.time() - timer) > 5:
        isRead = False
    
    message = ser.read().decode("utf-8")
    if message == '1' and not isRead:
        isRead = True
        timer = time.time()
        print(message)
        webbrowser.open("https://tvtc.gov.sa")
    elif message == '2' and not isRead:
        isRead = True
        timer = time.time()
        print(message)
        webbrowser.open("https://www.google.com")
    elif message == '3' and not isRead:
        isRead = True
        timer = time.time()
        print(message)
        webbrowser.open("https://www.twitter.com")
    else:
        print('Not defined command')