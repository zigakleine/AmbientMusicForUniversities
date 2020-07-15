import math
import random

from composingAlgorithms.HarmonyGenerator import HarmonyGenerator

'''
def crossover():
    genes_length = 4
    genes_a = ["a","p","a","b"]
    genes_b = ["c","d","e","d"]

    possible_midpoints = []
    for i in range(genes_length + 1):
        if i == 0 or i == genes_length:
            possible_midpoints.append(i)
        elif not (genes_b[i] == "e" and genes_a[i-1] == "p"):
            possible_midpoints.append(i)

    child_genes = []
    # print(possible_midpoints)
    midpoint = random.choice(possible_midpoints)
    for i in range(genes_length):
        if i < midpoint:
            child_genes.append(genes_a[i])
        else:
            child_genes.append(genes_b[i])

    print(child_genes)



for i in range(20):
    crossover()




    def crossover(self, partner):

        child_genes = []
        partner_genes = partner.get_genes()

        possible_midpoints = []
        for i in range(self.genes_length + 1):
            if i == 0 or i == self.genes_length:
                possible_midpoints.append(i)
            elif not (partner_genes[i] == "e" and self.genes[i - 1] == "p"):
                possible_midpoints.append(i)

        midpoint = random.choice(possible_midpoints)
        # no "p" "e"
        for i in range(self.genes_length):
            if i < midpoint:
                child_genes.append(self.genes[i])
            else:
                child_genes.append(partner_genes[i])

        child_dna = DNA(self.genes_length, self.key_root_note, self.octave, self.mode,
                        self.composition_parameters, self.underlying_harmony)
        child_dna.set_genes(child_genes)
        return child_dna

    def mutate(self, mutation_rate):
        new_genes = []

        for i in range(self.genes_length):

            if i - 1 < 0:
                previous_char = "none"
            else:
                previous_char = self.genes[i - 1]
            current_char = self.genes[i]
            if i + 1 > self.genes_length - 1:
                next_char = "none"
            else:
                next_char = self.genes[i + 1]

            if random.random() < mutation_rate:
                new_genes.append(self.generate_single_gene_char_mutation(previous_char, current_char, next_char))
            else:
                new_genes.append(current_char)

        self.set_genes(new_genes)


harmony_generator = HarmonyGenerator()

harmony_string = harmony_generator.generate_harmony("PERIOD", 8)

print(harmony_string)


for i in range(5):
    if i == 0:
        while i < 3:
            print(i ," in while")
            i += 1
    print(i , " outside")


b = [1,2,3]
c = [4,5,6]

a = (b,c)


print(a[0])




class a:
     def __init__(self):
         self.str = "hah"

class b:
    def __init__(self, a):
        self.a = a

    def print_a(self):
        print(self.a.str)


aa = a()

bb = b(aa)

bb.print_a()
aa.str = "huh"
bb.print_a()


a = math.inf

b = 3

print(a < b)
'''

arpeggio_notes = [random.randint(0, 2) for i in range(8)]
print(arpeggio_notes)
