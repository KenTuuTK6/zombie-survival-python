class Player:

    def __init__(self, name, age, health, money, ammo, water):
        self.name = name
        self.age = age
        self.health = health
        self.money = money
        self.ammo = ammo
        self.inventory = ["Water, Medkit, Canned Fish"]
        self.starterchest= ["Water, Medkit, Canned Fish"]
        self.water = water
       

    def show_starterchest(self):
        print(f"{self.name}'s starter chest: {self.starterchest}")
       

    
    
   
    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Health: {self.health}")
        print(f"Money: {self.money}")
        print(f"Ammo: {self.ammo}")

    def show_inventory(self):
        print(f"{self.name}'s inventory: {self.inventory}")
      
        
    def take_damage(self, damage):
        self.health -= damage

player1 = Player("Sebi", 17, 100, 2000, 10, "Water")
player1.take_damage(10)
print("Stats for player 1")
p2_weapon = "Machete"
print(f"Weapon: {p2_weapon}")
player1.show_starterchest()
player1.show_stats()




player2 = Player("Kentu", 18, 100, 2000, 10, "Water")
player2.take_damage(20)
print("Stats for player 2")
weapon = "knife" #weapon for player2
print(f"Weapon: {weapon}")
player2.show_starterchest()
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


shotgun = 120
print("Shotgun = 120$")
shotgun_ammo = 35
print("Shotgun ammo = 35$")
flashlight = 25
print("Flashlight = 25$")


choice = input("What would u like to purchase?")

if choice == "Shotgun":
    if player1.money >= shotgun:
       player1.money -= shotgun
       player1.inventory.append("Shotgun")
       print("Congrats you have bought a Shotgun")
       player1.show_inventory()
elif choice == "Shotgun ammo":
    if player1.money >= shotgun_ammo:
     player1.money -= shotgun_ammo
    print("Congrants you have bought Shotgun ammo")
    player1.inventory.append("Shotgun ammo")
    player1.show_inventory()

elif choice == "FLashlight":
    if player1.money >= flashlight:
      player1.money -= flashlight
      player1.inventory.append("Flashlight")
      print("Congrats you have bought a Flashlight")
      player1.show_inventory()

    else:
      print("Not enough money!")









      

















   
