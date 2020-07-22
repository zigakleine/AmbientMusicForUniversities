
class SynthParameters:

    def __init__(self):
        self.preset = 3
        self.delay_feedback = 0.2
        self.delay_mix = 0.3
        self.chorus_speed = 0.2
        self.chorus_depth = 0.2
        self.reverb_liveness = 0.7
        self.reverb_damping = 0.3

    def get_preset(self):
        return self.preset

    def set_preset(self, new_preset):
        self.preset = new_preset

    def get_delay_feedback(self):
        return self.delay_feedback

    def set_delay_feedback(self, new_delay_feedback):
        self.delay_feedback = new_delay_feedback

    def get_delay_mix(self):
        return self.delay_mix

    def set_delay_mix(self, new_delay_mix):
        self.delay_mix = new_delay_mix

    def get_chorus_speed(self):
        return self.chorus_speed

    def set_chorus_speed(self, new_chorus_speed):
        self.chorus_speed = new_chorus_speed

    def get_chorus_depth(self):
        return self.chorus_depth

    def set_chorus_depth(self, new_chorus_depth):
        self.chorus_depth = new_chorus_depth

    def get_reverb_liveness(self):
        return self.reverb_liveness

    def set_reverb_liveness(self, new_reverb_liveness):
        self.reverb_liveness = new_reverb_liveness

    def get_reverb_damping(self):
        return self.reverb_damping

    def set_reverb_damping(self, new_reverb_damping):
        self.reverb_damping = new_reverb_damping

