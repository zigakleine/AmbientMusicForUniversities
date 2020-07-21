from threading import Thread
import mido
import time
import copy

from composingAlgorithms.MusicComposer import MusicComposer
from audioEngine.AudioEngine import AudioEngine
from utils.TempoUtils import TempoUtils


class MusicPlayer(Thread):
    def __init__(self, music_player_params, music_composer_params, gui):
        Thread.__init__(self)
        self.daemon = True
        self.running = True
        self.music_player_params = music_player_params
        self.music_composer_params = music_composer_params
        self.gui = gui

    def stop(self):
        self.running = False

    def run(self):

        a = AudioEngine()
        a.start()

        self.gui.set_initial_synth_parameters()


        outputs = mido.get_output_names()
        print(outputs)
        out_port = mido.open_output(outputs[0])

        notes_to_play = set()
        notes_to_extend = set()
        notes_to_stop_playing = set()
        notes_playing = set()

        self.music_composer_params = self.gui.get_music_composer_params()
        starting_song_composer_thread = MusicComposer(copy.copy(self.music_composer_params))
        starting_song_composer_thread.start()
        starting_song_composer_thread.join()

        current_song = starting_song_composer_thread.get_generated_song()

        while self.running:

            self.music_composer_params = self.gui.get_music_composer_params()
            next_song_thread = MusicComposer(copy.copy(self.music_composer_params))
            next_song_thread.start()

            for part in current_song.get_structure_list():



                chord_progression = part.get_harmony_line()
                melody_line = part.get_melody_line()
                print(part.name)

                current_arpeggio_note_index = 0
                tick_counter = 0

                for i in range(len(chord_progression)):

                    notes_to_play = set()
                    notes_to_extend = set()
                    notes_to_stop_playing = set()

                    if self.music_player_params.get_arpeggiation_type() == "off":
                        # full chords playing
                        for note in chord_progression[i].get_notes():
                            if note.is_extended:
                                notes_to_extend.add(note.get_note_value())
                            else:
                                notes_to_play.add(note.get_note_value())

                    else:

                        note_length = None
                        if self.music_player_params.get_arpeggiation_speed() == "eighth_note":
                             note_length = 1
                        elif self.music_player_params.get_arpeggiation_speed() == "quarter_note":
                            note_length = 2
                        elif self.music_player_params.get_arpeggiation_speed() == "half_note":
                            note_length = 4
                        elif self.music_player_params.get_arpeggiation_speed() == "whole_note":
                            note_length = 8

                        arpeggio_notes = None
                        if self.music_player_params.arpeggiation_type == "up":
                            arpeggio_notes = [0, 1, 2, 0]
                        elif self.music_player_params.arpeggiation_type == "down":
                            arpeggio_notes = [2, 1, 0, 2]
                        elif self.music_player_params.arpeggiation_type == "downUp":
                            arpeggio_notes = [2, 1, 0, 1]
                        elif self.music_player_params.arpeggiation_type == "upDown":
                            arpeggio_notes = [0, 1, 2, 1]
                        elif self.music_player_params.arpeggiation_type == "random":
                            arpeggio_notes = part.get_random_arpeggiation_sequence()

                        if tick_counter % note_length == 0:
                            current_arpeggio_note_index += 1
                            current_arpeggio_note_index = current_arpeggio_note_index % len(arpeggio_notes)

                            notes_to_play.add(chord_progression[i].get_notes()[arpeggio_notes[current_arpeggio_note_index]].get_note_value())
                        else:
                            notes_to_extend.add(
                                chord_progression[i].get_notes()[arpeggio_notes[current_arpeggio_note_index]].get_note_value())


                    if not melody_line[i].get_note_value() == -1:
                        if melody_line[i].is_note_extended():
                            notes_to_extend.add(melody_line[i].get_note_value())
                        else:
                            notes_to_play.add(melody_line[i].get_note_value())

                    notes_to_stop_playing = notes_playing - notes_to_extend
                    notes_playing = (notes_to_play | notes_to_extend)


                    tick_counter +=1

                    if self.running:
                        for note in notes_to_stop_playing:
                            out_port.send(mido.Message('note_off', note=note))
                            a.note_off(note)

                        for note in notes_to_play:
                            out_port.send(mido.Message('note_on', note=note))
                            a.note_on(note)

                    else:
                        for note in notes_playing:
                            out_port.send(mido.Message('note_off', note=note))
                            a.note_off(note)

                        return

                    # print("on: ", notes_to_play)
                    # print("off: ", notes_to_stop_playing)

                    time.sleep(TempoUtils.get_note_duration_from_bpm_seconds("eigth_note", self.music_player_params.get_tempo()))

                for note in notes_playing:
                    out_port.send(mido.Message('note_off', note=note))
                    a.note_off(note)

            next_song_thread.join()
            current_song = next_song_thread.get_generated_song()



