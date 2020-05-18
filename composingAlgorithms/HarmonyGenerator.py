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
        harmony_cfg = ContextFreeGrammarHarmony(cls.start_symbol, cls.harmony_production_rules, length //2)

        generated_structure = harmony_cfg.expand()
        print(generated_structure)
        whole_structure = generated_structure + "," + generated_structure

        return whole_structure

class ContextFreeGrammarHarmony:

    def __init__(self, start_symbol, production_rules, length):
        self.start_symbol = start_symbol
        self.production_rules = production_rules
        self.length = length

    def expand(self):
        return self.expand_rec(self.start_symbol, None, 0)

    def calculate_production_weights(self, possible_productions, previous_production, current_length):

        if current_length == self.length - 1:
            possible_productions_weights = [0] * (len(possible_productions) - 1)
            possible_productions_weights.append(1)

        elif current_length == 0:

            possible_productions_weights = [1]
            possible_productions_weights += [0] * (len(possible_productions) - 1)
        else:
            possible_productions_weights = [1 / (len(possible_productions) - 1)] * (len(possible_productions) - 1)
            possible_productions_weights.append(0)

        return possible_productions_weights


    def expand_rec(self, symbol_to_expand, previous_production, current_length):

        # print("symbol to expand: ", symbol_to_expand, ", previous_production: ", previous_production, ", length: ", current_length)

        possible_productions = self.production_rules[symbol_to_expand]

        possible_productions_weights = self.calculate_production_weights(possible_productions, previous_production, current_length)

        selected_production = random.choices(possible_productions, possible_productions_weights, k=1)[0]

        non_terminals = re.findall(r'<[^>]+>', selected_production)

        if len(non_terminals) != 0:

            for non_terminal in non_terminals:
                expanded_non_terminal = self.expand_rec(non_terminal, selected_production, current_length + 1)
                selected_production = selected_production.replace(non_terminal, expanded_non_terminal)

        return selected_production
