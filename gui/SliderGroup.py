import tkinter as tk

from gui.SliderBox import SliderBox


class SliderGroup:

    def __init__(self, parent, size,  height, width, titles_list, commands_list, ranges_list, initial_values):
        self.parent = parent
        self.size = size
        self.height = height
        self.width = width
        self.titles_list = titles_list
        self.commands_list = commands_list
        self.ranges_list = ranges_list
        self.slider_boxes = []
        self.initial_values = initial_values

    def draw(self):

        for i in range(self.size):
            slider_box = SliderBox(self.parent, self.height, (self.width / self.size), self.titles_list[i],
                                     self.commands_list[i], self.ranges_list[i][0], self.ranges_list[i][1])
            slider_box.draw()
            slider_box.get_slider().set(self.initial_values[i])
            self.slider_boxes.append(slider_box)

    def get_slider_with_index(self, index):
        return self.slider_boxes[index].get_slider()
