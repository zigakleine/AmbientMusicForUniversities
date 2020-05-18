

'''
for i in range(10):
    print(i)

print(len("cucumber"))


from utils.NoteUtils import NoteUtils
from utils.ScaleUtils import ScaleUtils

scale = ScaleUtils.generate_scale_from_key_root_value(65, "MAJOR", 2)

for note in scale:
    print(NoteUtils.get_note_name_from_note_value(note.get_note_value()))


# print(NoteUtils.get_note_name_from_note_value(0))
# print(NoteUtils.get_note_octave_from_note_value(0))

# print(NoteUtils.get_note_value_from_note_name_and_octave("C", -1))


import re
html = "Today is a <adj> day. The sun shines and <animal_noise>."
tags = re.findall(r'<[^>]+>', html)
for a in tags:
    print(a)

import random

choices = ["a", "b", "c"]
weights = [0.2, 0.7, 0.1]

times_picked = [0, 0, 0]

for i in range(100):
    choice = random.choices(choices, weights, k=1)
    # print(choice)
    if choice[0] == "a":
        times_picked[0] += 1
    elif choice[0] == "b":
        times_picked[1] += 1
    else:
        times_picked[2] += 1


print("a: ", times_picked[0])
print("b: ", times_picked[1])
print("c: ", times_picked[2])

import random

def a():
    return 1


def b():
    return 2


def c():
    return 3


function_list = [a, b, c]
another_list = [1,2,3,4,5,6,7,8]

result = function_list[1]()
print(result)

print(chr(random.randrange(32, 128)))
print(random.uniform(0,0.7))

print(another_list[(len(another_list)//4):2*(len(another_list)//4)])

from composingAlgorithms.HarmonyGenerator import HarmonyGenerator
from composingAlgorithms.StructureGenerator import StructureGenerator

StructureGenerator.generate_structure()
HarmonyGenerator.generate_harmony(8)
'''
from composingAlgorithms.HarmonyGenerator import HarmonyGenerator
from composingAlgorithms.MelodyGenerator import MelodyGenerator
from compositionParams.CompositionParameters import CompositionParameters
from songStructure.Part import Part

string = "ahahha"


harmony_generator = HarmonyGenerator()
melody_generator = MelodyGenerator()
part_string = "A"

new_part = Part("PERIOD", 8, part_string)

harmony_string = harmony_generator.generate_harmony(new_part.get_type_of_part(), new_part.get_length())

print("part ", part_string, ": ", harmony_string)

new_part.set_harmony_string(harmony_string)
new_part.generate_harmony_from_harmony_string(1, "MAJOR", 60)



harmony_parts = {
    "a_harmony": new_part.get_motif_form_harmony(1),
    "b_harmony": new_part.get_motif_form_harmony(2),
    "a_harmony_r": new_part.get_motif_form_harmony(3),
    "b_harmony_e": new_part.get_motif_form_harmony(4)
}

generated_melody = melody_generator.generate_melody("PERIOD", 8, harmony_parts, 60, 2, "MAJOR", CompositionParameters())
print(generated_melody)


















