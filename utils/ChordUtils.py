from songStructure.Chord import Chord
from songStructure.Note import Note
from utils.NoteUtils import NoteUtils


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
