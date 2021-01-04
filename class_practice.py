from table_class import Lotus

class weapon:
    def __init__(self, damage=7, delay=28):
        self.damage = damage
        self.delay = delay
class one_hand_slash(weapon):
    def __init__(self, damage_type: str='slash'):
        super().__init__(damage=8, delay=20)
        self.damage_type = damage_type

class Mazda(Lotus):
    pass

