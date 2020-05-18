import random

from utils.NoteUtils import NoteUtils
from utils.ScaleUtils import ScaleUtils


class DNA:

    def __init__(self, genes_length, key_root_note, octave, mode, composition_parameters, underlying_harmony):
        self.genes = []
        self.fitness = None
        self.genes_length = genes_length
        self.key_root_note = key_root_note
        self.octave = octave
        self.mode = mode
        self.key_root_note_octave = NoteUtils.transpose_note_value_to_octave(key_root_note, octave)
        self.scale = ScaleUtils.generate_scale_from_key_root_value(self.key_root_note_octave, mode, 2)
        self.composition_parameters = composition_parameters
        self.underlying_harmony = underlying_harmony

        self.generate_new_genes()

    def get_genes(self):
        return self.genes

    def set_genes(self, new_genes):
        self.genes = new_genes

    def get_fitness(self):
        return self.fitness

    def calculate_fitness(self):

        score = 0

        #score += 1 - abs(self.composition_parameters.get_melody_to_silence_ratio() - self.calculate_melody_percentage())
        score += (16 - abs(self.composition_parameters.get_average_note_length() - self.calculate_average_note_length()))/16
        score += (25 - abs(self.composition_parameters.get_average_interval() - self.calculate_average_interval()))/25
        #print(self.calculate_average_note_length())
        score += 1 - abs(self.composition_parameters.get_melody_to_harmony_fit() - self.calculate_melody_to_harmony_fit())

        self.fitness = score

    def generate_new_genes(self):

        # we can generate:
        # -- note_value in a 2 octave range from key_root_note
        # -- e for extended
        # -- p for pause

        previous_char = "none"

        for i in range(self.genes_length):
            current_char = self.generate_single_gene_char(previous_char)
            previous_char = current_char
            self.genes.append(current_char)

    def generate_single_gene_char(self, previous_char):

        generated_char = None

        note_or_pause_weights = [self.composition_parameters.get_melody_to_silence_ratio(),
                                 1 - self.composition_parameters.get_melody_to_silence_ratio()]
        note_or_pause_choices = ["note", "pause"]

        note_or_pause = random.choices(note_or_pause_choices, note_or_pause_weights, k=1)[0]

        if note_or_pause == "note":

            if previous_char == "none" or previous_char == "p":
                generated_char = str(random.choice(self.scale).get_note_value())

            else:
                new_note_or_extend_weights = [1 * (16 - self.composition_parameters.get_average_note_length()),
                                              40 * self.composition_parameters.get_average_note_length()]
                new_note_or_extend_choices = ["new_note", "extend"]

                new_note_or_extend = random.choices(new_note_or_extend_choices, new_note_or_extend_weights, k=1)[0]

                if new_note_or_extend == "new_note":
                    generated_char = str(random.choice(self.scale).get_note_value())

                else:
                    generated_char = "e"
        else:
            generated_char = "p"

        return generated_char

    def crossover(self, partner):
        child_genes = []
        midpoint = random.randint(0, self.genes_length)
        partner_genes = partner.get_genes()

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

        mutated_genes = []
        previous_char = "none"
        for i in range(self.genes_length):
            if random.random() < mutation_rate:
                new_char = self.generate_single_gene_char(previous_char)
                mutated_genes.append(new_char)
                previous_char = new_char
            else:
                new_char = self.genes[i]
                mutated_genes.append(new_char)
                previous_char = new_char

        self.set_genes(mutated_genes)

    def calculate_average_note_length(self):

        number_of_notes = 0
        note_length_sum = 0

        for i in range(self.genes_length):

            if self.genes[i].isdigit():
                number_of_notes += 1
                note_length_sum += 1
            elif self.genes[i] == "e":
                note_length_sum += 1

        if number_of_notes == 0:
            return 0
        else:
            average_note_length = note_length_sum/number_of_notes
            return average_note_length

    def calculate_melody_percentage(self):

        melody_elements = 0
        all_elements = 0

        for i in range(self.genes_length):

            if self.genes[i].isdigit() or self.genes[i] == "e":
                melody_elements += 1
            all_elements += 1

        melody_percentage = melody_elements/all_elements
        return melody_percentage

    def calculate_melody_to_harmony_fit(self):

        melody_elements = 0
        chord_tones = 0
        note_playing = None
        for i in range(self.genes_length):
            if self.genes[i].isdigit():
                melody_elements += 1
                note_playing = self.genes[i]
                for note in self.underlying_harmony[i].get_notes():

                    if NoteUtils.are_note_values_the_same_note(int(note_playing), note.get_note_value()):
                        chord_tones += 1
                        melody_elements += 1
                        break

            elif self.genes[i] == "e":
                for note in self.underlying_harmony[i].get_notes():

                    if NoteUtils.are_note_values_the_same_note(int(note_playing), note.get_note_value()):
                        chord_tones += 1
                        melody_elements += 1
                        break

            elif self.genes[i] == "p":
                note_playing = -1


        if melody_elements == 0:
            return 0
        else:
            return chord_tones / melody_elements

    def calculate_average_interval(self):

        number_of_intervals = 0
        interval_size_sum = 0

        previous_note = -1

        for i in range(self.genes_length):
            if self.genes[i].isdigit():
                if previous_note != -1:
                    interval_size_sum += abs(int(previous_note) - int(self.genes[i]))
                    number_of_intervals += 1
                previous_note = self.genes[i]

        if number_of_intervals == 0:
            return 0
        else:
            average_interval = interval_size_sum / number_of_intervals
            return average_interval

    def calculate_resolution_intensity(self):
        last_note_value = -1
        last_note_length = -1
        last_note_index = -1

        for i in range(self.genes_length, -1, -1):
            if self.genes[i].isdigit():
                last_note_value = self.genes[i]
                last_note_length = 1
                while i+1 < self.genes_length and self.genes[i+1] == "e":
                    last_note_length += 1

                break

    def calculate_similarity(self):

        for i in range(self.genes_length):
            break
