class NoteUtils:

    # 0 => C
    @classmethod
    def get_note_name_from_note_value(cls, note_value):

        relative_pitch = note_value % 12

        if relative_pitch == 0:
            return "C"
        elif relative_pitch == 1:
            return "C#"
        elif relative_pitch == 2:
            return "D"
        elif relative_pitch == 3:
            return "D#"
        elif relative_pitch == 4:
            return "E"
        elif relative_pitch == 5:
            return "F"
        elif relative_pitch == 6:
            return "F#"
        elif relative_pitch == 7:
            return "G"
        elif relative_pitch == 8:
            return "G#"
        elif relative_pitch == 9:
            return "A"
        elif relative_pitch == 10:
            return "A#"
        elif relative_pitch == 11:
            return "B"

    @classmethod
    def get_note_octave_from_note_value(cls, note_value):

        note_octave = note_value // 12
        return note_octave - 1

    @classmethod
    def get_note_value_from_note_name_and_octave(cls, note_name, note_octave):

        note_base_value = None

        if note_name == "C":
            note_base_value = 0
        elif note_name == "C#":
            note_base_value = 1
        elif note_name == "D":
            note_base_value = 2
        elif note_name == "D#":
            note_base_value = 3
        elif note_name == "E":
            note_base_value = 4
        elif note_name == "F":
            note_base_value = 5
        elif note_name == "F#":
            note_base_value = 6
        elif note_name == "G":
            note_base_value = 7
        elif note_name == "G#":
            note_base_value = 8
        elif note_name == "A":
            note_base_value = 9
        elif note_name == "A#":
            note_base_value = 10
        elif note_name == "B":
            note_base_value = 11

        return note_base_value + (note_octave + 1) * 12



