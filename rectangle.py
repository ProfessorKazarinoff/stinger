# rectangle.py

import cv2
import cv2  # Not actually necessary if you just want to create an image.
import numpy as np
height = 500
width = 700
image = np.zeros((height,width,3), np.uint8)
start_point = (5, 5)
end_point = (220, 220)
color = color = (50, 50, 50)
thickness = 2
#image = cv2.rectangle(image, start_point, end_point, color, thickness)
image = cv2.rectangle(image,(384,0),(510,128),(30,50,10),3)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
image = cv2.polylines(image,[pts],False,(200,200,200))
image = cv2.circle(image,(447,63), 63, (0,255,255), -1)
#cv2.FillPoly(image, polys, color, lineType=8, shift=0)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # path  
# path = r'C:\Users\Rajnish\Desktop\geeksforgeeks\geeks.png'
   
# # Reading an image in default mode 
# image = cv2.imread(path) 
   
# # Window name in which image is displayed 
# window_name = 'Image'
  
# # Start coordinate, here (5, 5) 
# # represents the top left corner of rectangle 
# start_point = (5, 5) 
  
# # Ending coordinate, here (220, 220) 
# # represents the bottom right corner of rectangle 
# end_point = (220, 220) 
  
# # Blue color in BGR 
# color = (255, 0, 0) 
  
# # Line thickness of 2 px 
# thickness = 2
  
# # Using cv2.rectangle() method 
# # Draw a rectangle with blue line borders of thickness of 2 px 
# image = cv2.rectangle(image, start_point, end_point, color, thickness) 
  
# # Displaying the image  
# cv2.imshow(window_name, image)
