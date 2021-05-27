from .animal import Animal
import random


class NewAnimal(Animal):
    def __init__(self, name, i, j, hp, satiety, water, world, new_par, armor=0, is_alive=True):
        super().__init__(name, i, j, hp, satiety, water, world, armor, is_alive)
        self.new_par = new_par

    def make_move(self):
        pass

    @classmethod
    def spawn_in_position(cls, world, i, j):
        pass
