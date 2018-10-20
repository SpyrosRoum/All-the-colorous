import pyautogui as pag
import win32api
import webcolors
import waiting
import tkinter as tk


waiting.wait(lambda state_left=win32api.GetKeyState(0x01): state_left !=
             win32api.GetKeyState(0x01), sleep_seconds=0.01)

x, y = win32api.GetCursorPos()
rgb = pag.pixel(x, y)

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
            tBtn = self.buttons[f'btn{i}'] = tk.Button(self.master, width=8, bg=tColours[i])
            tBtn.config(command=lambda btn=tBtn: self.on_s_click(btn))
            tBtn.grid(row=1, column=i)
        # Shades
        for i in range(3):
            sBtn = self.buttons[f'btn{i+3}'] = tk.Button(self.master, width=8, bg=sColours[i])
            sBtn.config(command=lambda btn=sBtn: self.on_s_click(btn))
            sBtn.grid(row=2, column=i)

    def on_s_click(self, btn):
        col = btn.cget('bg')
        tk.Canvas(self.master, width=90, height=90, bg=col).grid(row=4, column=0)

        txt = tk.Text(self.master, width=60, height=1, bg='#f0f0f0')
        txt.insert(
            '1.0', f"Rgb value is: {webcolors.hex_to_rgb(col)[0:3]}. The Hex value is: {col}")
        txt['state'] = tk.DISABLED
        txt.grid(row=4, column=1)


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
