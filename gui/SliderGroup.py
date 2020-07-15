import tkinter as tk

from gui.SliderBox import SliderBox


class SliderGroup:

    def __init__(self, parent, size,  height, width, titles_list, commands_list, ranges_list):
        self.parent = parent
        self.size = size
        self.height = height
        self.width = width
        self.titles_list = titles_list
        self.commands_list = commands_list
        self.ranges_list = ranges_list
        self.slider_boxes = []

    def draw(self):

        for i in range(self.size):
            slider_box = SliderBox(self.parent, self.height, (self.width / self.size), self.titles_list[i],
                                     self.commands_list[i], self.ranges_list[i][0], self.ranges_list[i][1])
            slider_box.draw()
            self.slider_boxes.append(slider_box)

    def get_slider(self, index):
        return self.slider_boxes[index].get_slider()
