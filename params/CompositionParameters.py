class CompositionParameters:

    def __init__(self):

        # melody parameters
        self.melody_to_harmony_fit = 0.8  # 1 -> range: 0-1
        self.note_extension_amount = 0.4  # 2 --> range: 0 - 0.9375
        self.melody_amount = 0.9  # 3 -> range: 0-1
        self.average_interval = 2  # 4 -> range: 0-24
        self.resolution_intensity = 0.8   # 5 -> range 0-1
        self.rhythmic_range = 7  # 6
        self.melody_range = 12  # 7
        self.interval_consonance = 0.6  # 8

        # global parameters
        self.mode = "MAJOR"
        self.part_length = 8
        self.melody_octave = 4
        self.key = "C"
        self.harmony_octave = 2
        self.melody_range_octaves = 2

    # global parameters

    def get_mode(self):
        return self.mode

    def set_mode(self, new_mode):
        self.mode = new_mode

    def get_part_length(self):
        return self.part_length

    def set_part_length(self, new_part_length):
        self.part_length = new_part_length

    def get_melody_octave(self):
        return self.melody_octave

    def set_melody_octave(self, new_melody_octave):
        self.melody_octave = new_melody_octave

    def get_key(self):
        return self.key

    def set_key(self, new_key):
        self.key = new_key

    def get_harmony_octave(self):
        return self.harmony_octave

    def set_harmony_octave(self, new_harmony_octave):
        self.harmony_octave = new_harmony_octave

    def get_melody_range_octaves(self):
        return self.melody_range_octaves

    def set_melody_range_octaves(self, new_melody_range_octaves):
        self.melody_range_octaves = new_melody_range_octaves

    # melody parameters

    # 1
    def get_melody_to_harmony_fit(self):
        return self.melody_to_harmony_fit

    def set_melody_to_harmony_fit(self, new_melody_to_harmony_fit):
        self.melody_to_harmony_fit = new_melody_to_harmony_fit

    def get_melody_amount(self):
        return self.melody_amount

    def set_melody_amount(self, new_melody_amount):
        self.melody_amount = new_melody_amount

    def get_note_extension_amount(self):
        return self.note_extension_amount

    def set_note_extension_amount(self, new_note_extension_amount):
        self.note_extension_amount = new_note_extension_amount


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

    def get_rhythmic_range(self):
        return self.rhythmic_range

    def set_rhythmic_range(self, new_rhythmic_range):
        self.rhythmic_range = new_rhythmic_range

    def get_interval_consonance(self):
        return self.interval_consonance

    def set_interval_consonance(self, new_interval_consonance):
        self.interval_consonance = new_interval_consonance
