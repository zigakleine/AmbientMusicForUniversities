import copy


class Song():
    def __init__(self, mode, key):

        self.key = key
        self.mode = mode

        self.structure_string = ""
        self.parts_set = None
        self.parts_dict = None
        self.structure_list = None

    def get_structure_string(self):
        return self.structure_string

    def set_structure_string(self, new_structure_string):
        self.structure_string = new_structure_string

    def construct_parts_set(self):

        self.parts_set = set()

        structure_parts = self.structure_string.split(",")

        for part in structure_parts:
            self.parts_set.add(part.split("_")[0])

    def get_parts_set(self):
        return self.parts_set

    def set_parts_dict(self, new_parts_dict):
        self.parts_dict = new_parts_dict

    def get_parts_dict(self):
        return self.parts_dict

    def construct_structure_list(self):
        self.structure_list = []
        structure_parts = self.structure_string.split(",")

        for part in structure_parts:

            part_info = part.split("_")

            part_to_append = copy.deepcopy(self.parts_dict[part_info[0]])

            if part_info[1] == "n":
                part_to_append.set_is_intro_or_outro(True)
            elif part_info[1] == "m":
                part_to_append.set_is_intro_or_outro(False)

            self.structure_list.append(part_to_append)

    def get_structure_list(self):
        return self.structure_list

    # key getter & setter
    def get_key(self):
        return self.key

    def set_key(self, new_key):
        self.key = new_key

    # mode getter & setter
    def get_mode(self):
        return self.mode

    def set_mode(self, new_mode):
        self.mode = new_mode

