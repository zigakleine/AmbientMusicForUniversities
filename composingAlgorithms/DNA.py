import math
import random

from utils.NoteUtils import NoteUtils
from utils.ScaleUtils import ScaleUtils


class DNA:

    # TODO: add a parameter called melody_range_octaves
    def __init__(self, genes_length, key_root_note, octave, mode, composition_parameters, underlying_harmony,
                 is_continuation, is_variation, do_resolution, target_melody, note_to_continue):
        self.genes = []
        self.fitness = None
        self.genes_length = genes_length
        self.key_root_note = key_root_note
        self.octave = octave
        self.mode = mode
        self.key_root_note_octave = NoteUtils.transpose_note_value_to_octave(key_root_note, octave)
        self.composition_parameters = composition_parameters
        self.melody_range_octaves = composition_parameters.get_melody_range_octaves()
        self.scale = ScaleUtils.generate_scale_from_key_root_value(self.key_root_note_octave, mode, self.melody_range_octaves)

        self.underlying_harmony = underlying_harmony

        self.is_continuation = is_continuation
        self.is_variation = is_variation
        self.do_resolution = do_resolution
        self.target_melody = target_melody
        self.note_to_continue = note_to_continue

        self.number_of_melodic_elements = 0
        self.number_of_note_extensions = 0
        self.melody_length = self.genes_length
        self.number_of_chord_tones = 0
        self.number_of_intervals = 0
        self.interval_size_sum = 0
        self.melody_range = 0
        self.rhythmic_range = 0
        self.first_note_value = -1
        self.resolution_intensity = 0

        self.melody_intervals_list = []
        self.melody_lengths_list = []

        self.generate_new_genes()

    def get_genes(self):
        return self.genes

    def set_genes(self, new_genes):
        self.genes = new_genes

    def get_fitness(self):
        return self.fitness

    def calculate_fitness(self):

        score = 0
        self.calculate_melody_parameters()

        score += 1 - abs(self.composition_parameters.get_melody_amount() - self.calculate_melody_amount())
        score += 1 - abs(self.composition_parameters.get_note_extension_amount() - self.calculate_note_extension_amount())
        score += ((self.melody_range_octaves*12) - abs(self.composition_parameters.get_average_interval() - self.calculate_average_interval()))/ (self.melody_range_octaves*12)
        score += ((self.melody_range_octaves*12) - abs(self.composition_parameters.get_melody_range() - self.calculate_melody_range()))/ (self.melody_range_octaves*12)
        score += (1 - abs(self.composition_parameters.get_melody_to_harmony_fit() - self.calculate_melody_to_harmony_fit()))

        # score += (self.genes_length - abs(self.composition_parameters.get_rhythmic_range() - self.calculate_rhythmic_range()))/self.genes_length
        score += (1 - abs(self.composition_parameters.get_interval_consonance() - self.calculate_interval_consonance()))

        if self.do_resolution:
            score += (1 - abs(
                self.composition_parameters.get_resolution_intensity() - self.calculate_resolution_intensity()))
        if self.is_continuation:
            score += ((self.melody_range_octaves*12) - abs(
                self.composition_parameters.get_average_interval() - self.calculate_continuation())) / (self.melody_range_octaves*12)
        if self.is_variation:
            score += self.calculate_similarity()

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

        note_or_pause_weights = [self.composition_parameters.get_melody_amount(),
                                 1 - self.composition_parameters.get_melody_amount()]
        note_or_pause_choices = ["note", "pause"]

        note_or_pause = random.choices(note_or_pause_choices, note_or_pause_weights, k=1)[0]

        if note_or_pause == "note":

            if previous_char == "none" or previous_char == "p":
                generated_char = str(random.choice(self.scale).get_note_value())

            else:
                new_note_or_extend_weights = [1 * (1 - self.composition_parameters.get_note_extension_amount()),
                                              5 * self.composition_parameters.get_note_extension_amount()]
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
                        self.composition_parameters, self.underlying_harmony, self.is_continuation, self.is_variation,
                        self.do_resolution, self.target_melody, self.note_to_continue)
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

    def generate_single_gene_char_mutation(self, previous_char, current_char, next_char):

        include_e = True
        include_p = True
        include_num = True

        if previous_char == "p" or "none":
            include_e = False

        if next_char == "e":
            include_p = False

        choices = []
        if include_p:
            choices.append("p")
        if include_e:
            choices.append("e")
        if include_num:
            choices.append(str(random.choice(self.scale).get_note_value()))

        new_char = random.choice(choices)
        return new_char

    def calculate_note_extension_amount(self):
        # percentage of extension type melodic elements in all melodic elements

        if self.number_of_melodic_elements == 0:
            return 0
        else:
            extension_percentage = self.number_of_note_extensions/self.number_of_melodic_elements
            return extension_percentage

    def calculate_melody_amount(self):
        # percentage of melodic elements in the whole melody

        melody_percentage = self.number_of_melodic_elements/self.melody_length
        return melody_percentage

    def calculate_melody_to_harmony_fit(self):
        # percentage of melodic elements that are chord tones in all melodic elements

        if self.number_of_melodic_elements == 0:
            return 1
        else:
            return self.number_of_chord_tones / self.number_of_melodic_elements

    def calculate_melody_range(self):
        return self.melody_range

    def calculate_average_interval(self):

        # average interval size in the melody

        if self.number_of_intervals == 0:
            return 0
        else:
            average_interval = self.interval_size_sum / self.number_of_intervals
            return average_interval

    def calculate_continuation(self):

        continuation_interval = abs(self.first_note_value - self.note_to_continue)
        return continuation_interval

    def calculate_resolution_intensity(self):

        # a metric that calculates the intensity of resolution in the last note of the melody

        last_note_length = 0
        chord_tones_in_last_note = 0

        for i in range(self.genes_length-1, -1, -1):
            if self.genes[i].isdigit():
                last_note_value = int(self.genes[i])
                underlying_chord_root = int(self.underlying_harmony[-1].get_root_note_value())
                chord_tones_in_last_note += NoteUtils.are_note_values_the_same_note(last_note_value,
                                                                                    underlying_chord_root)
                last_note_length = 1
                while i+1 < self.genes_length and self.genes[i+1] == "e":
                    chord_tones_in_last_note += NoteUtils.are_note_values_the_same_note(last_note_value,
                                                                                        underlying_chord_root)
                    last_note_length += 1
                    i += 1

                break

        if last_note_length <= 4:
            note_length_weight = last_note_length
        else:
            note_length_weight = 5

        self.resolution_intensity = (note_length_weight * (chord_tones_in_last_note/last_note_length))/5
        return self.resolution_intensity

    def calculate_melody_parameters(self):

        self.melody_intervals_list, self.melody_lengths_list = self.get_melody_intervals_list_and_melody_lengths_list(self.genes)

        note_playing = None
        note_playing_length = 0
        highest_note = 0
        lowest_note = 128
        first_note_found = False

        for i in range(self.genes_length):

            if self.genes[i].isdigit():

                self.number_of_melodic_elements += 1

                if not first_note_found:
                    self.first_note_value = int(self.genes[i])
                    first_note_found = True

                if note_playing is not None:
                    self.interval_size_sum += abs(int(note_playing) - int(self.genes[i]))
                    self.number_of_intervals += 1

                note_playing = self.genes[i]

                for note in self.underlying_harmony[i].get_notes():

                    if NoteUtils.are_note_values_the_same_note(int(note_playing), note.get_note_value()):
                        self.number_of_chord_tones += 1
                        break

                current_note = int(self.genes[i])
                if current_note < lowest_note:
                    lowest_note = current_note

                if current_note > highest_note:
                    highest_note = current_note

            elif self.genes[i] == "e":
                self.number_of_melodic_elements += 1
                self.number_of_note_extensions += 1
                note_playing_length += 1

                for note in self.underlying_harmony[i].get_notes():

                    if NoteUtils.are_note_values_the_same_note(int(note_playing), note.get_note_value()):
                        self.number_of_chord_tones += 1
                        break

            elif self.genes[i] == "p":
                note_playing = -1

        self.melody_range = highest_note - lowest_note

    def calculate_similarity(self):

        # a metric that calculates similarity between the generated melody and the target melody. Used for creating
        # variations on a motif-form

        target_melody_intervals_list, target_melody_lengths_list = self.get_melody_intervals_list_and_melody_lengths_list(self.target_melody)

        generated_melody_intervals_list = self.melody_intervals_list
        generated_melody_lengths_list = self.melody_lengths_list

        interval_distances_sum = 0
        num_of_intervals = 0

        num_of_lengths = 0
        lengths_distances_sum = 0

        for i in range(len(generated_melody_intervals_list)):
            if not (generated_melody_intervals_list[i] is None or target_melody_intervals_list[i] is None):
                num_of_intervals += 1
                interval_distances_sum += abs(int(generated_melody_intervals_list[i]) - int(target_melody_intervals_list[i]))
            elif not (generated_melody_intervals_list[i] is None and target_melody_intervals_list[i] is None):
                num_of_intervals += 1

        for i in range(len(generated_melody_lengths_list)):
            if not (generated_melody_lengths_list[i] is None or target_melody_lengths_list[i] is None):
                num_of_lengths += 1
                lengths_distances_sum += abs(int(generated_melody_lengths_list[i]) - int(target_melody_lengths_list[i]))
            elif not (generated_melody_lengths_list[i] is None and target_melody_lengths_list[i] is None):
                num_of_lengths += 1

        interval_similarity = 1 - (interval_distances_sum / (num_of_intervals * self.melody_range_octaves*12))

        lengths_similarity = 1 - (lengths_distances_sum/self.genes_length)

        similarity = 0.7*interval_similarity + 0.3*lengths_similarity
        return similarity

    def get_melody_intervals_list_and_melody_lengths_list(self, melody):

        interval_list_length = len(melody) - 1
        interval_list = [None] * interval_list_length
        interval_list_index = 0

        previous_note = None
        current_element = None

        melody_lengths_list_length = len(melody)
        melody_lengths_list = [None] * melody_lengths_list_length
        melody_lengths_list_index = -1

        for i in range(len(melody)):
            if melody[i].isdigit():
                current_note = int(melody[i])
                if previous_note is not None:
                    interval_list[interval_list_index] = current_note - previous_note
                    interval_list_index += 1
                previous_note = current_note

                current_element = melody[i]
                melody_lengths_list_index += 1
                melody_lengths_list[melody_lengths_list_index] = 1

            if melody[i] == "p" and current_element == "p":
                melody_lengths_list[melody_lengths_list_index] += 1
            elif melody[i] == "p":
                current_element = melody[i]
                melody_lengths_list_index += 1
                melody_lengths_list[melody_lengths_list_index] = 1

            if melody[i] == "e":
                melody_lengths_list[melody_lengths_list_index] += 1

        return interval_list, melody_lengths_list

    def calculate_rhythmic_range(self):

        shortest_note = self.genes_length
        longest_note = 0

        for note_length in self.melody_lengths_list:
            if note_length is not None:
                if note_length > longest_note:
                    longest_note = longest_note
                if note_length < shortest_note:
                    shortest_note = note_length
            else:
                break

        rhythmic_range = longest_note - shortest_note
        return rhythmic_range

    def calculate_interval_consonance(self):

        consonance_score = 0
        intervals = 0

        for interval in self.melody_intervals_list:
            if interval is not None:
                intervals += 1

                interval_quality = abs(interval) % 12

                if interval_quality == 0 or interval_quality == 7 or interval_quality == 5:
                    consonance_score += 1

                elif interval_quality == 3 or interval_quality == 4 or interval_quality == 2 or \
                        interval_quality == 8 or interval_quality == 9:
                    consonance_score += 0.5

                elif interval_quality == 1 or interval_quality == 6 or interval_quality == 10 or interval_quality == 11:
                    consonance_score += 0

        if intervals == 0:
            return 1
        else:
            return consonance_score / intervals
