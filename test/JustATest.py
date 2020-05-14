

'''
for i in range(10):
    print(i)

print(len("cucumber"))
'''

from utils.NoteUtils import NoteUtils
from utils.ScaleUtils import ScaleUtils

scale = ScaleUtils.generate_scale_from_key_root_value(65, "MAJOR", 2)

for note in scale:
    print(NoteUtils.get_note_name_from_note_value(note.get_note_value()))


# print(NoteUtils.get_note_name_from_note_value(0))
# print(NoteUtils.get_note_octave_from_note_value(0))

# print(NoteUtils.get_note_value_from_note_name_and_octave("C", -1))
