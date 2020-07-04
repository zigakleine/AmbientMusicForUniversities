import tkinter as tk
from MusicPlayer import MusicPlayer
from gui.MyFrame import MyFrame
from params.CompositionParameters import CompositionParameters
from params.MusicPlayerParameters import MusicPlayerParameters

HEIGHT = 700
WIDTH = 700


class Gui:

    def __init__(self):

        self.music_player_params = MusicPlayerParameters()
        self.music_composer_params = CompositionParameters()

        self.root = tk.Tk()
        self.root.title("Ambient Music For Universities")
        self.canvas = tk.Canvas(self.root, height=HEIGHT, width=WIDTH, bg="#FFFAFA")
        self.canvas.pack()

        self.frame_1 = MyFrame(self.root, "#D3D3D3", "Music player parameters")
        self.frame_1.draw(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.41)

        self.frame_2 = MyFrame(self.root, "#D3D3D3", "Music composition parameters")
        self.frame_2.draw(relx=0.02, rely=0.45, relwidth=0.96, relheight=0.41)

        self.frame_3 = tk.Frame(self.root, bg="#D3D3D3", highlightbackground="black", highlightthickness=1)
        self.frame_3.place(relx=0.02, rely=0.88, relwidth=0.96, relheight=0.1)

        self.start_button = tk.Button(self.frame_3, text="Start", highlightbackground="#D3D3D3",
                                      command=self.on_start_button_clicked)
        self.start_button.place(relx=0.76, rely=0.2, relwidth=0.1, relheight=0.6)

        self.stop_button = tk.Button(self.frame_3, text="Stop", highlightbackground="#D3D3D3",
                                     command=self.on_stop_button_clicked)
        self.stop_button.place(relx=0.88, rely=0.2, relwidth=0.1, relheight=0.6)


        # Tempo frame

        self.tempo_frame = MyFrame(self.frame_1.get_frame(), "#D3D3D3", "Tempo")
        self.tempo_frame.draw(relx=0.01, rely=0.02, relwidth=0.1, relheight=0.96)

        self.tempo_slider_label = tk.Label(self.tempo_frame.get_frame(), text="Bpm", bg="#D3D3D3", pady=10)
        self.tempo_slider_label.place(relx=0.05, rely=0, relwidth=0.6, relheight=0.2)

        self.tempo_slider = tk.Scale(self.tempo_frame.get_frame(), from_=200, to=50, command=self.on_tempo_slider_change, background="#D3D3D3")
        self.tempo_slider.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.8)
        self.tempo_slider.set(self.music_player_params.get_tempo())

        # Arpeggiator Frame

        self.arpeggiator_frame = MyFrame(self.frame_1.get_frame(), "#D3D3D3", "Arpeggiator")
        self.arpeggiator_frame.draw(relx=0.12, rely=0.02, relwidth=0.35, relheight=0.96)

        self.arpeggiator_type_frame = tk.Frame(self.arpeggiator_frame.get_frame(), bg="#D3D3D3")
        self.arpeggiator_type_frame.place(relx=0.02, rely=0.02, relwidth=0.47, relheight=0.93)

        temp = tk.StringVar()
        temp.set("off")
        arpeggiator_types = [("Off", "off"),("Up", "up"),("Down", "down"), ("UpDown", "upDown"), ("Random", "random")]

        self.arpeggiator_type_frame_label = tk.Label(self.arpeggiator_type_frame, text="Arpeggiator type", bg="#D3D3D3", pady=6).pack(anchor=tk.W, fill=tk.Y)
        for label, value in arpeggiator_types:
            tk.Radiobutton(self.arpeggiator_type_frame, text=label, value=value, variable=temp, bg="#D3D3D3", pady=4).pack(anchor=tk.W, fill=tk.Y)

        self.arpeggiator_speed_frame = tk.Frame(self.arpeggiator_frame.get_frame(), bg="#D3D3D3")
        self.arpeggiator_speed_frame.place(relx=0.51, rely=0.02, relwidth=0.48, relheight=0.93)

        temp2 = tk.StringVar()
        temp2.set("eighth_note")

        arpeggiator_speeds = [("1/8", "eighth_note"),("1/4", "quarter_note"),("1/2", "half_note"), ("1", "whole_note")]

        self.arpeggiator_type_frame_label = tk.Label(self.arpeggiator_speed_frame, text="Arpeggiator speed", bg="#D3D3D3", pady=6).pack(anchor=tk.W, fill=tk.Y)
        for label, value in arpeggiator_speeds:
            tk.Radiobutton(self.arpeggiator_speed_frame, text=label, value=value, variable=temp2, bg="#D3D3D3", pady=4).pack(anchor=tk.W, fill=tk.Y)

        # Synth controls frame

        self.synth_controls_frame = MyFrame(self.frame_1.get_frame(), "#D3D3D3", "Synth controls")
        self.synth_controls_frame.draw(relx=0.48, rely=0.02, relwidth=0.51, relheight=0.96)

        # Global composition controls

        self.global_controls_frame = MyFrame(self.frame_2.get_frame(), "#D3D3D3", "Global controls")
        self.global_controls_frame.draw(relx=0.01, rely=0.02, relwidth=0.2, relheight=0.96)

        # Harmony controls

        self.harmony_controls_frame = MyFrame(self.frame_2.get_frame(), "#D3D3D3", "Harmony")
        self.harmony_controls_frame.draw(relx=0.22, rely=0.02, relwidth=0.1, relheight=0.96)

        # Melody controls

        self.melody_controls_frame = MyFrame(self.frame_2.get_frame(), "#D3D3D3", "Melody controls")
        self.melody_controls_frame.draw(relx=0.33, rely=0.02, relwidth=0.66, relheight=0.96)


        self.melody_to_harmony_fit_label = tk.Label(self.melody_controls_frame.get_frame(),
                                                    text="Melody to harmony fit", bg="#D3D3D3",  wraplength=70)
        self.melody_to_harmony_fit_label.place(relx=0, rely=0, relwidth=0.3, relheight=0.3)

        self.melody_to_harmony_fit_slider = tk.Scale(self.melody_controls_frame.get_frame(), from_=1, to=0, digits=3,
                                                     resolution=0.01, background="#D3D3D3", command=self.on_melody_to_harmony_fit_slider_change)
        self.melody_to_harmony_fit_slider.place(relx=0, rely=0.25, relwidth=0.4, relheight=0.7)
        self.melody_to_harmony_fit_slider.set(self.music_composer_params.get_melody_to_harmony_fit())


        self.note_extension_amount_label = tk.Label(self.melody_controls_frame.get_frame(),
                                                    text="Note extention amount", bg="#D3D3D3",  wraplength=70)
        self.note_extension_amount_label.place(relx=0.25, rely=0, relwidth=0.3, relheight=0.3)

        self.note_extension_amount_slider = tk.Scale(self.melody_controls_frame.get_frame(), from_=0.9, to=0, digits=2,
                                                     resolution=0.01, background="#D3D3D3", length=50, width=10, command=self.on_note_extension_amount_slider_change)
        self.note_extension_amount_slider.place(relx=0.25, rely=0.25, relwidth=0.4, relheight=0.7)
        self.note_extension_amount_slider.set(self.music_composer_params.get_note_extension_amount())


        self.root.mainloop()

        self.player = None

    def on_start_button_clicked(self):
        self.player = MusicPlayer(self.music_player_params, self.music_composer_params, self)
        self.player.start()

    def on_stop_button_clicked(self):
        self.player.stop()

    def on_tempo_slider_change(self, new_tempo):
        self.music_player_params.set_tempo(int(new_tempo))

    def on_melody_to_harmony_fit_slider_change(self, new_melody_to_harmony_fit):
        self.music_composer_params.set_melody_to_harmony_fit(float(new_melody_to_harmony_fit))

    def on_note_extension_amount_slider_change(self, new_note_extension_amount):
        self.music_composer_params.set_note_extension_amount(float(new_note_extension_amount))

    def get_music_composer_params(self):
        return self.music_composer_params

    def set_music_composer_params(self, new_music_composer_params):
        self.music_composer_params = new_music_composer_params


gui = Gui()