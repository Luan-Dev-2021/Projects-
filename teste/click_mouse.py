import serial
from pynput.mouse import Button, Controller
import win32api
import win32con
import pyautogui
import pydirectinput
#import pywinauto
import mouse
import time
mouse1 = Controller()

porta = "COM3"
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
        #print(x1,y1)
        #mouse.position = (x1, y1)
        #mouse.click(Button.left)
        #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1, y1, 0, 0)
        #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x1, y1, 0, 0)
        #pyautogui.click(button='left')
        #pyautogui.click(clicks=2)
        #pyautogui.click(button='left', interval=0.25)
        #mouse1.click('left')
        #pywinauto.mouse.click(button='left', coords=(x1, y1))
        
        mouse1.press(Button.left)
        #mouse1.release(Button.left)
        #pydirectinput.click()
        pr = 1
        
    if leitura == b'L':
        
        if pr == 1:
            #time.sleep(0.3) #para jogos
            
            mouse1.release(Button.left)
            pr = 0
        
