import random
import time

from composingAlgorithms.Population import Population
from songStructure.Note import Note
from utils.NoteUtils import NoteUtils
from utils.ScaleUtils import ScaleUtils


class MelodyGenerator:

    @classmethod
    def generate_melody(cls, type_of_part, length, harmony_parts, key_root_note, octave, mode, composition_parameters):

        genetic_algorithm = GeneticAlgorithm(0.01, 700)

        if type_of_part == "PERIOD":

            melody_motif_form_length = (length // 4) * 8

            a_melody = genetic_algorithm.generate_new_melody(
                melody_motif_form_length, key_root_note, octave, mode, composition_parameters,
                harmony_parts["a_harmony"], False, False, False, [], -1)

            a_melody_last_note_value = cls.get_last_note_value_in_melody(a_melody)
            b_melody = genetic_algorithm.generate_new_melody(
                melody_motif_form_length, key_root_note, octave, mode, composition_parameters,
                harmony_parts["b_harmony"], (a_melody_last_note_value != -1), False, True, a_melody, a_melody_last_note_value)

            b_melody_e = genetic_algorithm.generate_new_melody(
                melody_motif_form_length, key_root_note, octave, mode, composition_parameters,
                harmony_parts["b_harmony_e"], (a_melody_last_note_value != -1), True, True, b_melody, a_melody_last_note_value)

            a_melody_list = cls.convert_melody_to_note_list(a_melody)
            b_melody_list = cls.convert_melody_to_note_list(b_melody)
            b_melody_e_list = cls.convert_melody_to_note_list(b_melody_e)

            whole_melody_list = a_melody_list + b_melody_list + a_melody_list + b_melody_e_list

            return whole_melody_list

    @classmethod
    def convert_melody_to_note_list(cls,melody):
        note_list = []
        current_note_value = None
        for note in melody:
            new_note = None
            if note == "p":
                current_note_value = -1
                new_note = Note(current_note_value)
            elif note.isdigit():
                current_note_value = int(note)
                new_note = Note(current_note_value)
            elif note == "e":
                new_note = Note(current_note_value)
                new_note.set_note_extended(True)
            note_list.append(new_note)

        return note_list

    @classmethod
    def get_last_note_value_in_melody(cls, melody):
        last_note_value = -1
        for i in range(len(melody)):
            if melody[i].isdigit():
                last_note_value = int(melody[i])
        return last_note_value


class GeneticAlgorithm:

    def __init__(self, mutation_rate, population_size):
        self.mutation_rate = mutation_rate
        self.population_size = population_size

    def generate_new_melody(self, melody_length, key_root_note, octave, mode, composition_parameters,
                            underlying_harmony, is_continuation, is_variation, do_resolution, target_melody, note_to_continue):
        start = time.time()

        population = Population(self.mutation_rate, self.population_size, melody_length, key_root_note,
                                octave, mode, composition_parameters, underlying_harmony,
                                is_continuation, is_variation, do_resolution, target_melody, note_to_continue)

        while not population.finished:

            population.get_best()
            population.create_next_generation()

        end = time.time()
        print("Time: ", end - start)
        print("best", population.get_best())
        print("generations:", population.generations)


        return population.get_best()

