import random
import re
from composingAlgorithms.ContextFreeGrammarStructure import ContextFreeGrammarStructure


class StructureGenerator:

    structure_production_rules = {

        "<structure>": ["<intro>,<body>", "<body>,<outro>", "<intro>,<body>,<outro>", "<body>"],
        "<intro>": ["A_n", "B_n"],
        "<outro>": ["A_n", "B_n"],
        "<body>": ["<part-one>,<part-two>", "<part-one>,<part-two>,<part-three>"],
        "<part-one>": ["A_m", "A_m,B_m", "A_m,A_m"],
        "<part-two>": ["A_m", "A_m,B_m", "B_m,A_m", "B_m,B_m", "B_m", "C_m,B_m", "A_m,C_m"],
        "<part-three>": ["A_m", "A_m,C_m", "C_m,A_m", "C_m,C_m", "C_m", "C_m,B_m", "B_m,C_m"],

    }

    start_symbol = "<structure>"

    @classmethod
    def generate_structure(cls):
        structure_cfg = ContextFreeGrammarStructure(cls.start_symbol, cls.structure_production_rules)
        generated_structure = structure_cfg.expand()

        return generated_structure
