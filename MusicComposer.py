from composingAlgorithms.HarmonyGenerator import HarmonyGenerator
from composingAlgorithms.MelodyGenerator import MelodyGenerator
from composingAlgorithms.StructureGenerator import StructureGenerator
from compositionParams.CompositionParameters import CompositionParameters
from songStructure.Part import Part
from songStructure.Song import Song


class MusicComposer:

    possible_part_lengths = [8]
    possible_part_types = ["PERIOD"]

    def __init__(self):
        self.song = None

    def generate_new_song(self):

        self.song = Song(60, "MAJOR", 120)

        structure_generator = StructureGenerator()
        structure_string = structure_generator.generate_structure()
        print(structure_string)

        self.song.set_structure_string(structure_string)
        self.song.construct_parts_set()
        parts_set = self.song.get_parts_set()
        parts_dict = dict()
        print("parts set: ", parts_set)
        for part_string in parts_set:
            new_part = Part("PERIOD", 8, part_string)

            harmony_generator = HarmonyGenerator()
            melody_generator = MelodyGenerator()

            harmony_string = harmony_generator.generate_harmony(new_part.get_type_of_part(), new_part.get_length())

            print("part ", part_string, ": ", harmony_string)

            new_part.set_harmony_string(harmony_string)
            new_part.generate_harmony_from_harmony_string(2, self.song.get_mode(), self.song.get_key_root_note_value())

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
                "PERIOD", new_part.get_length(), harmony_parts,
                self.song.get_key_root_note_value(), 4, self.song.get_mode(), CompositionParameters())

            new_part.set_melody_line(generated_melody)

            parts_dict[part_string] = new_part

        self.song.set_parts_dict(parts_dict)
        self.song.construct_structure_list()

        return self.song

    def clear_current_song(self):
        self.song = None
