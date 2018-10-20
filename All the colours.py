import pyautogui as pag
import win32api
import webcolors
import tkinter as tk

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
    sHex = webcolors.rgb_to_hex((rs, gs, bs))
    sColours.append(sHex)

# For Tints (lighter)
tColours = []
for i in (1/2, 1/4, 1/6):
    rt = int(r + ((255 - r) * i))
    gt = int(g + ((255 - g) * i))
    bt = int(b + ((255 - b) * i))
    tHex = webcolors.rgb_to_hex((rt, gt, bt))
    tColours.append(tHex)


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master).grid()
        self.init_window()

    def init_window(self):
        self.master.title('All the colors')

        tk.Canvas(self.master, width=90, height=90, bg=Hex).grid(row=1, column=0)

        txt = tk.Text(self.master, width=60, height=6, bg='#f0f0f0')
        txt.insert('1.0', 'Rgb value is: {}. The Hex value is: {}'.format(rgb, Hex))
        txt['state'] = tk.DISABLED
        txt.grid(row=1, column=1)

        tk.Button(self.master, text='Shades', width=14,
                  command=self.new_window).grid(row=3, column=1)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.title("Shades")
        self.app = ST_Win(self.newWindow)


class ST_Win:
    buttons = {}

    def __init__(self, master):
        self.master = master
        # self.master.geometry('60x30')
        self.frame = tk.Frame(self.master).grid()

        self.Shades_Win()

    def Shades_Win(self):
        self.master.title("Shades")
        # Tints
        for i in range(3):
            btn = self.buttons[f'btn{i}'] = tk.Button(self.master, width=8, bg=tColours[i],
                                                      command=lambda: self.on_s_click('Blue'))
            btn.grid(row=1, column=i)
        # Shades
        for i in range(3):
            btn = self.buttons[f'btn{i+3}'] = tk.Button(self.master, width=8, bg=sColours[i],
                                                        command=lambda: self.on_s_click('Red'))
            btn.grid(row=2, column=i)

        txt = tk.Text(self.master, width=60, height=1, bg='#f0f0f0')
        txt.insert('1.0', f'Rgb value is: rgb. The Hex value is: {tColours[0]}')
        txt['state'] = tk.DISABLED
        txt.grid(row=4, column=1)

    def on_s_click(self, co):
        tk.Canvas(self.master, width=90, height=90, bg=co).grid(row=4, column=0)
        print(self.buttons)


# Create the main window
def main():
    root = tk.Tk()
    root.geometry(f'600x300+{x+1}+{y+1}')
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()

# Canvas(root, width=90, height=90, bg=Hex).grid(row=1, column=0)
#
# Button(root, text='Shades', width=14, command=Shades_win).grid(row=3, column=1)
#
#
# text = Text(root, width=60, height=6, bg='#f0f0f0')
# text.insert('1.0', 'Rgb value is: {}. The Hex value is: {}'.format(rgb, Hex))
# text['state'] = DISABLED
# text.grid(row=1, column=1)
#
#
# root.mainloop()
#
# Label(root, text=(''), font='none 12 bold', bg=Hex). grid(row=1, column=0, sticky='w')
#
# Button(root, text="", width=14, bg=Hex) .grid(row=1, column=0, sticky=W)
