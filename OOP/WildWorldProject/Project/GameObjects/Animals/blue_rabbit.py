import random
from .animal import Animal, Grassy


class BlueRabbit(Animal):
    sprite = 'r'
    radius = 3
    names = ['Pupsen', 'Vupsen']

    def make_move(self):
        cur_min = float('inf')
        nearest_grassy = None
        for creature in self.get_all_creatures_in_radius(self.radius):
            if isinstance(creature, Grassy):
                d = self.distance(creature)
                if d < cur_min:
                    cur_min = d
                    nearest_grassy = creature

        if nearest_grassy:
            self.move_to_point([nearest_grassy.i, nearest_grassy.j])
        else:
            self.move(random.choice(['w', 'a', 's', 'd']))

        grassies = self.get_grassies()
        if grassies:
            grassies[0].die()
            self.restore_satiety(grassies[0].satiety * 3 + 2)

        self.loose_satiety(1)

    @classmethod
    def spawn_in_position(cls, world, i, j):
        new_rabbit = cls(
            name=random.choice(cls.names),
            i=i,
            j=j,
            hp=5,
            satiety=random.randint(5, 9) + random.randint(5, 9) + random.randint(5, 9),
            water=0,  #
            world=world
        )
        world.creatures.append(new_rabbit)
