import random

class RandomValues:

    @staticmethod
    def generate_array(size : int):
        return [random.randint(10,100) for _ in range(size)]
        