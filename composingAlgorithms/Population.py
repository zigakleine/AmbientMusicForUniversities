import random

from composingAlgorithms.DNA import DNA


class Population:

    def __init__(self, mutation_rate, population_size,
                 melody_length, key_root_note, octave, mode, composition_parameters, underlying_harmony):

        self.mutation_rate = mutation_rate
        self.population_size = population_size

        self.melody_length = melody_length
        self.key_root_note = key_root_note
        self.octave = octave
        self.mode = mode
        self.composition_parameters = composition_parameters
        self.underlying_harmony = underlying_harmony

        self.population = []
        for i in range(population_size):
            new_dna = DNA(self.melody_length, self.key_root_note, self.octave, self.mode, self.composition_parameters, self.underlying_harmony)
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

        if best_fitness_score > 2.6 or self.generations > 75:
            self.finished = True

        self.max_fitness_score = best_fitness_score
        return best_fitness_dna.get_genes()

    def finished(self):
        return self.finished

