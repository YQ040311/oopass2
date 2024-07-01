class Character:
    def __init__(self, name, role, health, strength, defence, magic, ranged):
        self.name = name
        self.role = role
        self.health = health
        self.strength = strength
        self.defence = defence
        self.magic = magic
        self.ranged = ranged

    def attack(self, opponent):
        if self.ranged > 0:
            damage = self.ranged
        else:
            damage = self.strength
        blocked_damage = opponent.defence
        actual_damage = max(0, damage - blocked_damage)
        opponent.health -= actual_damage
        return actual_damage, opponent.health

    def __str__(self):
        return (f"{self.name} is a {self.role} and has the following stats:\n"
                f"Health: {self.health}\n"
                f"Strength: {self.strength}\n"
                f"Defence: {self.defence}\n"
                f"Magic: {self.magic}\n"
                f"Ranged: {self.ranged}\n")


class Arena:
    def __init__(self, name):
        self.name = name
        self.characters = {}

    def add_character(self, character):
        self.characters[character.name] = character
        print(f"{character.name} was added to {self.name}")

    def remove_character(self, name):
        if name in self.characters:
            del self.characters[name]
            print(f"{name} was removed from {self.name}")
        else:
            print(f"{name} cannot be removed as they were not found in the arena")

    def battle(self, name1, name2):
        if name1 not in self.characters or name2 not in self.characters:
            print(f"Both characters must be in the arena to battle")
            return

        char1 = self.characters[name1]
        char2 = self.characters[name2]

        print(f"-----   Battle has taken place in {self.name} on the Castle Walls between {char1.name} and {char2.name}  -----")
        round_count = 1
        while char1.health > 0 and char2.health > 0 and round_count <= 10:
            print(f"\nRound {round_count}")
            damage, remaining_health = char1.attack(char2)
            print(f"{char1.name} attacks for {damage} damage!")
            print(f"{char2.name}'s defence blocked {char2.defence} damage")
            print(f"{char2.name} took {damage} damage and has {remaining_health} health remaining")

            if char2.health <= 0:
                print(f"{char2.name} has been knocked out!")
                break

            damage, remaining_health = char2.attack(char1)
            print(f"{char2.name} attacks for {damage} damage!")
            print(f"{char1.name}'s defence blocked {char1.defence} damage")
            print(f"{char1.name} took {damage} damage and has {remaining_health} health remaining")

            if char1.health <= 0:
                print(f"{char1.name} has been knocked out!")
                break
            
            round_count += 1

        if round_count > 10:
            print("The battle ran out of time!")
        print("----------   END BATTLE  ----------")


# Sample data based on provided document
falador = Arena("Falador")
varrock = Arena("Varrock")
lumbridge = Arena("Lumbridge")

tim = Character("Tim", "Ranger", 99, 10, 10, 1, 50)
jeff = Character("Jeff", "Karil", 99, 50, 40, 1, 10)
falador.add_character(tim)
falador.add_character(jeff)

# Simulate battle in Falador
falador.battle("Tim", "Jeff")

falador.remove_character("Jeff")
falador.remove_character("Jeff")  # Intentional to test removal message

kevin = Character("Kevin", "Dharok", 100, 45, 20, 10, 0)
zac = Character("Zac", "Guthan", 100, 45, 25, 12, 0)
varrock.add_character(kevin)
varrock.add_character(zac)

# Simulate battle in Varrock
varrock.battle("Kevin", "Zac")

jaina = Character("Jaina", "Mage", 90, 5, 15, 60, 0)
jay = Character("Jay", "Warrior", 85, 70, 30, 5, 5)
lumbridge.add_character(jaina)
lumbridge.add_character(jay)
lumbridge.add_character(tim)

# Simulate battle in Lumbridge
lumbridge.battle("Jay", "Tim")