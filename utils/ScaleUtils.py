from songStructure.Note import Note

class ScaleUtils:

    major_mode_intervals = [2,2,1,2,2,2,1]
    minor_mode_intervals = [2,1,2,2,1,2,2]

    @classmethod
    def generate_scale_from_key_root_value(cls, key_root_note, mode, number_of_octaves):

        if mode == "MAJOR":
            requested_mode_intervals = cls.major_mode_intervals

        elif mode == "MINOR":
            requested_mode_intervals = cls.minor_mode_intervals

        scale = []

        current_note_value = key_root_note
        scale.append(Note(current_note_value))

        for octave in range(number_of_octaves):

            for interval in requested_mode_intervals:
                current_note_value += interval
                scale.append(Note(current_note_value))

        return scale
