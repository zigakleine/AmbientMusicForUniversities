class CompositionParameters:

    def __init__(self):

        # melody parameters
        self.melody_to_harmony_fit = 0.8  # 1 -> range: 0-1
        self.note_extension_amount = 0.4  # 2 --> range: 0 - 0.9375
        self.melody_amount = 0.9  # 3 -> range: 0-1
        self.average_interval = 2  # 4 -> range: 0-24
        self.resolution_intensity = 0.8   # 5 -> range 0-1
        self.rhythmic_variation = 0  # 6
        self.rhythmic_range = 0  # 7
        self.note_variation = 0  # 8
        self.melody_range = 12  # 9
        self.melody_direction = 0  # 10
        self.interval_dissonance = 0  # 11
        self.strong_beat_emphasis = 0  # 12

        # harmony parameters
        self.harmonic_direction = 0  # 1
        self.resolution_intensity_harmony = 0  # 2

    def get_melody_amount(self):
        return self.melody_amount

    def set_melody_amount(self, new_melody_amount):
        self.melody_amount = new_melody_amount

    def get_note_extension_amount(self):
        return self.note_extension_amount

    def set_note_extension_amount(self, new_note_extension_amount):
        self.note_extension_amount = new_note_extension_amount

    def get_melody_to_harmony_fit(self):
        return self.melody_to_harmony_fit

    def set_melody_to_harmony_fit(self, new_melody_to_harmony_fit):
        self.melody_to_harmony_fit = new_melody_to_harmony_fit

    def get_average_interval(self):
        return self.average_interval

    def set_average_interval(self, new_average_interval):
        self.average_interval = new_average_interval

    def get_resolution_intensity(self):
        return self.resolution_intensity

    def set_resolution_intensity(self, new_resolution_intensity):
        self.resolution_intensity = new_resolution_intensity

    def get_melody_range(self):
        return self.melody_range

    def set_melody_range(self, new_melody_range):
        self.melody_range = new_melody_range

