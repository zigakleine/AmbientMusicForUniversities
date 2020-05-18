
import mido
import time

from MusicComposer import MusicComposer
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

notes_to_play = set()
notes_to_extend = set()
notes_to_stop_playing = set()
notes_playing = set()

composer = MusicComposer()
song = composer.generate_new_song()

for part in song.get_structure_list():

    chord_progression = part.get_harmony_line()
    melody_line = part.get_melody_line()
    print(part.name)

    for i in range(len(chord_progression)):

        notes_to_play = set()
        notes_to_extend = set()
        notes_to_stop_playing = set()

        modulo_4 = i % 4
        arpeggio_note = 0

        if modulo_4 == 0:
            arpeggio_note = 0
        if modulo_4 == 1:
            arpeggio_note = 1
        if modulo_4 == 2:
            arpeggio_note = 2
        if modulo_4 == 3:
            arpeggio_note = 1

        for note in chord_progression[i].get_notes():
            if note.is_extended:
                notes_to_extend.add(note.get_note_value())
            else:
                notes_to_play.add(note.get_note_value())

        if not melody_line[i].get_note_value() == -1:
            if melody_line[i].is_note_extended():
                notes_to_extend.add(melody_line[i].get_note_value())
            else:
                notes_to_play.add(melody_line[i].get_note_value())

        #notes_to_play.add(chord_progression[i].get_notes()[arpeggio_note].get_note_value())

        notes_to_stop_playing = notes_playing - notes_to_extend
        notes_playing = (notes_to_play | notes_to_extend)

        for note in notes_to_stop_playing:
            out_port.send(mido.Message('note_off', note=note))

        for note in notes_to_play:
            out_port.send(mido.Message('note_on', note=note))

        print("on: ", notes_to_play)
        print("off: ", notes_to_stop_playing)

        time.sleep(0.33)

    for note in notes_playing:
        out_port.send(mido.Message('note_off', note=note))