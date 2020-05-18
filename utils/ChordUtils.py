from songStructure.Chord import Chord
from songStructure.Note import Note
from utils.NoteUtils import NoteUtils
from utils.ScaleUtils import ScaleUtils


class ChordUtils:

    @classmethod
    def create_chord_from_root_note_value(cls, root_note_value, quality, is_extended):

        third_note_value = None

        if quality == "MAJOR":
            third_note_value = root_note_value + 4
        elif quality == "MINOR":
            third_note_value = root_note_value + 3

        fifth_note_value = root_note_value + 7

        root_note = Note(root_note_value)
        root_note.set_note_extended(is_extended)
        third_note = Note(third_note_value)
        third_note.set_note_extended(is_extended)
        fifth_note = Note(fifth_note_value)
        fifth_note.set_note_extended(is_extended)

        chord_notes = [root_note, third_note, fifth_note]

        return Chord(chord_notes)

    @classmethod
    def create_chord_from_name_and_octave(cls, name, octave, quality, is_extended):

        root_note_value = NoteUtils.get_note_value_from_note_name_and_octave(name, octave)

        requested_chord = cls.create_chord_from_root_note_value(root_note_value, quality, is_extended)

        return requested_chord

    @classmethod
    def create_chord_from_roman_numeral(cls, numeral, octave, mode, key_root_note_value, is_extended):
        key_root_note_value_octave = NoteUtils.transpose_note_value_to_octave(key_root_note_value, octave)
        scale = ScaleUtils.generate_scale_from_key_root_value(key_root_note_value_octave, mode, 1)

        chord_root_note_value = -1
        chord_quality = None

        if mode == "MAJOR":
            if numeral == "I":
                chord_root_note_value = key_root_note_value_octave + scale[0].get_note_value()
                chord_quality = "MAJOR"
            elif numeral == "II":
                chord_root_note_value = key_root_note_value_octave + scale[1].get_note_value()
                chord_quality = "MINOR"
            elif numeral == "III":
                chord_root_note_value = key_root_note_value_octave + scale[2].get_note_value()
                chord_quality = "MINOR"
            elif numeral == "IV":
                chord_root_note_value = key_root_note_value_octave + scale[3].get_note_value()
                chord_quality = "MAJOR"
            elif numeral == "V":
                chord_root_note_value = key_root_note_value_octave + scale[4].get_note_value()
                chord_quality = "MAJOR"
            elif numeral == "VI":
                chord_root_note_value = key_root_note_value_octave + scale[5].get_note_value()
                chord_quality = "MINOR"
            elif numeral == "VII":
                chord_root_note_value = key_root_note_value_octave + scale[6].get_note_value()
                chord_quality = "MINOR"
        if mode == "MINOR":
            if numeral == "I":
                chord_root_note_value = key_root_note_value_octave + scale[0].get_note_value()
                chord_quality = "MINOR"
            elif numeral == "II":
                chord_root_note_value = key_root_note_value_octave + scale[1].get_note_value()
                chord_quality = "MINOR"
            elif numeral == "III":
                chord_root_note_value = key_root_note_value_octave + scale[2].get_note_value()
                chord_quality = "MAJOR"
            elif numeral == "IV":
                chord_root_note_value = key_root_note_value_octave + scale[3].get_note_value()
                chord_quality = "MINOR"
            elif numeral == "V":
                chord_root_note_value = key_root_note_value_octave + scale[4].get_note_value()
                chord_quality = "MINOR"
            elif numeral == "VI":
                chord_root_note_value = key_root_note_value_octave + scale[5].get_note_value()
                chord_quality = "MAJOR"
            elif numeral == "VII":
                chord_root_note_value = key_root_note_value_octave + scale[6].get_note_value()
                chord_quality = "MAJOR"

        return cls.create_chord_from_root_note_value(chord_root_note_value, chord_quality, is_extended)
