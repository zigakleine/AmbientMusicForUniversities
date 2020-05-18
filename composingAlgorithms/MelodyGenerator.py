import random
import time

from composingAlgorithms.Population import Population
from songStructure.Note import Note
from utils.NoteUtils import NoteUtils
from utils.ScaleUtils import ScaleUtils


class MelodyGenerator:

    @classmethod
    def generate_melody(cls, type_of_part, length, harmony_parts, key_root_note, octave, mode, composition_parameters):

        genetic_algorithm = GeneticAlgorithm(0.008, 900)

        if type_of_part == "PERIOD":

            melody_motif_form_length = (length // 4) * 8

            a_melody = genetic_algorithm.generate_new_melody(
                melody_motif_form_length, key_root_note, octave, mode, composition_parameters, harmony_parts["a_harmony"])

            b_melody = genetic_algorithm.generate_new_melody(
                melody_motif_form_length, key_root_note, octave, mode, composition_parameters, harmony_parts["b_harmony"])

            c_melody = genetic_algorithm.generate_new_melody(
                melody_motif_form_length, key_root_note, octave, mode, composition_parameters, harmony_parts["a_harmony_r"])

            d_melody = genetic_algorithm.generate_new_melody(
                melody_motif_form_length, key_root_note, octave, mode, composition_parameters, harmony_parts["b_harmony_e"])

            a_melody_list = cls.convert_melody_to_note_list(a_melody)
            b_melody_list = cls.convert_melody_to_note_list(b_melody)
            c_melody_list = cls.convert_melody_to_note_list(c_melody)
            d_melody_list = cls.convert_melody_to_note_list(d_melody)

            whole_melody_list = a_melody_list + b_melody_list + c_melody_list + d_melody_list

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




class GeneticAlgorithm:

    def __init__(self, mutation_rate, population_size):
        self.mutation_rate = mutation_rate
        self.population_size = population_size

    def generate_new_melody(self, melody_length, key_root_note, octave, mode, composition_parameters, underlying_harmony):
        start = time.time()

        population = Population(self.mutation_rate, self.population_size, melody_length, key_root_note,
                                octave, mode, composition_parameters, underlying_harmony)

        while not population.finished:

            print(population.get_best())

            population.create_next_generation()

        end = time.time()
        print("Time: ", end - start)
        print(population.get_best())
        return population.get_best()

    def generate_melody_variation(self, underlying_harmony, length, original_melody):
        pass


