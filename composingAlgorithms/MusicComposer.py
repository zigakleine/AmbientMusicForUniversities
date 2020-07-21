import random

from composingAlgorithms.HarmonyGenerator import HarmonyGenerator
from composingAlgorithms.MelodyGenerator import MelodyGenerator
from composingAlgorithms.StructureGenerator import StructureGenerator
from params.CompositionParameters import CompositionParameters
from songStructure.Part import Part
from songStructure.Song import Song

from threading import Thread


class MusicComposer(Thread):

    def __init__(self, composition_parameters):
        Thread.__init__(self)
        self.daemon = True
        self.song = None
        self.composition_parameters = composition_parameters

    def run(self):

        self.song = Song(self.composition_parameters.get_mode(), self.composition_parameters.get_key())

        structure_generator = StructureGenerator()
        structure_string = structure_generator.generate_structure()
        print(structure_string)

        self.song.set_structure_string(structure_string)
        self.song.construct_parts_set()
        parts_set = self.song.get_parts_set()
        parts_dict = dict()
        print("parts set: ", parts_set)

        for part_string in parts_set:

            possible_part_types = ["PERIOD", "SENTENCE"]
            new_part_type = random.choices(possible_part_types, k=1)[0]
            print("new part type: ", new_part_type)
            new_part = Part(new_part_type, self.composition_parameters.get_part_length(), part_string)

            harmony_generator = HarmonyGenerator()
            melody_generator = MelodyGenerator()

            harmony_string = harmony_generator.generate_harmony(new_part.get_type_of_part(), new_part.get_length())

            print("part ", part_string, ": ", harmony_string)

            new_part.set_harmony_string(harmony_string)
            new_part.generate_harmony_from_harmony_string(self.composition_parameters.get_harmony_octave(), self.song.get_mode(), self.song.get_key())

            harmony_parts = dict()
            if new_part.get_type_of_part() == "PERIOD":
                harmony_parts = {
                    "a_harmony": new_part.get_motif_form_harmony(1),
                    "b_harmony": new_part.get_motif_form_harmony(2),
                    "a_harmony_r": new_part.get_motif_form_harmony(3),
                    "b_harmony_e": new_part.get_motif_form_harmony(4)
                }
            elif new_part.get_type_of_part() == "SENTENCE":
                harmony_parts = {
                    "a_harmony": new_part.get_motif_form_harmony(1),
                    "a_harmony_r": new_part.get_motif_form_harmony(2),
                    "a_harmony_e": new_part.get_motif_form_harmony(3),
                    "b_harmony": new_part.get_motif_form_harmony(4),
                }

            generated_melody = melody_generator.generate_melody(
                new_part.get_type_of_part(), new_part.get_length(), harmony_parts,
                self.song.get_key(), self.composition_parameters.get_melody_octave(), self.song.get_mode(), self.composition_parameters)

            new_part.set_melody_line(generated_melody)

            parts_dict[part_string] = new_part

        self.song.set_parts_dict(parts_dict)
        self.song.construct_structure_list()

    def get_generated_song(self):
        return self.song
