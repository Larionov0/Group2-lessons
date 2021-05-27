class Bottle:
    def __init__(self, text, v, material, liquids=None):
        self.__text = text  # private
        self.__v = v  # private
        self.__material = material  # private
        if liquids is None:
            liquids = {}
        self.liquids = liquids

    @property
    def text(self):
        return self.__text

    @property
    def v(self):
        return self.__v

    @property
    def material(self):
        return self.__material

    def will_liquid_fit(self, liquid_v):
        print(self.__v)
        if self.__v >= liquid_v:
            return True
        else:
            return False

    def add_liquid(self, liquid, v):
        if self.will_liquid_fit(v):
            pass
        else:
            pass

    def pour_out_liquid(self, v):
        pass

    def print_liquids(self):
        pass


b = Bottle('Coca-Cola', 3, 'скло', [])
print(b.v)
