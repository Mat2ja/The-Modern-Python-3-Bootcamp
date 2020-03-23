class Character:
    '''models a charachter'''

    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level


class NPC(Character):
    '''models a npc charachter'''

    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        print(f'{self.name} says: "I heard you got pretty fucked last night"')


villager = NPC("Bob", 100, 12)
print(villager.name, villager.hp, villager.level)
villager.speak()
