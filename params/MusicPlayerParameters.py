class MusicPlayerParameters:

    def __init__(self):
        self.tempo = 90
        self.arpeggiation_type = "random"
        self.arpeggiation_speed = "quarter_note"

    def get_tempo(self):
        return self.tempo

    def set_tempo(self, new_tempo):
        self.tempo = new_tempo

    def get_arpeggiation_type(self):
        return self.arpeggiation_type

    def set_arpeggiation_type(self, new_arpeggiation_type):
        self.arpeggiation_type = new_arpeggiation_type

    def get_arpeggiation_speed(self):
        return self.arpeggiation_speed

    def set_arpeggiation_speed(self, new_arpeggiation_speed):
        self.arpeggiation_speed = new_arpeggiation_speed