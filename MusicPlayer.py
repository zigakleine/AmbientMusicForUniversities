from threading import Thread
import mido
import time

from MusicComposer import MusicComposer
from songStructure.Note import Note
from songStructure.Song import Song
from utils.ChordUtils import ChordUtils


class MusicPlayer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.running = True

    def stop(self):
        self.running = False

    def run(self):

        outputs = mido.get_output_names()
        print(outputs)
        out_port = mido.open_output(outputs[0])

        notes_to_play = set()
        notes_to_extend = set()
        notes_to_stop_playing = set()
        notes_playing = set()

        # tule bi mogu passat notr nov objekt s parametri
        starting_song_composer_thread = MusicComposer()
        starting_song_composer_thread.start()
        starting_song_composer_thread.join()

        current_song = starting_song_composer_thread.get_generated_song()

        while self.running:

            next_song_thread = MusicComposer()
            next_song_thread.start()

            for part in current_song.get_structure_list():

                chord_progression = part.get_harmony_line()
                melody_line = part.get_melody_line()
                print(part.name)

                for i in range(len(chord_progression)):

                    notes_to_play = set()
                    notes_to_extend = set()
                    notes_to_stop_playing = set()

                    modulo_8 = i % 8
                    modulo_2 = i % 2
                    arpeggio_note = 0

                    if modulo_8 == 0 or modulo_8 == 1:
                        arpeggio_note = 0
                    if modulo_8 == 2 or modulo_8 == 3:
                        arpeggio_note = 1
                    if modulo_8 == 4 or modulo_8 == 5:
                        arpeggio_note = 2
                    if modulo_8 == 6 or modulo_8 == 7:
                        arpeggio_note = 1
                    '''
                    for note in chord_progression[i].get_notes():
                        if note.is_extended:
                            notes_to_extend.add(note.get_note_value())
                        else:
                            notes_to_play.add(note.get_note_value())
                    '''
                    if not melody_line[i].get_note_value() == -1:
                        if melody_line[i].is_note_extended():
                            notes_to_extend.add(melody_line[i].get_note_value())
                        else:
                            notes_to_play.add(melody_line[i].get_note_value())

                    if modulo_2 == 0:
                        notes_to_play.add(chord_progression[i].get_notes()[arpeggio_note].get_note_value())
                    elif modulo_2 == 1:
                        notes_to_extend.add(chord_progression[i].get_notes()[arpeggio_note].get_note_value())

                    notes_to_stop_playing = notes_playing - notes_to_extend
                    notes_playing = (notes_to_play | notes_to_extend)

                    if self.running:
                        for note in notes_to_stop_playing:
                            out_port.send(mido.Message('note_off', note=note))

                        for note in notes_to_play:
                            out_port.send(mido.Message('note_on', note=note))
                    else:
                        for note in notes_playing:
                            out_port.send(mido.Message('note_off', note=note))

                        return

                    # print("on: ", notes_to_play)
                    # print("off: ", notes_to_stop_playing)

                    time.sleep(0.22)

                for note in notes_playing:
                    out_port.send(mido.Message('note_off', note=note))

            next_song_thread.join()
            current_song = next_song_thread.get_generated_song()



