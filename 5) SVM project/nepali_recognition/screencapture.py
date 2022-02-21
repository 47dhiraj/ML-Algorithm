import pyscreenshot as ImageGrab         # Note : for installing pyscreenshot => pip install pyscreenshot
import time

images_folder = "test_images/"

for i in range (0,45):
	
	time.sleep(7)
	im = ImageGrab.grab(bbox=(50, 80, 240, 285)) # X1= left,Y1= top,X2= right,Y2= bottom
	print("saved....",i)
	im.save(images_folder+str(i)+'.png')
	print("clear screen now and redraw now...")
	