class Note:

    def __init__(self, value):
        self.note_value = value
        self.is_extended = False
        self.is_rest = (self.note_value == -1)

    def get_note_value(self):
        return self.note_value

    def set_note_value(self, new_note_value):
        self.note_value = new_note_value
        self.is_rest = (self.note_value == -1)

    def is_note_extended(self):
        return self.is_extended

    def set_note_extended(self, new_is_extended):
        self.is_extended = new_is_extended

    def is_note_rest(self):
        return self.is_rest
