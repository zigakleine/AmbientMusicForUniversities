import tkinter as tk
from MusicPlayer import MusicPlayer

HEIGHT = 800
WIDTH = 800


class Gui:

    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=HEIGHT, width=WIDTH )
        self.canvas.pack()

        self.frame = tk.Frame(self.root, bg="gray")
        self.frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        self.start_button = tk.Button(self.frame, text="Start", highlightbackground="gray",  command=self.on_start_button_clicked)
        self.start_button.pack()

        self.stop_button = tk.Button(self.frame, text="Stop", highlightbackground="gray", command=self.on_stop_button_clicked)
        self.stop_button.pack()

        slider1 = tk.Scale(self.frame, from_=0, to=42)
        slider1.pack()

        self.root.mainloop()

        self.player = None

    def on_start_button_clicked(self):
        self.player = MusicPlayer()
        self.player.start()

    def on_stop_button_clicked(self):
        self.player.stop()


gui = Gui()