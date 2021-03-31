from functions_with_data import write_to_json_file, read_json_file

class InvalidIndex(Exception):
    def __init__(self, index):
        super().__init__('Invalid index')
        self.index = index

class SizeError(Exception):
    pass

class Vector:
    def __init__(self, n):
        self.values = [0]*n

    def get_values(self):
        return self.values

    def give_elem(self, index):
        try:
            return self.values[index]
        except IndexError:
            raise InvalidIndex(index)
    
    def change_elem(self, index, new_value):
        try:
            self.values[index] = new_value
        except IndexError:
            raise InvalidIndex(index)

    def add_vector(self, vector):
        if(len(self.values) == len(vector.get_values())):
            for i in range(len(self.values)):
                self.values[i] += vector.get_values()[i]
        else:
            raise SizeError("Incorect size of vector")

    def __mul__(self, vector):
        if(len(self.values) == len(vector.get_values())):
            scalar_multiplication = 0
            for i in range(len(self.values)):
                scalar_multiplication += self.values[i] * vector.get_values()[i]
            return scalar_multiplication
        else:
            raise SizeError("Incorect size of vector")

    def write_to_file(self, path):
        write_to_json_file(path, self.values)
    
    def read_from_file(self, path):
        self.values = read_json_file(path)

