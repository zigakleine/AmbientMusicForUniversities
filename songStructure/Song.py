class Song():
    def __init__(self, parts, key_root_note, mode, tempo):

        self.parts = parts
        self.key_root_note = key_root_note
        self.mode = mode
        self.tempo = tempo

    # parts getter & setter
    def get_parts(self):
        return self.parts

    def set_parts(self, new_parts):
        self.parts = new_parts

    # key_root_note getter & setter
    def get_key_root_note(self):
        return self.key_root_note

    def set_key_root_note(self, new_key_root_note):
        self.key_root_note = new_key_root_note

    # mode getter & setter
    def get_mode(self):
        return self.mode

    def set_mode(self, new_mode):
        self.mode = new_mode

    # tempo getter & setter
    def get_tempo(self):
        return self.tempo

    def set_tempo(self, new_tempo):
        self.tempo = new_tempo
