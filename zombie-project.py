class Player:

    def __init__(self, name, age, health, money, ammo,):
        self.name = name
        self.age = age
        self.health = health
        self.money = money
        self.ammo = ammo
       
        
    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Health: {self.health}")
        print(f"Money: {self.money}")
        print(f"Ammo: {self.ammo}")
        
        
    def take_damage(self, damage):
        self.health -= damage

player1 = Player("Sebi", 17, 100, 2000, 10,)
player1.take_damage(10)
print("Stats for player 1")
p2_weapon = "Machete"
print(f"Wepaon: {p2_weapon}")
player1.show_stats()

player2 = Player("Kentu", 18, 100, 2000, 10,)
player2.take_damage(20)
print("Stats for player 2")
weapon = "knife" #weapon for player2
print(f"Weapon: {weapon}")
player2.show_stats()



if player1.ammo < 150:
    print("You should run")
else:
    print("You'r good for now")

if player2.ammo >= 10:
    print("You'r good for now lil bro")
else:
    print("You should run")


print("Sebi found a shop,here are the available products")


print("Medkit = 500")
print("Canned Fish = 300 ")
print("Energy Drink = 1200")


choice = input("What would like to purchase?")
bought = " Sebi has bought nothing"



if choice == "Medkit":
    player1.money -= 500

    print(f"Sebi bough Medkit and now has: {player1.money} money")

elif choice == "Canned Fish":
    player1.money -= 300

    print(f"Sebi bough Canned Fish and now has: {player1.money} money")

elif choice == "Energy Drink":
    player1.money -= 1200
    print(f"Sebi bought Energy Drink and now has: {player1.money} money")

else:
    print(bought)
    print(f"And still has: {player1.money} in his account")
















   
