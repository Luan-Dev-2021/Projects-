#Para esse codigo funciona é necessario ter uma arduino.
#For this code to work it is necessary to have an arduino.


import serial
from pynput.mouse import Button, Controller
import win32api
import win32con
import pyautogui
import pydirectinput
import mouse
import time

mouse1 = Controller()

porta = "COM3" #Essa é a porta aonde esta o conectado o meu arduino               
               #This is the port where my arduino is connected
    
velocidade = 9600
ser = serial.Serial(porta, velocidade)
umon = 0
opcao = 0
pr = 1
while True:
    leitura = ser.read()
    if leitura == b'1': # aperta
        #print(leitura)
        x1,y1 = mouse1.position
        
        
        mouse1.press(Button.left)
        
        pr = 1
        
    if leitura == b'L':
        
        if pr == 1:
            #time.sleep(0.3) #para jogos
            mouse1.release(Button.left)
            pr = 0
        
