class Song():
    def __init__(self, key_root_note, mode):

        self.key_root_note_value = key_root_note
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

    # key_root_note getter & setter
    def get_key_root_note_value(self):
        return self.key_root_note_value

    def set_key_root_note_value(self, new_key_root_note_value):
        self.key_root_note_value = new_key_root_note_value

    # mode getter & setter
    def get_mode(self):
        return self.mode

    def set_mode(self, new_mode):
        self.mode = new_mode

    # tempo getter & setter
    def get_tempo(self):
        return self.tempo

    def set_tempo(self, new_tempo):
        self.tempo = new_tempo
