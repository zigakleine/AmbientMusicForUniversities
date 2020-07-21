import tkinter as tk
from tkinter import font

class RadioButtonsBox:
    def __init__(self, parent, height, width, title, labels_and_values, command):
        self.parent = parent
        self.height = height
        self.color = "#D3D3D3"
        self.title = title
        self.width = width
        self.labels_and_values = labels_and_values
        self.outer_frame = None
        self.title_frame = None
        self.title_label = None
        self.buttons_frame = None
        self.label_font = font.Font(self.parent, family='Helvetica', size=10)
        self.command = command
        self.button_value = tk.StringVar()
        self.num_of_options = len(self.labels_and_values)

    def draw(self):
        self.outer_frame = tk.Frame(self.parent, bg=self.color,  # highlightbackground="black", highlightthickness=1,
                                    height=self.height, width=self.width)

        self.outer_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        self.title_frame = tk.Frame(self.outer_frame, bg="#D3D3D3")
        self.title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.3)

        self.title_label = tk.Label(self.title_frame, bg=self.color, text=self.title)
        self.title_label.config(font=self.label_font)
        self.title_label.pack(fill=tk.BOTH, expand=tk.YES)

        self.buttons_frame = tk.Frame(self.outer_frame, bg=self.color, padx=10)
        self.buttons_frame.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)

        self.buttons_frame.update()
        print("num of options: ", self.num_of_options)

        buttons_frame_height = self.buttons_frame.winfo_height()
        buttons_frame_width = self.buttons_frame.winfo_width()

        for label, value in self.labels_and_values:
            tk.Radiobutton(self.buttons_frame, text=label, value=value, variable=self.button_value,
                           bg="#D3D3D3", command=self.command, pady=3, font=self.label_font, wraplength=self.width, height=2).pack(anchor=tk.W, fill=tk.Y)
            #  width=int(buttons_frame_width),
            #                            height=int(buttons_frame_height/self.num_of_options)

    def get_button_value(self):
        return self.button_value.get()

    def set_button_value(self, new_button_value):
        self.button_value.set(new_button_value)

