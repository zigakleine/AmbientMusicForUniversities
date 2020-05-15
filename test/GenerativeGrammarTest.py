import re
import random


class ContextFreeGrammar:

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


production_rules_1 = {
    "<start>": ["Today is a <adj> day. The sun shines and <animal_noise>."],
    "<adj>": ["beautiful", "nice", "wonderful", "good"],
    "<animal_noise>": ["birds are chirping", "birds are singing", "dogs are barking", "cats are purring"]

}

start_symbol_1 = "<start>"

production_rules_2 = {

    "<S>": ["<S><S>", "()", "(<S>)", "[]", "[<S>]"],

}

start_symbol_2 = "<S>"


production_rules_3 = {

    "<start>": ["<start> C", "<start> D", "<start> E", "<start> F", "<start> G", "<start> A", "<start> B", ""],

}

start_symbol_3 = "<start>"

cfg = ContextFreeGrammar(start_symbol_1, production_rules_1)
print(cfg.expand())

cfg_2 = ContextFreeGrammar(start_symbol_2, production_rules_2)
print(cfg_2.expand())

cfg_3 = ContextFreeGrammar(start_symbol_3, production_rules_3)
print(cfg_3.expand())
