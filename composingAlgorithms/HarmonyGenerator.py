import random
import re


class HarmonyGenerator:

    harmony_production_rules = {
        "<harmony>": ["<harmony>,I", "<harmony>,II", "<harmony>,III", "<harmony>,IV",
                      "<harmony>,V", "<harmony>,VI",  "I"]
    }

    start_symbol = "<harmony>"

    @classmethod
    def generate_harmony(cls, type_of_progression, length):

        half_of_length = length // 2

        harmony_cfg_1 = ContextFreeGrammarHarmony(cls.start_symbol, cls.harmony_production_rules,
                                                  half_of_length, type_of_progression, 1, [])

        generated_structure_1 = harmony_cfg_1.expand()

        harmony_cfg_2 = ContextFreeGrammarHarmony(cls.start_symbol, cls.harmony_production_rules,
                                                  half_of_length, type_of_progression, 2, generated_structure_1)

        generated_structure_2 = harmony_cfg_2.expand()

        whole_structure = generated_structure_1 + "," + generated_structure_2

        return whole_structure

class ContextFreeGrammarHarmony:

    def __init__(self, start_symbol, production_rules, length, type_of_progression, phrase_num, previous_progression):
        self.start_symbol = start_symbol
        self.production_rules = production_rules
        self.length = length
        self.type_of_progression = type_of_progression
        self.phrase_num = phrase_num
        self.previous_progression = previous_progression
        self.progression_weights_major = {
            #     I     II      III     IV      V       VI
            "0": [60,   10,     10,     30,     80,     10],
            "1": [10,   60,     10,     30,     10,     60],
            "2": [10,   10,     60,     10,     10,     30],
            "3": [60,   30,     30,     60,     30,     30],
            "4": [60,   60,     10,     60,     60,     60],
            "5": [30,   30,     60,     10,     30,     60],
        }

    def calculate_production_weights_period(self, possible_productions, previous_production, current_length):

        possible_productions_weights = [0] * 7
        if previous_production is None:
            if self.phrase_num == 1:
                # preceded by II, IV, V
                # less often preceded by I, III, VI
                possible_productions_weights[0] = 20  # I
                possible_productions_weights[1] = 30  # II
                possible_productions_weights[2] = 20  # III
                possible_productions_weights[3] = 80  # IV
                possible_productions_weights[4] = 100  # V
                possible_productions_weights[5] = 20  # VI

            elif self.phrase_num == 2:
                possible_productions_weights = [1] + [0] * 5 + [0]

        else:
            previous_production_index = possible_productions.index(previous_production)
            for i in range(6):
                possible_productions_weights[i] = self.progression_weights_major[str(previous_production_index)][i]

        if current_length >= self.length // 2 and self.phrase_num == 2:

            production_index = self.get_production_number_from_previous_progression(self.length - current_length)
            possible_productions_weights = [0] * 7
            possible_productions_weights[production_index] = 1

        if current_length == self.length - 1:
            possible_productions_weights = [0] * 6 + [1] * 1

        return possible_productions_weights

    def expand(self):
        return self.expand_rec(self.start_symbol, None, 0)

    def expand_rec(self, symbol_to_expand, previous_production, current_length):

        possible_productions = self.production_rules[symbol_to_expand]

        possible_productions_weights = self.calculate_production_weights_period(possible_productions, previous_production, current_length)

        selected_production = random.choices(possible_productions, possible_productions_weights, k=1)[0]

        non_terminals = re.findall(r'<[^>]+>', selected_production)

        if len(non_terminals) != 0:

            for non_terminal in non_terminals:
                expanded_non_terminal = self.expand_rec(non_terminal, selected_production, current_length + 1)
                selected_production = selected_production.replace(non_terminal, expanded_non_terminal)

        return selected_production

    def get_production_number_from_previous_progression(self, number):
        index = number - 1
        previous_progression_list = self.previous_progression.split(",")

        numeral = previous_progression_list[index]

        production_number = -1

        if numeral == "I":
            production_number = 0
        elif numeral == "II":
            production_number = 1
        elif numeral == "III":
            production_number = 2
        elif numeral == "IV":
            production_number = 3
        elif numeral == "V":
            production_number = 4
        elif numeral == "VI":
            production_number = 5

        return production_number
