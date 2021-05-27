from .GameObjects.Animals.blue_rabbit import BlueRabbit
from .GameObjects.Animals.chicken import Chicken
from .GameObjects.Plants.grassy import Grassy
from .functions import *
from .GameObjects.Animals.new_animal import NewAnimal


class World:
    def __init__(self):
        self.creatures = []
        self.objects = []
        # for _ in range(10):
        #     Chicken.spawn(self)
        for _ in range(20):
            BlueRabbit.spawn(self)
        for _ in range(60):
            Grassy.spawn(self)
        for _ in range(10):
            NewAnimal.spawn(self)


    def get_alive_creatures(self):
        return list(filter(lambda creature: creature.is_alive is True, self.creatures))

    def run(self):
        years = 1

        round_ = 1
        while True:
            if round_ % years == 0:
                clear()
                matrix = create_matrix()
                for obj in self.get_alive_creatures():
                    obj.draw(matrix)
                print_matrix(matrix)

            # lst = [creature.satiety for creature in self.creatures if isinstance(creature, Animal)]
            # print(lst)

            for creature in self.get_alive_creatures():
                creature.make_move()

            Grassy.check_spawn(self, round_)

            if round_ % years == 0:
                input()

            round_ += 1


w = World()
w.run()
