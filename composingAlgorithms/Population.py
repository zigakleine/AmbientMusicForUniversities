import random

from composingAlgorithms.DNA import DNA


class Population:

    def __init__(self, mutation_rate, population_size,
                 melody_length, key_root_note, octave, mode, composition_parameters, underlying_harmony,
                 is_continuation, is_variation, do_resolution, target_melody, note_to_continue):

        self.mutation_rate = mutation_rate
        self.population_size = population_size

        self.melody_length = melody_length
        self.key_root_note = key_root_note
        self.octave = octave
        self.mode = mode
        self.composition_parameters = composition_parameters
        self.underlying_harmony = underlying_harmony

        self.is_continuation = is_continuation
        self.is_variation = is_variation
        self.do_resolution = do_resolution
        self.target_melody = target_melody
        self.note_to_continue = note_to_continue

        self.population = []
        for i in range(population_size):
            new_dna = DNA(self.melody_length, self.key_root_note, self.octave, self.mode,
                          self.composition_parameters, self.underlying_harmony, self.is_continuation, self.is_variation,
                          self.do_resolution, self.target_melody, self.note_to_continue)
            new_dna.calculate_fitness()
            self.population.append(new_dna)

        self.fitness_sum = None
        self.max_fitness_score = None
        self.mating_pool = []
        self.finished = False
        self.generations = 0
        self.perfect_score = 1

    def pick_dna_weighted(self):

        i = -1
        r = random.randint(0, self.fitness_sum)

        while r > 0:
            i += 1
            r = r - self.population[i].get_fitness()

        return self.population[i]

    def accept_reject(self):
        while True:

            dna = self.population[random.randrange(0, self.population_size)]
            accept_threshold = random.uniform(0, self.max_fitness_score)

            if accept_threshold < dna.get_fitness():
                return dna

    def create_next_generation(self):

        new_population = []

        for i in range(self.population_size):
            partner_a = self.accept_reject()
            partner_b = self.accept_reject()

            child = partner_a.crossover(partner_b)
            child.mutate(self.mutation_rate)
            child.calculate_fitness()
            new_population.append(child)

        self.generations += 1
        self.population = new_population

    def calculate_fitness(self):

        for i in range(self.population_size):
            self.population[i].calculate_fitness()

    def get_best(self):
        best_fitness_score = 0
        best_fitness_dna = None
        self.fitness_sum = 0
        for dna in self.population:

            self.fitness_sum += dna.get_fitness()

            if dna.get_fitness() > best_fitness_score:
                best_fitness_score = dna.get_fitness()
                best_fitness_dna = dna

        fitness_threshold = 0.95 * 5
        if self.do_resolution:
            fitness_threshold += 0.95
        if self.is_continuation:
            fitness_threshold += 0.95
        if self.is_variation:
            fitness_threshold += 0.8

        if best_fitness_score > fitness_threshold or self.generations > 50:
            self.finished = True

            print("melody amount", best_fitness_dna.calculate_melody_amount())
            print("note extension amount", best_fitness_dna.calculate_note_extension_amount())
            print("melody to harmony fit", best_fitness_dna.calculate_melody_to_harmony_fit())
            print("average interval", best_fitness_dna.calculate_average_interval())
            print("melody range", best_fitness_dna.calculate_melody_range())
            print("resolution intensity: ", best_fitness_dna.calculate_resolution_intensity(), best_fitness_dna.do_resolution)
            print("continuation intensity: ", best_fitness_dna.calculate_continuation(),
                  best_fitness_dna.is_continuation)
            if best_fitness_dna.is_variation:
                print("similarity: ", best_fitness_dna.calculate_similarity(), best_fitness_dna.is_variation)

        self.max_fitness_score = best_fitness_score
        return best_fitness_dna.get_genes()

    def finished(self):
        return self.finished
