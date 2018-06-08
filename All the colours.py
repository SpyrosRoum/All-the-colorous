import pyautogui as pag
import win32api
from tkinter import *
import webcolors
 
'''
def onClick(x, y):
	rgb = pag.pixel(x, y)
	return rgb
'''


state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128


while True:
	a = win32api.GetKeyState(0x01)

	if a != state_left:  # Button state changed
		state_left = a

		x, y = win32api.GetCursorPos()
		rgb = pag.pixel(x, y)

		#rgb = onClick(x, y)
		break

Hex = webcolors.rgb_to_hex(rgb)
#print(rgb, hex, x, y)



window = Tk()
window.title("All the colors")
#window.configure(background='black')
window.geometry('600x300+{}+{}'.format(x+1, y+1))
window.lift()
window.attributes('-topmost',True)
window.after_idle(window.attributes,'-topmost',False)

'''
Label(window, text=(''), font='none 12 bold', bg=Hex). grid(row=1, column=0, sticky='w')

Button(window, text="", width=14, bg=Hex) .grid(row=1, column=0, sticky=W)
'''

Canvas(window, width=90, height=90, bg=Hex).grid(row=1, column=0)#, sticky='w')


text = Text(window, width=60, height=6, bg='#f0f0f0')
text.insert('1.0', 'Rgb value is: {}. The Hex value is: {}'.format(rgb, Hex))
text['state']=DISABLED
text.grid(row=1, column=1)#, sticky='n')


window.mainloop()

