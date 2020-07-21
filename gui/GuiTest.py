import tkinter as tk

from gui.MyFrame import MyFrame
from gui.RadioButtonsBox import RadioButtonsBox
from gui.SliderBox import SliderBox
from gui.SliderGroup import SliderGroup

HEIGHT = 700
WIDTH = 700


def on_slider_1_change(new_value):
    print("slider 1: ", new_value)


def on_slider_2_change(new_value):
    print("slider 2: ", new_value)


def on_slider_3_change(new_value):
    print("slider 3: ", new_value)

root = tk.Tk()
root.title("Ambient Music For Universities")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#FFFAFA")
canvas.pack()

frame_1 = MyFrame(root, "#D3D3D3", "Music player parameters")
frame_1.draw(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.41)

frame_2 = MyFrame(root, "#D3D3D3", "Music composition parameters")
frame_2.draw(relx=0.02, rely=0.45, relwidth=0.96, relheight=0.41)

synth_controls_frame = MyFrame(frame_1.get_frame(), "#D3D3D3", "Synth controls")
synth_controls_frame.draw(relx=0.48, rely=0.02, relwidth=0.51, relheight=0.96)

synth_controls_frame.get_frame().update()
print("height: ", synth_controls_frame.get_frame().winfo_height())
print("width: ", synth_controls_frame.get_frame().winfo_width())

synth_controls_frame_height = synth_controls_frame.get_frame().winfo_height()
synth_controls_frame_width = synth_controls_frame.get_frame().winfo_width()
synth_controls_frame_titles = ["slider 1", "slider 2", "slider 3"]
synth_controls_frame_commands = [on_slider_1_change, on_slider_2_change, on_slider_3_change]
synth_controls_frame_ranges = [(0, 1), (0, 1), (0, 1)]

synth_controls_slider_group = SliderGroup(synth_controls_frame.get_frame(), 3, synth_controls_frame_height, synth_controls_frame_width,
                                      synth_controls_frame_titles, synth_controls_frame_commands, synth_controls_frame_ranges)
synth_controls_slider_group.draw()



synth_controls_slider_group.get_slider_with_index(0).set(0.3)
synth_controls_slider_group.get_slider_with_index(1).set(0.3)
synth_controls_slider_group.get_slider_with_index(2).set(0.3)





arpeggiator_frame = MyFrame(frame_1.get_frame(), "#D3D3D3", "Arpeggiator")
arpeggiator_frame.draw(relx=0.12, rely=0.02, relwidth=0.35, relheight=0.96)

arpeggiator_frame.get_frame().update()

print("height: ", arpeggiator_frame.get_frame().winfo_height())
print("width: ", arpeggiator_frame.get_frame().winfo_width())


arpeggiator_types = [("Off", "off"), ("Up", "up"), ("Down", "down"), ("UpDown", "upDown"), ("Random", "random")]
arpeggiator_type_box = RadioButtonsBox(arpeggiator_frame.get_frame(), 220, (237/2), "Arpeggiator types",  arpeggiator_types, None)
arpeggiator_type_box.draw()

root.mainloop()


