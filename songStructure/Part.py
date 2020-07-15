import random

from utils.ChordUtils import ChordUtils
from utils.NoteUtils import NoteUtils


class Part:

    def __init__(self, type_of_part, length, name):

        self.type_of_part = type_of_part
        self.harmony_line = None
        self.melody_line = None
        self.length = length
        self.harmony_string = ""
        self.is_intro_or_outro = False
        self.name = name
        self.random_arpeggiation_sequence = [random.randint(0, 2) for i in range(8)]

    def get_harmony_string(self):
        return self.harmony_string

    def set_harmony_string(self, new_harmony_string):
        self.harmony_string = new_harmony_string

    def generate_harmony_from_harmony_string(self, octave, mode, key):

        chords_list = self.harmony_string.split(",")
        self.harmony_line = []

        for chord_numeral in chords_list:

            for i in range(8):

                is_extended = None
                if i == 0:
                    is_extended = False
                else:
                    is_extended = True

                key_root_note_value = NoteUtils.get_note_value_from_note_name_and_octave(key, octave)

                chord_object = ChordUtils.create_chord_from_roman_numeral(chord_numeral, octave,
                                                                          mode, key_root_note_value, is_extended)
                self.harmony_line.append(chord_object)


    def get_motif_form_melody(self, number):
        if number <= 4:
            quarter_length = (self.length // 4) * 8
            return self.melody_line[((number - 1)*quarter_length):(number * quarter_length)]
        else:
            return None

    def set_motif_form_melody(self, new_melody_part, number):
        if number <= 4:
            quarter_length = (self.length // 4) * 8
            self.melody_line[((number - 1)*quarter_length):(number * quarter_length)] = new_melody_part

    def get_motif_form_harmony(self, number):
        if number <= 4:
            quarter_length = (self.length // 4) * 8
            return self.harmony_line[((number - 1)*quarter_length):(number * quarter_length)]
        else:
            return None

    def set_motif_form_harmony(self, new_harmony_part, number):
        if number <= 4:
            quarter_length = (self.length // 4) * 8
            self.harmony_line[((number - 1)*quarter_length):(number * quarter_length)] = new_harmony_part

    def get_phrase_melody(self, number):
        if number <= 2:
            half_length = (self.length // 2) * 8
            return self.melody_line[((number - 1)*half_length):(number * half_length)]
        else:
            return None

    def set_phrase_melody(self, new_melody_part, number):
        if number <= 2:
            half_length = (self.length // 2) * 8
            self.melody_line[((number - 1)*half_length):(number * half_length)] = new_melody_part

    def get_phrase_harmony(self, number):
        if number <= 2:
            half_length = (self.length // 2) * 8
            return self.harmony_line[((number - 1)*half_length):(number * half_length)]
        else:
            return None

    def set_phrase_harmony(self, new_harmony_part, number):
        if number <= 2:
            half_length = (self.length // 2) * 8
            self.harmony_line[((number - 1)*half_length):(number * half_length)] = new_harmony_part

    def get_length(self):
        return self.length

    def get_harmony_line(self):
        return self.harmony_line

    def get_melody_line(self):
        return self.melody_line

    def set_melody_line(self, new_melody_line):
        self.melody_line = new_melody_line

    def get_type_of_part(self):
        return self.type_of_part

    def set_is_intro_or_outro(self, is_intro_outro):
        self.is_intro_or_outro = is_intro_outro

    def is_intro_outro(self):
        return self.is_intro_or_outro

    def get_random_arpeggiation_sequence(self):
        return self.random_arpeggiation_sequence