import tkinter as tk


class MyFrame:

    def __init__(self, parent, color, title_label):
        self.color = color
        self.title_label = title_label
        self.parent = parent

        self.frame_outer = tk.Frame(self.parent)
        self.frame_header = tk.Frame(self.frame_outer, bg=self.color, highlightbackground="black", highlightthickness=1)
        self.frame_title_label = tk.Label(self.frame_header, text=self.title_label, bg=self.color)
        self.frame = tk.Frame(self.frame_outer, bg=self.color, highlightbackground="black", highlightthickness=1)

    def draw(self, relx, rely, relwidth, relheight):
        self.frame_outer.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
        self.frame_header.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        self.frame_title_label.pack(side=tk.LEFT)
        self.frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

    def get_frame(self):
        return self.frame
