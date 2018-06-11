import pyautogui as pag
import win32api, webcolors
from tkinter import *
import numpy as np

# Get state of mouse
state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128

# Wait for mouse click
while True:
	a = win32api.GetKeyState(0x01)

	if a != state_left:  # Button state changed
		state_left = a

		# Get the x,y of cursor and rgb of pixel on that x,y
		x, y = win32api.GetCursorPos()
		rgb = pag.pixel(x, y)

		break
# Set Hex based on the rgb
Hex = webcolors.rgb_to_hex(rgb)
r, g, b = rgb


# For shades (darker)
sColours = []
for i in (1/2, 1/4, 1/6):
	rs = int(r * i)
	gs = int(g * i)
	bs = int(b * i)
	sHex = webcolors.rgb_to_hex((rs,gs,bs))
	sColours.append(sHex)

# For Tints (lighter)
tColours = []
for i in (1/2, 1/4, 1/6):
	rt = int(r + ((255 - r) * i))
	gt = int(g + ((255 - g) * i))
	bt = int(b + ((255 - b) * i))
	tHex = webcolors.rgb_to_hex((rt,gt,bt))
	tColours.append(tHex)


# Create shades window
def Shades_win():
	Shades_Win = Tk()

	for i in range (0, 3):
		Button(Shades_Win, width = 8, bg=tColours[i]).grid(row=1, column=i)
	for i in range (0, 3):
		Button(Shades_Win, width= 8, bg=sColours[i]).grid(row=2, column=i)

	#Text(Shades_Win, text='You chose ')


# Create the main window
root = Tk()
root.title("All the colors")
root.geometry('600x300+{}+{}'.format(x+1, y+1))
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

Canvas(root, width=90, height=90, bg=Hex).grid(row=1, column=0)

Button(root, text='Shades', width=14, command=Shades_win).grid(row=3, column=1)

text = Text(root, width=60, height=6, bg='#f0f0f0')
text.insert('1.0', 'Rgb value is: {}. The Hex value is: {}'.format(rgb, Hex))
text['state']=DISABLED
text.grid(row=1, column=1)


root.mainloop()


'''
Label(root, text=(''), font='none 12 bold', bg=Hex). grid(row=1, column=0, sticky='w')

Button(root, text="", width=14, bg=Hex) .grid(row=1, column=0, sticky=W)
'''
