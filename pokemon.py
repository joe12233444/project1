class pokemon:
    def __init__(self, new_name, new_weight, new_height, new_food
                 , new_cp):
        self.name = new_name
        self.weight = new_weight
        self.height = new_height
        self.food = new_food
        self.cp = new_cp

    def eat(self):
        print(f'the pokemon is eatting{self.__food}.')

    def make_noice(self):
        print(f'the pokemon wow wow wow!')

    def get_name(self):
        return self.__name
    def get_weight(self):
        return self.__weight
    def get_height(self):
        return self.__height
    def get_food(self):
        return self.__food
    def get_cp(self):
        return self.__cp



class Pilachu(pokemon):
    def eat(self):
        print(f'{self.name} is eatting {self.food}. pika')

    def make_noice(self):
        print(f'{self.name} pika pika chu!')

class Squirtle(pokemon):
    def eat(self):
        print(f'{self.name} is eatting {self.food}. jenny jenny')

    def make_noice(self):
        print(f'{self.name} jenny jenny!')

