#Notes: made by a 12 years old boy
# I make some rpg based mechanics, just to learn it and have fun too

import random
import time

# Parent class
class Character:
    # The main component, for the gameplay and mechanics
    def __init__(self, name, hp, damage, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage
        self.old_damage = damage
        self.defense = defense
        self.old_defense = defense
        self.critical = None

    def attack(self, target): # Basic attack!
        if self.hp != 0: # Check if self hp is 0 or not, you can't attack if you die right?

            if target.hp != 0: # Check if target is dead or not, why attack a dead body?
                print(f"{self.name} attacks {target.name}!")
                damage = self.damage - target.defense
                target.hp -= damage
                self.critical = "(Critical!)" if target.hp < 5 else ""

                if target.hp <= 0: # Check if after subtract target hp with damage, target is dead or not?
                    print(f"{target.name} is dead!") # If yes, don't inform the hp again, just the die

                else: # But if not, inform the hp again
                    print(f"{target.name} loss {damage} hp!")
                    print(f"{target.name} hp: {target.hp} {self.critical}/{target.max_hp}\n")

            else: # If target already dead, don't subtract the hp again, he is already dead!
                print(f"{target.name} is already dead!")

        else: # If self hp is 0, don't subtract the target hp, dead body can't attack somebody!
            print(f"Cannot attack {target.name}, {self.name} is already dead!")

    def heal_self(self): # Basic healing!
        # Check if the player already dead or not, why heal a dead body?
        # But if player is not dead, check if his hp are below max hp or already full.
        # Why use heal when your hp is already full right?
        if self.hp != 0 and self.hp < self.max_hp:
            print(f"{self.name} use healing!")
            self.hp += random.randint(10, 20)

            # This prevents hp to go beyond the max hp itself
            if self.hp > self.max_hp:
                self.hp = self.max_hp

            # After that, print the new hp!
            print(f"{self.name} hp: {self.hp}/{self.max_hp}\n")
        # If player hp is indeed full, then print that the hp is already full
        # Don't need to heal when hp is full right?
        elif self.hp == self.max_hp:
            print(f"{self.name} hp is already full!\n")

        # If player already dead, then print that he was already dead
        # Don't need to use heal when player is already dead
        else:
            print(f"Cannot heal, {self.name} is already dead.\n")

    # To see your stats! this is kinda satisfying to see
    def open_status(self):
        # Prevents open status while player is already dead!
        if self.hp != 0:
            print("=== STATUS OPEN ===") # Just the opening for sure
            print(f"Name    : {self.name}") # Name
            print(f"HP      : {self.hp}/{self.max_hp}") # Hp
            print(f"Damage  : {self.damage}") # Damage attack!
            print(f"Defense : {self.defense}\n") # Defense
            print(f"=== STATUS END ===\n") # And this is the end!

        # Just to inform that player is already dead!
        else:
            print(f"Cannot open status, {self.name} is already dead.\n")

class Knight(Character):
    def __init__(self, name, hp, damage, defense):
        # Because of the role, im increasing the hp of the player!
        super().__init__(name, hp, damage, defense)
        self.hp *= 1.2
        self.hp = round(self.hp)
        self.max_hp *= 1.2
        self.max_hp = round(self.max_hp)

    # To increase defense & damage!
    def aura(self): # Skill 1!
        # Check if player dead or not
        if self.hp != 0: # If not, use aura!
            print(f"{self.name} using aura!")
            boost = random.randint(12, 16) / 10
            self.defense *= boost
            self.damage *= boost
            add_in1 = self.defense - self.old_defense
            add_in2 = self.damage - self.old_damage
            print(f"{self.name} defense: {self.defense}(+{add_in1}) | damage: {self.damage}(+{add_in2})\n")
            time.sleep(2)
        # If yes, then print that player can't use boost because he was already dead!
        else:
            print(f"Cannot defense boost, {self.name} is already dead.\n")
            time.sleep(2)

    # Strike skill!
    def strike(self, target): # Skill 2
        # Check
        if self.hp != 0:

            # Check
            if target.hp != 0:
                print(f"{self.name} strikes {target.name}!")
                damage = round((max(0, self.damage - target.defense * 0.6)), 1)
                target.hp -= damage
                self.critical = "(Critical!)" if target.hp < 5 else ""

                # Check
                if target.hp <= 0:
                    print(f"{target.name} is dead!")

                # If not:
                else:
                    print(f"{target.name} loss {damage} hp!")
                    print(f"{target.name} hp: {round(target.hp, 1)} {self.critical}/{target.max_hp}\n")
            else:
                print(f"{target.name} is already dead!")
        else:
            print(f"Cannot throws knife at {target.name}, {self.name} is already dead.\n")

    # ULTIMATE SLASH!
    def ultimate_slash(self, target): # Ultimate skill / skill 3
        # Check
        if self.hp != 0:
            # Check
            if target.hp != 0:
                # Some extra dialogue!
                print(f"{self.name}: With the power of holy sword... I shall defeat You!!")
                time.sleep(3.5)
                print(f"{self.name}: Die!!")
                time.sleep(2)
                print(f"{self.name} use ultimate skill to {target.name}!")
                time.sleep(2.5)
                self.hp -= 20 # The recoil!
                damage = round(max(0, self.damage * 1.4), 1)
                target.hp -= damage
                self.critical = "(Critical!)" if target.hp < 5 else ""

                # Check
                if target.hp <= 0:
                    print(f"{target.name} is dead!")

                # If not:
                else:
                    print(f"{target.name} loss {damage} hp!")
                    print(f"{target.name} hp: {round(target.hp)} {self.critical}/{target.max_hp}\n")
            else:
                print(f"{target.name} is already dead.\n")
        else:
            print(f"Cannot use ultimate skill to {target.name}, {self.name} is already dead.\n")

class Assassin(Character):
    def __init__(self, name, hp, damage, defense):

        # Another stats' modification!
        super().__init__(name, hp, damage, defense)

        self.damage *= 1.4
        self.damage = round(self.damage)
        self.hp *= 0.8
        self.hp = round(self.hp)
        self.max_hp *= 0.8
        self.max_hp = round(self.max_hp)

    # Throw!
    def knife_throw(self, target): # Skill 1!
        # Check
        if self.hp != 0:
            # Check
            if target.hp != 0:
                print(f"{self.name} throws some knife at {target.name}!")
                damage = round((max(0, self.damage - target.defense * 0.8)), 1)
                target.hp -= damage
                self.critical = "(Critical!)" if target.hp < 5 else ""

                # Check
                if target.hp <= 0:
                    print(f"{target.name} is dead!")

                # If not:
                else:
                    print(f"{target.name} loss {damage} hp!")
                    print(f"{target.name} hp: {round(target.hp)} {self.critical}/{target.max_hp}\n")
            else:
                print(f"{target.name} is already dead.\n")
        else:
            print(f"Cannot throws knife to {target.name}, {self.name} is already dead.\n")

# I stop make the skill, because my battery low


k1 = Knight("John", 50, 25, 10)
k2 = Assassin("Emily", 70, 20, 10)

# THE BATTLEFIELD!
print(f"{k2.name}: Hey {k1.name}, remember me?")
time.sleep(3)
print(f"{k1.name}: {k2.name}... What are you doing here?")
time.sleep(3.5)
print(f"{k2.name}: Just having some fun!")
time.sleep(2.5)
print(f"{k1.name}: With the dead bodies?!")
time.sleep(2.5)
print(f"{k2.name}: Yes! Their blood is very sweet, {k1.name}.")
time.sleep(3.5)
print(f"{k1.name}: {k2.name}, you are crazy!!")
time.sleep(3)
print(f"{k2.name}: Am i crazy? Or is that you, that don't understand me?")
time.sleep(4)
print(f"{k1.name}: Stop it, {k2.name}!")
time.sleep(2.5)
print(f"{k2.name}: Or what? Do you want to kill me? Go ahead!")
time.sleep(3.5)
print(f"{k2.name}: Lets see, if you can kill me.")
time.sleep(3)

# Enter your code here! Make your own scenario/fight!
# Actually, I kinda lazy, so make your own fight!
# Sorry!