from macgyver import constants

class Hero:
    def __init__(self, labyrinthe):
        self.labyrinthe = labyrinthe
        self.position = position
        self.count_items = []
        self.status = None

    def move(self, direction):
        """Créez la position de départ du héros et les positions après le mouvement."""
        position = direction(position=self.position)
        if position in self.labyrinthe.paths:
            self.position = position
        if position in self.labyrinthe.item_positions:
            self.catch_item()
        if position == self.labyrinthe.guardian.position:
            self.goal()
            return False
        return True

     def catch_item(self):
         """Compter les objets après les avoir ramassés."""
        self.count_items.append(self.position)
        index = self.labyrinthe.item_positions.index(self.position)
        del self.labyrinthe.item_positions[index]


    def goal(self):
        if len(self.count_items) == len(constants.NAME_ITEMS):
            self.status = "GAGNER"
        else:
            self.status = "PERDU"
