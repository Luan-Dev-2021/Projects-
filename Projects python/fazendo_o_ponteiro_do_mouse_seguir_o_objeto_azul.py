import numpy as np 
import cv2
import mouse
import pydirectinput


webcam = cv2.VideoCapture(0) 

while True: 

    _, imageFrame = webcam.read()
    imageFrame=cv2.flip(imageFrame,2);
    imageFrame=cv2.resize(imageFrame,(1366, 708))#1366, 708 Esses valores tem que ser alterados de acordo com o monitor do usuario, para obter o bom funcionamento do codigo.
  
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 
 
    blue_lower = np.array([94, 80, 2], np.uint8) 
    blue_upper = np.array([120, 255, 255], np.uint8) 
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
   
    kernal = np.ones((5, 5), "uint8") 

    blue_mask = cv2.dilate(blue_mask, kernal) 
    res_blue = cv2.bitwise_and(imageFrame, imageFrame, 
                               mask = blue_mask) 
                               
    contours, hierarchy = cv2.findContours(blue_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour)
        
        if(area > 1060):
            x, y, w, h = cv2.boundingRect(contour)
            xu = x + w -67
            x1= xu #* 2
            #yu = y + h - 197
            #yu = y + h -205
            yu = y + h
            
            y1=yu #* 2
           
            pydirectinput.moveTo(x1, y1)#funciona nos jogos
            #print(x1,y1
            
            imageFrame =cv2.line(imageFrame, (0, 0), (x1, y1),(255, 0, 0),1)
                       
              
    
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    #cv2.imshow("mascarar_Azul", blue_mask)
    if	cv2.waitKey(1)==27:								
        break
    
webcam.release() ;
cv2.destroyAllWindows();
