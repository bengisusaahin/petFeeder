#WifiCommunication
import Servomotor
from socket import 
from time import ctime
import RPi.GPIO as GPIO
from gpiozero import AngularServo
import time
s = AngularServo(17, min_angle=0, max_angle=180,min_pulse_width=0.0006, max_pulse_width=0.0024, frame_width=0.0025, pin_factory=None)
s.angle = 0.0


HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True
        print ('Waiting for connection')
        tcpCliSock,addr = tcpSerSock.accept()
        print ('...connected from ', addr)
        try
                while True
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE)
                        print(str(data.decode(utf-8)))
                        print(type(data.decode(utf-8)))
                        data=data.decode(utf-8)
                        if not data
                                break
                        if data == Up
                                if(s.angle180)
                                        s.angle += 90.0
                                        print(Increase +str(s.angle))
                        if data == Down
                                if(s.angle0)
                                        s.angle -= 90.0
                                        print(Decrease ,str(s.angle))
        except KeyboardInterrupt
                Servomotor.close()
                GPIO.cleanup()
tcpSerSock.close();

