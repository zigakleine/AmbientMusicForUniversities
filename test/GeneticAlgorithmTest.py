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
'''
import random
import time


class GeneticAlgorithm:

    def __init__(self, target_phrase, mutation_rate, population_size):
        self.target_phrase = target_phrase
        self.mutation_rate = mutation_rate
        self.population_size = population_size

    def find_solution(self):
        start = time.time()
        population = Population(self.target_phrase, self.mutation_rate, self.population_size)

        while not population.finished:

            print(population.get_best())

            population.create_next_generation()


        end = time.time()
        print("Time: ", end - start)


class Population:

    def __init__(self, target_phrase, mutation_rate, population_size):

        self.target_phrase = target_phrase
        self.mutation_rate = mutation_rate
        self.population_size = population_size

        self.population = []
        for i in range(population_size):
            new_dna = DNA(len(self.target_phrase))
            new_dna.calculate_fitness(self.target_phrase)
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
            child.calculate_fitness(self.target_phrase)
            new_population.append(child)

        self.generations += 1
        self.population = new_population

    def calculate_fitness(self):

        for i in range(self.population_size):
            self.population[i].calculate_fitness(self.target_phrase)

    def get_best(self):
        best_fitness_score = 0
        best_fitness_dna = None
        self.fitness_sum = 0
        for dna in self.population:

            self.fitness_sum += dna.get_fitness()

            if dna.get_fitness() > best_fitness_score:
                best_fitness_score = dna.get_fitness()
                best_fitness_dna = dna

        if best_fitness_score == self.perfect_score:
            self.finished = True

        self.max_fitness_score = best_fitness_score
        return best_fitness_dna.get_genes()

    def finished(self):
        return self.finished



class DNA:

    def __init__(self, genes_length):
        self.genes = ""
        self.fitness = None
        for i in range(genes_length):
            self.genes += chr(random.randrange(32, 128))

    def get_genes(self):
        return self.genes

    def set_genes(self, new_genes):
        self.genes = new_genes

    def get_fitness(self):
        return self.fitness

    def calculate_fitness(self, target_phrase):

        score = 0
        for i in range(len(self.genes)):
            if self.genes[i] == target_phrase[i]:
                score += 1

        self.fitness = score /len(target_phrase)

    def crossover(self, partner):
        child_genes = ""
        midpoint = random.randint(0, len(self.genes))
        partner_genes = partner.get_genes()

        for i in range(len(self.genes)):
            if i < midpoint:
                child_genes += self.genes[i]
            else:
                child_genes += partner_genes[i]

        child_dna = DNA(len(self.get_genes()))
        child_dna.set_genes(child_genes)
        return child_dna

    def mutate(self, mutation_rate):

        mutated_genes = ""

        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                mutated_genes += chr(random.randrange(32, 128))
            else:
                mutated_genes += self.genes[i]

        self.set_genes(mutated_genes)


gen_alg = GeneticAlgorithm("abcdefghijklmnopqrstuvxyzabcdefghijklmnopqrstuvxyz", 0.008, 900)
gen_alg.find_solution()

'''
