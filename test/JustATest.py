

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
'''
import random

def a():
    return 1


def b():
    return 2


def c():
    return 3


function_list = [a, b, c]

result = function_list[1]()
print(result)

print(chr(random.randrange(32, 128)))
print(random.uniform(0,0.7))