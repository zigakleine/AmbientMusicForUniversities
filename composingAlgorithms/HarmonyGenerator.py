import random
import re

from composingAlgorithms.ContextFreeGrammarHarmony import ContextFreeGrammarHarmony


class HarmonyGenerator:

    harmony_production_rules = {
        "<harmony>": ["<harmony>,I", "<harmony>,II", "<harmony>,III", "<harmony>,IV",
                      "<harmony>,V", "<harmony>,VI",  "I"]
    }

    start_symbol = "<harmony>"

    @classmethod
    def generate_harmony(cls, type_of_progression, length):

        half_of_length = length // 2
        quarter_of_length = length // 4

        harmony_cfg_1 = ContextFreeGrammarHarmony(cls.start_symbol, cls.harmony_production_rules,
                                                  half_of_length, type_of_progression, 1, [])

        generated_structure_1 = harmony_cfg_1.expand()

        harmony_cfg_2 = ContextFreeGrammarHarmony(cls.start_symbol, cls.harmony_production_rules,
                                                  half_of_length, type_of_progression, 2, generated_structure_1)

        generated_structure_2 = harmony_cfg_2.expand()

        if type_of_progression == "PERIOD":
            whole_structure = generated_structure_1 + "," + generated_structure_2
        elif type_of_progression == "SENTENCE":
            generated_structure_1_chords_list = generated_structure_1.split(",")

            new_generated_structure_1 = ""

            for count, chord in enumerate(generated_structure_1_chords_list):
                if count < quarter_of_length:
                    new_generated_structure_1 += chord
                else:
                    new_generated_structure_1 += generated_structure_1_chords_list[count % quarter_of_length]

                if not count == len(generated_structure_1_chords_list)-1:
                    new_generated_structure_1 += ","

            whole_structure = new_generated_structure_1 + "," + generated_structure_2

        return whole_structure


