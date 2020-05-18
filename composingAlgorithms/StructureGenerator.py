import random
import re


class StructureGenerator:

    structure_production_rules = {

        "<structure>": ["<intro><body>", "<body><outro>", "<intro><body><outro>"],
        "<intro>": ["A", "B"],
        "<outro>": ["A", "B"],
        "<body>": ["<part-one><part-two>", "<part-one><part-two><part-three>"],
        "<part-one>": ["A", "AB", "AA"],
        "<part-two>": ["A", "AB", "BA", "BB", "B", "CB", "AC"],
        "<part-three>": ["A", "AC", "CA", "CC", "C", "CB", "BC"],

    }

    start_symbol = "<structure>"

    @classmethod
    def generate_structure(cls):
        structure_cfg = ContextFreeGrammarStructure(cls.start_symbol, cls.structure_production_rules)
        generated_structure = structure_cfg.expand()

        return generated_structure


class ContextFreeGrammarStructure:

    def __init__(self, start_symbol, production_rules):
        self.start_symbol = start_symbol
        self.production_rules = production_rules

    def expand(self):
        return self.expand_rec(self.start_symbol)

    def expand_rec(self, symbol_to_expand):

        possible_productions = self.production_rules[symbol_to_expand]

        possible_productions_weights = [1/len(possible_productions)]*len(possible_productions)

        selected_production = random.choices(possible_productions, possible_productions_weights, k=1)[0]

        non_terminals = re.findall(r'<[^>]+>', selected_production)

        if len(non_terminals) != 0:

            for non_terminal in non_terminals:
                expanded_non_terminal = self.expand_rec(non_terminal)
                selected_production = selected_production.replace(non_terminal, expanded_non_terminal)

        return selected_production
