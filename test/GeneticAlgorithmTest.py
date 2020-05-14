# we need:
# 1. Variation
# 2. Heredity
# 3. Selection

# algorithm
# 1 -> create a population of n elements (setup)
# 2 -> calculate fitness for n elements
# 3 -> reproduction / selection
# # 3.1 pick k parents with highest fitness scores
# # 3.2 pick 2 parents -> probability of picking corresponds to fitness score
# # 3.3 make a new element trough crossover and mutation
# # 3.3 add element to the new population


class GeneticAlgorithm:

    def __init__(self):
        self.target_phrase = "unicorn"
        self.mutation_rate = 0.01
        self.population_size = 500

    def find_solution(self):
        population = Population(self.target_phrase, self.mutation_rate, self.population_size)

        while not population.finished:

            population.create_mating_pool()

            population.create_next_generation()

            population.calculate_fitness()

            print(population.get_best())

        print(population.get_best())


class Population:

    def __init__(self, target_phrase, mutation_rate, population_size):
        self.target_phrase = target_phrase
        self.mutation_rate = mutation_rate
        self.population_size = population_size
        self.population = []

        for i in range(population_size):
            self.population.append(DNA(len(self.target_phrase)))

    def create_mating_pool(self):
        pass

    def create_next_generation(self):
        pass

    def calculate_fitness(self):
        pass

    def get_best(self):
        pass

    def finished(self):
        return False


class DNA:

    def __init__(self, phrase_length):
        self.phrase_length = phrase_length
        self.phrase = ""

    def get_phrase(self):
        return self.phrase

    def fitness(self, target_phrase):

        score = 0

        for i in range(self.phrase_length):
            pass






