import tkinter as tk
from tkinter import font

class SliderBox:
    def __init__(self, parent, height, width, title, command, min_range, max_range):
        self.parent = parent
        self.height = height
        self.color = "#D3D3D3"
        self.width = width
        self.title = title
        self.command = command
        self.min_range = min_range
        self.max_range = max_range
        self.outer_frame = None
        self.title_frame = None
        self.title_label = None
        self.slider_frame = None
        self.slider = None
        self.label_font = font.Font(self.parent, family='Helvetica', size=10)

    def draw(self):
        self.outer_frame = tk.Frame(self.parent, bg=self.color,  # highlightbackground="black", highlightthickness=1,
                                    height=self.height, width=self.width)

        self.outer_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        self.title_frame = tk.Frame(self.outer_frame, bg="#D3D3D3")
        self.title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.3)

        self.title_label = tk.Label(self.title_frame, bg=self.color, text=self.title, wraplength=self.width)
        self.title_label.config(font=self.label_font)
        self.title_label.pack(fill=tk.BOTH, expand=tk.YES)

        self.slider_frame = tk.Frame(self.outer_frame, bg=self.color)
        self.slider_frame.place(relx=0, rely=00.3, relwidth=1, relheight=0.7)

        self.slider_frame.update()

        slider_frame_height = self.slider_frame.winfo_height()
        slider_frame_width = self.slider_frame.winfo_width()

        self.slider = tk.Scale(self.slider_frame, from_=self.max_range, to=self.min_range, digits=2,
                               resolution=0.1, background="#D3D3D3", length=0.9*slider_frame_height,
                               width=0.15*slider_frame_width, command=self.command)
        self.slider.pack(side=tk.TOP)

    def get_slider(self):
        return self.slider
