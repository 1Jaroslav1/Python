from functions_with_data import write_to_file, read_file


"""
Власні класи для оброблення помилок(можна користуватися стандартними)
"""

class InvalidIndex(Exception):
    def __init__(self, index):
        super().__init__('Invalid index')
        self.index = index

class SizeError(Exception):
    pass

class Vector:
    def __init__(self, n, array=[]):
        if len(array) == 0:
            self.values = [0]*n
        else:
            if n == len(array):
                self.values = array
            else:
                raise SizeError


    def get_values(self):
        """
        Вертає елементи вектора
        """
        return self.values

    def give_elem(self, index):
        """
        Вертає елемент під індексом index у векторі
        """
        try:
            return self.values[index]
        except IndexError:
            raise InvalidIndex(index)
    
    def change_elem(self, index, new_value):
        """
        Змінює елемент під індексом index у векторі на елемент new_value
        """
        try:
            self.values[index] = new_value
        except IndexError:
            raise InvalidIndex(index)

    def add_vector(self, vector):
        """
        Додає вектор до іншого вектора
        """
        if(len(self.values) == len(vector.get_values())):
            for i in range(len(self.values)):
                self.values[i] += vector.get_values()[i]
        else:
            raise SizeError("Incorect size of vector")

    def __mul__(self, vector):
        """
        Вертає скалярний добуток двох векторів
        """
        if(len(self.values) == len(vector.get_values())):
            scalar_multiplication = 0
            for i in range(len(self.values)):
                scalar_multiplication += self.values[i] * vector.get_values()[i]
            return scalar_multiplication
        else:
            raise SizeError("Incorect size of vector")

    def write_to_file(self, path):
        """
        записує елементи вектора до файла з силскою path
        """
        write_to_file(path, self.values)
    
    def read_from_file(self, path):
        """
        зчитує елементи вектора з файла з силскою path
        """
        self.values = read_file(path)

