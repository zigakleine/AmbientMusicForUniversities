class Chord:

    def __init__(self, notes):
        self.quality = None
        self.notes = notes

        if notes[1].get_note_value() - notes[0].get_note_value() == 3:
            self.quality = "MINOR"
        elif notes[1].get_note_value() - notes[0].get_note_value() == 4:
            self.quality = "MAJOR"

        self.root_note = notes[0]
        self.third_note = notes[1]
        self.fifth_note = notes[2]

    def get_root_note_value(self):
        return self.root_note.get_note_value()

    def get_third_note_value(self):
        return self.third_note.get_note_value()

    def get_fifth_note_value(self):
        return self.fifth_note.get_note_value()

    def get_quality(self):
        return self.quality

    def get_notes(self):
        return self.notes
