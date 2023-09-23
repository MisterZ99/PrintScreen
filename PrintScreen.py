#python3
import pyscreenshot

img = pyscreenshot.grab()
img.show()
img.save("You_Print_Screen.png")
#img = pyscreenshot.grab(bbox=(100,50,300,150)) #subarea
#img.show()