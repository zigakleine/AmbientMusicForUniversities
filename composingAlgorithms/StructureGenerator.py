import random
import re
from composingAlgorithms.ContextFreeGrammarStructure import ContextFreeGrammarStructure


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
