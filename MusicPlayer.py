
import mido
import time

from songStructure.Note import Note
from songStructure.Song import Song
from utils.ChordUtils import ChordUtils

'''
def func():
    print('ran')
    func2()


def func2():
    print('ran2')
    time.sleep(1)
    print('thread 2 done')


x = threading.Thread(target=func, args=())
x.start()
print('tread 1 done')


'''

outputs = mido.get_output_names()
print(outputs)
out_port = mido.open_output(outputs[0])


chord_progression = []
melody_line = []

# a four bar song to test the MusicPlayer implementation
for i in range(4):

    chord_root_value = None
    chord_quality = None

    if i == 0:
        chord_root_value = 36 + 12
        chord_quality = "MAJOR"
    if i == 1:
        chord_root_value = 41 + 12
        chord_quality = "MAJOR"
    if i == 2:
        chord_root_value = 43 + 12
        chord_quality = "MAJOR"
    if i == 3:
        chord_root_value = 45 + 12
        chord_quality = "MINOR"

    for j in range(8):
        is_extended = None
        current_note_value = None

        if j == 0:
            is_extended = False
        else:
            is_extended = True

        modulo_4 = j % 4
        third_interval = None

        if chord_quality == "MAJOR":
            third_interval = 4
        else:
            third_interval = 3

        if modulo_4 == 0:
            current_note_value = chord_root_value + 12
        elif modulo_4 == 1:
            current_note_value = chord_root_value + 12 + third_interval
        elif modulo_4 == 2:
            current_note_value = chord_root_value + 12 + 7
        elif modulo_4 == 3:
            current_note_value = chord_root_value + 12 + third_interval

        chord_progression.append(
            ChordUtils.create_chord_from_root_note_value(chord_root_value, chord_quality, is_extended))
        melody_line.append(Note(current_note_value))


notes_to_play = set()
notes_to_extend = set()
notes_to_stop_playing = set()
notes_playing = set()

for i in range(4):
    for i in range(len(chord_progression)):

        notes_to_play = set()
        notes_to_extend = set()
        notes_to_stop_playing = set()

        if not melody_line[i].get_note_value() == -1:
            if melody_line[i].is_note_extended():
                notes_to_extend.add(melody_line[i].get_note_value())
            else:
                notes_to_play.add(melody_line[i].get_note_value())

        for note in chord_progression[i].get_notes():
            if note.is_note_extended():
                notes_to_extend.add(note.get_note_value())
            else:
                notes_to_play.add(note.get_note_value())

        notes_to_stop_playing = notes_playing - (notes_to_extend | notes_to_play)

        notes_playing = (notes_to_play | notes_to_extend)

        for note in notes_to_stop_playing:
            out_port.send(mido.Message('note_off', note=note))

        for note in notes_to_play:
            out_port.send(mido.Message('note_on', note=note))



        print("on: ", notes_to_play)
        print("off: ", notes_to_stop_playing)


        # msg1 = mido.Message('note_on', note=60)
        # out_port.send(msg1)

        time.sleep(0.33)

    for note in notes_playing:
        out_port.send(mido.Message('note_off', note=note))