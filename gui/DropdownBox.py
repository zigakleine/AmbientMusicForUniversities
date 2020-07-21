import tkinter as tk
from tkinter import font

class DropdownBox:
    def __init__(self, parent, height, width, title, options_list, command):
        self.parent = parent
        self.height = height
        self.color = "#D3D3D3"
        self.title = title
        self.width = width
        self.options_list = options_list
        self.outer_frame = None
        self.title_frame = None
        self.title_label = None
        self.dropdown_frame = None
        self.dropdown = None
        self.label_font = font.Font(self.parent, family='Helvetica', size=10)
        self.command = command
        self.dropdown_value = tk.StringVar()
        self.num_of_options = len(self.options_list)

    def draw(self):
        self.outer_frame = tk.Frame(self.parent, bg=self.color,  # highlightbackground="black", highlightthickness=1,
                                    height=self.height, width=self.width)

        self.outer_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        self.title_frame = tk.Frame(self.outer_frame, bg=self.color)
        self.title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.3)

        self.title_label = tk.Label(self.title_frame, bg=self.color, text=self.title)
        self.title_label.config(font=self.label_font)
        self.title_label.pack(fill=tk.BOTH, expand=tk.YES)

        self.dropdown_frame = tk.Frame(self.outer_frame, bg=self.color, padx=10)
        self.dropdown_frame.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)

        self.dropdown_frame.update()
        print("num of options: ", self.num_of_options)

        dropdown_frame_height = self.dropdown_frame.winfo_height()
        dropdown_frame_width = self.dropdown_frame.winfo_width()

        self.dropdown = tk.OptionMenu(self.dropdown_frame, self.dropdown_value, *self.options_list, command=self.command)
        self.dropdown.pack()
        self.dropdown.config(bg=self.color)

    def get_button_value(self):
        return self.dropdown_value.get()

    def set_button_value(self, new_dropdown_value):
        self.dropdown_value.set(new_dropdown_value)

