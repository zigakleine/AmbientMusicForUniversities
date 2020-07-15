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

        for part in self.structure_string:
            self.parts_set.add(part)

    def get_parts_set(self):
        return self.parts_set

    def set_parts_dict(self, new_parts_dict):
        self.parts_dict = new_parts_dict

    def get_parts_dict(self):
        return self.parts_dict

    def construct_structure_list(self):
        self.structure_list = []

        for part in self.structure_string:
            self.structure_list.append(self.parts_dict[part])

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

