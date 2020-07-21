import time
from composingAlgorithms.Population import Population


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
