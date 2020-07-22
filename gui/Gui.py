import tkinter as tk
from tkinter import font

from pylibpd import *

from gui.DropdownBox import DropdownBox
from musicPlayer.MusicPlayer import MusicPlayer
from gui.MyFrame import MyFrame
from gui.RadioButtonsBox import RadioButtonsBox
from gui.SliderGroup import SliderGroup
from params.CompositionParameters import CompositionParameters
from params.MusicPlayerParameters import MusicPlayerParameters
from params.SynthParameters import SynthParameters

HEIGHT = 800
WIDTH = 900


class Gui:

    def __init__(self):

        self.player = None
        self.music_player_params = MusicPlayerParameters()
        self.music_composer_params = CompositionParameters()
        self.synth_params = SynthParameters()

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
        self.start_button.place(relx=0.88, rely=0.2, relwidth=0.1, relheight=0.6)

        self.stop_button = tk.Button(self.frame_3, text="Stop", highlightbackground="#D3D3D3",
                                     command=self.on_stop_button_clicked)
        self.stop_button.place(relx=0.76, rely=0.2, relwidth=0.1, relheight=0.6)

        info_label_font = font.Font(self.frame_3, family='Helvetica', size=12)
        self.info_label_text = tk.StringVar()
        self.info_label = tk.Label(self.frame_3, textvariable=self.info_label_text, font=info_label_font, bg="#D3D3D3",
                                   anchor='w')
        self.info_label.place(relx=0.01, rely=0.2, relwidth=0.6, relheight=0.6)


        # Tempo frame

        self.tempo_frame = MyFrame(self.frame_1.get_frame(), "#D3D3D3", "Tempo")
        self.tempo_frame.draw(relx=0.01, rely=0.02, relwidth=0.1, relheight=0.96)

        self.tempo_frame.get_frame().update()
        tempo_frame_height = self.tempo_frame.get_frame().winfo_height()
        tempo_frame_width = self.tempo_frame.get_frame().winfo_width()
        tempo_frame_titles = ["Bpm"]
        tempo_frame_commands = [self.on_tempo_slider_change]
        tempo_frame_ranges = [(50, 200)]
        tempo_frame_initial_values = [self.music_player_params.get_tempo()]

        self.tempo_slider_group = SliderGroup(self.tempo_frame.get_frame(), 1, tempo_frame_height, tempo_frame_width,
                                              tempo_frame_titles, tempo_frame_commands, tempo_frame_ranges, tempo_frame_initial_values)
        self.tempo_slider_group.draw()

        self.tempo_slider_group.get_slider_with_index(0).set(self.music_player_params.get_tempo())

        # Arpeggiator Frame

        self.arpeggiator_frame = MyFrame(self.frame_1.get_frame(), "#D3D3D3", "Arpeggiator")
        self.arpeggiator_frame.draw(relx=0.12, rely=0.02, relwidth=0.25, relheight=0.96)

        self.arpeggiator_frame.get_frame().update()
        arpeggiator_frame_height = self.arpeggiator_frame.get_frame().winfo_height()
        arpeggiator_frame_width = self.arpeggiator_frame.get_frame().winfo_width()


        arpeggiator_types = [("Off", "off"),("Up", "up"),("Down", "down"), ("UpDown", "upDown"), ("Random", "random")]

        self.arpeggiator_type_box = RadioButtonsBox(self.arpeggiator_frame.get_frame(), arpeggiator_frame_height,
                                               (arpeggiator_frame_width / 2), "Arpeggiator type",
                                               arpeggiator_types, self.on_arpeggiator_type_button_change)
        self.arpeggiator_type_box.draw()
        self.arpeggiator_type_box.set_button_value(self.music_player_params.get_arpeggiation_type())


        arpeggiator_speeds = [("1/8", "eighth_note"),("1/4", "quarter_note"),("1/2", "half_note"), ("1", "whole_note")]

        self.arpeggiator_speed_box = RadioButtonsBox(self.arpeggiator_frame.get_frame(), arpeggiator_frame_height,
                                                     (arpeggiator_frame_width / 2), "Arpeggiator speed",
                                                     arpeggiator_speeds, self.on_arpeggiator_speed_button_change)
        self.arpeggiator_speed_box.draw()
        self.arpeggiator_speed_box.set_button_value(self.music_player_params.get_arpeggiation_speed())

        # Synth controls frame

        self.synth_controls_frame = MyFrame(self.frame_1.get_frame(), "#D3D3D3", "Synth controls")
        self.synth_controls_frame.draw(relx=0.38, rely=0.02, relwidth=0.61, relheight=0.96)

        self.synth_controls_frame.get_frame().update()
        synth_controls_frame_height = self.synth_controls_frame.get_frame().winfo_height()
        synth_controls_frame_width = self.synth_controls_frame.get_frame().winfo_width()

        presets = [0, 1, 2, 3, 4, 6, 7, 8]

        self.preset_dropdown_box = DropdownBox(self.synth_controls_frame.get_frame(), synth_controls_frame_height,
                                               (synth_controls_frame_width / 6), "Preset", presets, self.on_preset_dropdown_change)
        self.preset_dropdown_box.draw()
        self.preset_dropdown_box.set_button_value(self.synth_params.get_preset())

        synth_controls_frame_titles = ["Delay feedback", "Delay mix", "Chorus speed", "Chorus depth", "Reverb liveness",
                                       "Reverb damping"]
        synth_controls_frame_commands = [self.on_delay_feedback_slider_change, self.on_delay_mix_slider_change,
                                         self.on_chorus_speed_slider_change, self.on_chorus_depth_slider_change,
                                         self.on_reverb_liveness_slider_change, self.on_reverb_damping_slider_change
                                         ]
        synth_controls_frame_ranges = [(0, 0.7), (0, 1), (0, 0.6), (0, 1), (1, 0.6), (1, 0)]
        synth_controls_frame_initial_values = [self.synth_params.get_delay_feedback(), self.synth_params.get_delay_mix(),
                                               self.synth_params.get_chorus_speed(), self.synth_params.get_chorus_depth(),
                                               self.synth_params.get_reverb_liveness(), self.synth_params.get_reverb_damping()]

        self.synth_controls_slider_group = SliderGroup(self.synth_controls_frame.get_frame(), 6, synth_controls_frame_height, (6/7)*synth_controls_frame_width,
                                                       synth_controls_frame_titles, synth_controls_frame_commands,
                                                       synth_controls_frame_ranges, synth_controls_frame_initial_values)
        self.synth_controls_slider_group.draw()



        # Global composition controls

        self.global_controls_frame = MyFrame(self.frame_2.get_frame(), "#D3D3D3", "Global controls")
        self.global_controls_frame.draw(relx=0.01, rely=0.02, relwidth=0.2, relheight=0.96)

        self.global_controls_frame_top = tk.Frame(self.global_controls_frame.get_frame(), bg="#D3D3D3")
        self.global_controls_frame_top.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.48)

        music_modes = [("Major", "MAJOR"), ("Minor", "MINOR")]
        self.global_controls_frame_top.update()
        global_controls_frame_height = self.global_controls_frame.get_frame().winfo_height()
        global_controls_frame_width = self.global_controls_frame.get_frame().winfo_width()

        self.music_mode_box = RadioButtonsBox(self.global_controls_frame_top, global_controls_frame_height,
                                              (global_controls_frame_width / 2), "Music mode",
                                              music_modes, self.on_music_mode_button_change)
        self.music_mode_box.draw()
        self.music_mode_box.set_button_value(self.music_composer_params.get_mode())

        melody_octaves = [("3", 3), ("4", 4)]

        self.melody_octave_box = RadioButtonsBox(self.global_controls_frame_top, global_controls_frame_height,
                                              (global_controls_frame_width / 2), "Melody octave",
                                              melody_octaves, self.on_melody_octave_button_change)
        self.melody_octave_box.draw()
        self.melody_octave_box.set_button_value(self.music_composer_params.get_melody_octave())

        self.global_controls_frame_bot = tk.Frame(self.global_controls_frame.get_frame(), bg="#D3D3D3")
        self.global_controls_frame_bot.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.48)

        self.global_controls_frame_bot.update()

        part_lengths = [("4 bar", 4), ("8 bar", 8)]

        self.part_length_box = RadioButtonsBox(self.global_controls_frame_bot, global_controls_frame_height,
                                              (global_controls_frame_width / 2), "Part length",
                                              part_lengths, self.on_part_length_button_change)
        self.part_length_box.draw()
        self.part_length_box.set_button_value(self.music_composer_params.get_part_length())

        harmony_octaves = [("1", 1),("2", 2)]

        self.harmony_octaves_box = RadioButtonsBox(self.global_controls_frame_bot, global_controls_frame_height,
                                              (global_controls_frame_width / 2), "Harmony octave",
                                              harmony_octaves, self.on_harmony_octave_button_change)
        self.harmony_octaves_box.draw()
        self.harmony_octaves_box.set_button_value(self.music_composer_params.get_harmony_octave())

        # Harmony controls

        self.harmony_controls_frame = MyFrame(self.frame_2.get_frame(), "#D3D3D3", "Harmony")
        self.harmony_controls_frame.draw(relx=0.22, rely=0.02, relwidth=0.1, relheight=0.96)

        self.harmony_controls_frame.get_frame().update()
        harmony_controls_frame_height = self.harmony_controls_frame.get_frame().winfo_height()
        harmony_controls_frame_width = self.harmony_controls_frame.get_frame().winfo_width()
        harmony_controls_frame_titles = ["Resolution intensity"]
        harmony_controls_frame_commands = [self.on_harmony_resolution_intensity_slider_change]
        harmony_controls_frame_ranges = [(0, 1)]
        harmony_controls_frame_initial_values = [self.music_composer_params.get_harmony_resolution_intensity()]

        self.harmony_controls_slider_group = SliderGroup(self.harmony_controls_frame.get_frame(), 1,
                                                         harmony_controls_frame_height, harmony_controls_frame_width,
                                                         harmony_controls_frame_titles, harmony_controls_frame_commands,
                                                         harmony_controls_frame_ranges, harmony_controls_frame_initial_values)
        self.harmony_controls_slider_group.draw()

        # self.tempo_slider_group.get_slider_with_index(0).set(self.music_player_params.get_tempo())

        # Melody controls

        self.melody_controls_frame = MyFrame(self.frame_2.get_frame(), "#D3D3D3", "Melody controls")
        self.melody_controls_frame.draw(relx=0.33, rely=0.02, relwidth=0.66, relheight=0.96)

        self.melody_controls_frame.get_frame().update()
        melody_controls_frame_height = self.melody_controls_frame.get_frame().winfo_height()
        melody_controls_frame_width = self.melody_controls_frame.get_frame().winfo_width()

        melody_controls_frame_titles = ["Melody to harmony fit", "Note extension amount", "Melody amount", "Average interval",
                                        "Resolution intensity", "Melody range", "Interval consonance"]
        melody_controls_frame_commands = [self.on_melody_to_harmony_fit_slider_change, self.on_note_extension_amount_slider_change,
                                          self.on_melody_amount_slider_change, self.on_average_interval_slider_change,
                                          self.on_resolution_intensity_slider_change, self.on_melody_range_slider_change,
                                          self.on_interval_consonance_slider_change]
        melody_controls_frame_initial_values = [float(self.music_composer_params.get_melody_to_harmony_fit()),
                                                float(self.music_composer_params.get_note_extension_amount()),
                                                float(self.music_composer_params.get_melody_amount()),
                                                float(self.music_composer_params.get_average_interval()),
                                                float(self.music_composer_params.get_resolution_intensity()),
                                                float(self.music_composer_params.get_melody_range()),
                                                float(self.music_composer_params.get_interval_consonance())]
        melody_controls_frame_ranges = [(0.5, 1), (0, 0.9), (0.0, 1.0), (0, 12), (0.0, 1.0), (0, 24), (0.0, 1.0)]

        self.melody_controls_slider_group = SliderGroup(self.melody_controls_frame.get_frame(), 7,
                                                        melody_controls_frame_height, melody_controls_frame_width,
                                                        melody_controls_frame_titles, melody_controls_frame_commands,
                                                        melody_controls_frame_ranges, melody_controls_frame_initial_values)

        self.melody_controls_slider_group.draw()

        print(self.melody_controls_slider_group.slider_boxes)

        #
        # self.melody_controls_slider_group.get_slider_with_index(0).set(
        #     float(self.music_composer_params.get_melody_to_harmony_fit()))
        # self.melody_controls_slider_group.get_slider_with_index(1).set(
        #     float(self.music_composer_params.get_note_extension_amount()))
        # self.melody_controls_slider_group.get_slider_with_index(2).set(
        #     float(self.music_composer_params.get_melody_amount()))
        # self.melody_controls_slider_group.get_slider_with_index(3).set(
        #     float(self.music_composer_params.get_average_interval()))
        # self.melody_controls_slider_group.get_slider_with_index(4).set(
        #     float(self.music_composer_params.get_resolution_intensity()))
        # self.melody_controls_slider_group.get_slider_with_index(5).set(
        #     float(self.music_composer_params.get_melody_range()))
        # self.melody_controls_slider_group.get_slider_with_index(6).set(
        #     float(self.music_composer_params.get_interval_consonance()))

        self.root.mainloop()

    def on_start_button_clicked(self):
        if self.player is None:
            self.player = MusicPlayer(self.music_player_params, self.music_composer_params, self)
            self.player.start()

    def on_stop_button_clicked(self):
        if self.player is not None:
            self.player.stop()
            self.player = None
            self.set_info_text_label("Stopped")

    def on_tempo_slider_change(self, new_tempo):
        self.music_player_params.set_tempo(int(new_tempo))
        libpd_float("tempo", float(new_tempo))

    def on_harmony_resolution_intensity_slider_change(self, new_harmony_resolution_intensity):
        self.music_composer_params.set_harmony_resolution_intensity(new_harmony_resolution_intensity)

    def on_melody_to_harmony_fit_slider_change(self, new_melody_to_harmony_fit):
        self.music_composer_params.set_melody_to_harmony_fit(float(new_melody_to_harmony_fit))

    def on_note_extension_amount_slider_change(self, new_note_extension_amount):
        self.music_composer_params.set_note_extension_amount(float(new_note_extension_amount))

    def on_melody_amount_slider_change(self, new_melody_amount):
        self.music_composer_params.set_melody_amount(float(new_melody_amount))

    def on_average_interval_slider_change(self, new_average_interval):
        self.music_composer_params.set_average_interval(float(new_average_interval))

    def on_resolution_intensity_slider_change(self, new_resolution_intensity):
        self.music_composer_params.set_resolution_intensity(float(new_resolution_intensity))

    def on_melody_range_slider_change(self, new_melody_range):
        self.music_composer_params.set_melody_range(float(new_melody_range))

    def on_interval_consonance_slider_change(self, new_interval_consonance):
        self.music_composer_params.set_interval_consonance(float(new_interval_consonance))

    def get_music_composer_params(self):
        return self.music_composer_params

    def set_music_composer_params(self, new_music_composer_params):
        self.music_composer_params = new_music_composer_params

    def on_arpeggiator_type_button_change(self):
        new_arpeggiator_type = self.arpeggiator_type_box.get_button_value()
        self.music_player_params.set_arpeggiation_type(new_arpeggiator_type)
        print("type: ", self.music_player_params.get_arpeggiation_type())

    def on_arpeggiator_speed_button_change(self):
        new_arpeggiator_speed = self.arpeggiator_speed_box.get_button_value()
        self.music_player_params.set_arpeggiation_speed(new_arpeggiator_speed)
        print("speed: ", self.music_player_params.get_arpeggiation_speed())

    def on_music_mode_button_change(self):
        new_music_mode = self.music_mode_box.get_button_value()
        self.music_composer_params.set_mode(new_music_mode)

    def on_melody_octave_button_change(self):
        new_melody_octave = int(self.melody_octave_box.get_button_value())
        self.music_composer_params.set_melody_octave(new_melody_octave)

    def on_harmony_octave_button_change(self):
        new_harmony_octave = int(self.harmony_octaves_box.get_button_value())
        self.music_composer_params.set_harmony_octave(new_harmony_octave)

    def on_part_length_button_change(self):
        new_part_length = int(self.part_length_box.get_button_value())
        self.music_composer_params.set_part_length(new_part_length)

    def on_preset_dropdown_change(self, new_preset):
        print("new preset: ", new_preset)
        self.synth_params.set_preset(new_preset)
        libpd_float("preset", new_preset)

    def on_delay_feedback_slider_change(self, new_delay_feedback_value):
        self.synth_params.set_delay_feedback(new_delay_feedback_value)
        libpd_float("delay_feedback", float(new_delay_feedback_value))

    def on_delay_mix_slider_change(self, new_delay_mix_value):
        self.synth_params.set_delay_mix(new_delay_mix_value)
        libpd_float("delay_mix", float(new_delay_mix_value))

    def on_chorus_speed_slider_change(self, new_chorus_speed_value):
        self.synth_params.set_chorus_speed(new_chorus_speed_value)
        libpd_float("chorus_speed", float(new_chorus_speed_value))

    def on_chorus_depth_slider_change(self, new_chorus_depth_value):
        self.synth_params.set_chorus_depth(new_chorus_depth_value)
        libpd_float("chorus_depth", float(new_chorus_depth_value))

    def on_reverb_liveness_slider_change(self, new_reverb_liveness_value):
        self.synth_params.set_reverb_liveness(new_reverb_liveness_value)
        libpd_float("reverb_liveness", float(new_reverb_liveness_value))

    def on_reverb_damping_slider_change(self, new_reverb_damping_value):
        self.synth_params.set_reverb_damping(new_reverb_damping_value)
        libpd_float("reverb_damping", float(new_reverb_damping_value))

    def set_initial_synth_parameters(self):
        libpd_float("preset", float(self.synth_params.get_preset()))
        libpd_float("delay_feedback", float(self.synth_params.get_delay_feedback()))
        libpd_float("delay_mix", float(self.synth_params.get_delay_mix()))
        libpd_float("chorus_speed", float(self.synth_params.get_chorus_speed()))
        libpd_float("chorus_depth", float(self.synth_params.get_chorus_depth()))
        libpd_float("reverb_liveness", float(self.synth_params.get_reverb_liveness()))
        libpd_float("reverb_damping", float(self.synth_params.get_reverb_damping()))
        libpd_float("tempo", float(self.music_player_params.get_tempo()))

    def set_info_text_label(self, new_text):
        self.info_label_text.set(new_text)
