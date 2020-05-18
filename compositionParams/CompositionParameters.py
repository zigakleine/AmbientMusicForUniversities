class CompositionParameters:

    def __init__(self):

        # melody parameters
        self.melody_to_harmony_fit = 0.9  # 1
        self.average_note_length = 1.5  # 2 --> range: 0-16
        self.melody_to_silence_ratio = 0.9  # 3 -> range: 0-1
        self.average_interval = 2.3  # 4
        self.resolution_intensity = 0  # 5
        self.rhythmic_variation = 0  # 6
        self.rhythmic_range = 0  # 7
        self.note_variation = 0  # 8
        self.note_range = 0  # 9
        self.melody_direction = 0  # 10
        self.interval_dissonance = 0  # 11
        self.strong_beat_emphasis = 0  # 12

        # harmony parameters
        self.harmonic_direction = 0  # 1
        self.resolution_intensity = 0  # 2

    def get_melody_to_silence_ratio(self):
        return self.melody_to_silence_ratio

    def set_melody_to_silence_ratio(self, new_melody_to_silence_ratio):
        self.melody_to_silence_ratio = new_melody_to_silence_ratio

    def get_average_note_length(self):
        return self.average_note_length

    def set_average_note_length(self, new_average_note_length):
        self.average_note_length = new_average_note_length

    def get_melody_to_harmony_fit(self):
        return self.melody_to_harmony_fit

    def set_melody_to_harmony_fit(self, new_melody_to_harmony_fit):
        self.melody_to_harmony_fit = new_melody_to_harmony_fit

    def get_average_interval(self):
        return self.average_interval

    def set_average_interval(self, new_average_interval):
        self.average_interval = new_average_interval
