"""
From Genius_um. Under the name of MazeGroup (https://mazegroup.org/)
2024
"""

"""
When you move the window, the blur effect will be delayed because pillow is slow.
"""

# Old Python versions support
try:
    import tkinter as tk
except:
    import Tkinter as tk

from PIL import ImageTk, ImageGrab, ImageFilter

class BlurryBackground():
    def __init__(self):
        self.root = tk.Tk()

        # You can change size values here (can affect the speed of the generation of blur image) :
        width = 400
        height = 400

        self.root.geometry(f"{width}x{height}")
        self.root.overrideredirect(True)
        self.canvas = tk.Canvas(self.root, width=self.root.winfo_width(), height=self.root.winfo_height(), highlightthickness=0, background="red")
        self.canvas.pack(fill="both", expand=True)
        self.screen_img = None
        self.canvas.image = []
        self.root.after(1, self.loop)
        self.root.bind("<ButtonPress-1>", self.start_move)
        self.root.bind("<ButtonRelease-1>", self.stop_move)
        self.root.bind("<B1-Motion>", self.do_move)
        self.root.mainloop()

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        event;...
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.getWindowPos()[0] + deltax
        y = self.getWindowPos()[1] + deltay
        self.root.geometry(f"+{x}+{y}")
        self.root.after(1, self.loop)

    def loop(self):
        img = self.getScreenImage()
        if self.screen_img:
            pass
        self.canvas.create_image(0, 0, anchor="nw", image=img)
        self.canvas.image.append(img)
        
    def getWindowPos(self):
        return (self.root.winfo_x(), self.root.winfo_y())
    
    def getWindowSize(self):
        return (self.root.winfo_width(), self.root.winfo_height())
    
    def getScreenImage(self):
        box = self.getWindowPos() + (self.getWindowPos()[0] + self.getWindowSize()[0], self.getWindowPos()[1] + self.getWindowSize()[1])
        self.root.withdraw()
        img = ImageGrab.grab()
        img = img.crop(box).filter(ImageFilter.GaussianBlur(2))
        self.root.deiconify()
        img = ImageTk.PhotoImage(img)
        return img
    
BlurryBackground()