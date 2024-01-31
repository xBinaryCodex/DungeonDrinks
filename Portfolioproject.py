#Portfolio project
import random
import math
import msvcrt as m
import time
# Beginning of project

# List of spirits
spirits = {1: 'Absinth', 2: 'Licor 43', 3: 'Peach Schnapps', 4: 'Triple Sec', 5: 'Red Wine', 6: 'Rum Chata', 7: 'Pineapple Moonshine', 8: 'Tequila', 9: 'Tequila Rose', 10: 'Chocolate Liqueur', 11: 'Rose', 12: 'Captian Morgan', 13: 'Coconut Whiskey', 14: 'Gin', 15: 'Vodka', 16: 'Whiskey', 17: 'Japanese Whiskey', 18: 'Sake', 19: 'Soju', 20: 'Bacardi 151'}
spirits_list = []
# List of Mixers

mixers = {1: "None", 2: "Cream/Milk", 3: "Tea", 4: "Water", 5: "Bitters", 6: "Coconut Water", 7: "Energy Drink", 8:"Sour Mix", 9:"Coffee", 10:"Juice", 11:"Lemon Juice", 12:"Sparkling Water", 13:"Sports Drink", 14:"Soda", 15:"Beer", 16:"Seltzer", 17:"Syrup", 18:"Lime Juice", 19:"Lemonade", 20:"Dealer's Choice"}
mixer_list = []
# List of flairs and add-ins
flairs = {1:"Hot Sauce",2: "Soy Sauce",3: "Salt Rim",4: "Fresh Fruit", 5:"Tajin", 6:"Pop Rocks", 7:"Food Coloring", 8:"Grenadine", 9:"Lime Juice",10: "Blue Curacao", 11:"Boba", 12:"Bitters",13: "Whipped Cream", 14:"Dried Fruit", 15:"Sugar Rim", 16:"Crushed Herbs", 17:"Cinnamon", 18:"Caramel Sauce", 19:"Glitter", 20:"Trechas"}
flairs_list = []
# Dict of DD Classes

classes = {"Barbarian" : "You get a Beer Chaser", "Warlock" : "Add Jaeger to your drink.", "Wizard" : "Add Frieball to your drink", "Rogue" : "Take an Extra Shot", "Paladin" : "Take an Everclear Shot", "Cleric" : "Take a Liquid IV Chaser", "Bard" : "Drink with a friend", "Monk" : "Take a Sake Shot", "Sorcerer" : "Double the Spirits in your drink", "Ranger" : "Double Hotsuace added to your drink", "Fighter" : "Double the Mixers in your drink", "Druid" : "Take a Midori Shot"}
classes_keys = list(classes.keys())
classes_values = list(classes.values())

drink_style = {"1" : "Shaken", "2": "Stirred", "3": "Blended", "4": "Dealers Choice"}

shot_style = {'1' : 'Shaken', '2' : 'Stirred', '3': 'Layered', '4' : 'Dealers Choice'}


#die rolls

def roll_d20():
    return random.randint(1, 20)

def roll_d6():
    return random.randint(1, 6)

def coin_flip():
    return random.randint(0, 1)

def roll_d4():
    return random.randint(1, 4)

def roll_d12():
    return random.randint(1, 12)
#functions for recipe
def drink_or_shot():
    return 'Drink' if coin_flip() == 0 else 'Shot'

def rock_or_neat():
    return "on the rocks" if coin_flip() == 0 else "neat"

def flair_none():
    return "flair" if coin_flip() == 0 else "no flair"

            # print list
            # print("\n".join())
#final drink
final_drink = {"spirits list" : [], "mixers list" : [], "flair list" : []}

# introduction
def intro():
    print("Welcome to 'Dungeons & Drinks!'")
    time.sleep(1.5)
    print("""A simple terminal game to determine your drink for your next adventure.
You will start off by flipping a coin for the choice of either a full drink or a shot.""")
    time.sleep(1.5)
    name = input("But, first lets get your name :")
    print("Hi " + name.title() + ", lets get you started!")
    time.sleep(1.5)


intro()

while True:
    print("Press space to flip coin")
    key = m.getch() # Get a single character from the keyboard
    if key == b" ": # Check if it is a space
        break # Exit the loop
print("Flipping...")
ds_flip = drink_or_shot()
final_drink["Beverage"] = ds_flip
time.sleep(1.5)
print("You flipped " + ds_flip)

time.sleep(1.5)
# drink rolls
if ds_flip == "Drink":
    print("How will your drink be made. Lets roll a D4")
    #list available drink styles
    for k, v in drink_style.items():
        time.sleep(0.25)
        print(k, v)
    #d4 style roll
    while True:
        print("Space to roll...")
        key = m.getch() # Get a single character from the keyboard
        if key == b" ": # Check if it is a space
            break # Exit the loop
    roll = roll_d4()
    print("Rolling...")
    time.sleep(1.5)
    print("Your rolled a " + str(roll))
    style = drink_style[str(roll)]
    time.sleep(1.5)
    #print the style
    print("Your drink will be " + style)
    time.sleep(1.5)
    if style == "Dealers Choice":
        style = input("You get to choose your style! Which style would you like? Shaken, Stirred, or Blended? ")
        while style.lower() != "shaken" or style.lower() != "stirred" or style.lower() != "blended":
            style = input("Please select one of the options: ")


    #add style to final drink recipe
    final_drink["style"] = style
    #print(final_drink)
    # on the rocks or neat
    if style.lower() == "shaken" or style.lower == "stirred":
        print("Rolling to determine 'On the rocks' or 'Neat' ")

        while True:
            print("Space to roll...")
            key = m.getch() # Get a single character from the keyboard
            if key == b" ": # Check if it is a space
                break # Exit the loop
        print("Rolling...")
        rock_neat = rock_or_neat()
        time.sleep(1.5)
        print("Your drink will be " + rock_neat)
        final_drink["rocks"] = rock_neat
        time.sleep(1.5)
    # flair or no flair
    print("Will your drink have any flair?")
    flair = flair_none()
    while True:
        print("Space to roll...")
        key = m.getch() # Get a single character from the keyboard
        if key == b" ": # Check if it is a space
            break # Exit the loop
    print("Rolling ")
    time.sleep(1.5)
    print("Your drink will have " + flair)
    final_drink["flair"] = flair
    time.sleep(1.5)
# Shot Rolls

if ds_flip == "Shot":
    print("How will your shot be made. Lets roll a D4")
    #list available drink styles
    for k, v in shot_style.items():
        time.sleep(0.25)
        print(k, v)
    #d4 style roll
    while True:
        print("Space to roll...")
        key = m.getch() # Get a single character from the keyboard
        if key == b" ": # Check if it is a space
            break # Exit the loop
    print("Rolling...")
    time.sleep(1.5)
    roll = roll_d4()
    print("Your rolled a " + str(roll))
    style = shot_style[str(roll)]
    #print the style
    print("Your shot will be " + style)
    if style == "Dealers Choice":
        answer = input("You get to choose your style! Which style would you like? Shaken, Stirred, or Layered? ")
        while answer.lower() != "shaken" or answer.lower() != "stirred" or answer.lower() != "layered":
            answer = input("PLease select one of the choices ")
            style = answer
    #add style to final drink recipe
    final_drink["style"] = style
    time.sleep(1.5)
    # flair or no flair
    print("Will your shot have any flair?")
    while True:
        print("Space to roll...")
        key = m.getch() # Get a single character from the keyboard
        if key == b" ": # Check if it is a space
            break # Exit the loop
    print("Rolling...")
    flair = flair_none() 
    time.sleep(1.5)
    print("Your shot will have " + flair)
    final_drink["flair"] = flair
    time.sleep(1.5)

# rolls for number of spirits mixers and flairs if needed

print("Lets roll for our amount of ingredients ")
time.sleep(1.5)
print("First how many spirits are we adding? ")
while True:
    print("Space to roll...")
    key = m.getch() # Get a single character from the keyboard
    if key == b" ": # Check if it is a space
        break # Exit the loop
print("Rolling...")
time.sleep(1.5)
if ds_flip == "Drink":
    spirits_roll = roll_d6()
else:
    spirits_roll = roll_d4()
print("You rolled for " + str(spirits_roll) + " spirits")
final_drink["spirits"] = spirits_roll
time.sleep(1.5)
print("Now how many mixers? ")
while True:
    print("Space to roll...")
    key = m.getch() # Get a single character from the keyboard
    if key == b" ": # Check if it is a space
        break # Exit the loop
print("Rolling...")
if ds_flip == "Drink":
    mixers_roll = roll_d6()
else:
    mixers_roll = roll_d4()
time.sleep(1.5)
print("The roll calls for " + str(mixers_roll) + " mixers")
final_drink["mixers"] = mixers_roll
time.sleep(1.5)
if flair == "flair":
    print("How much flair?")
    while True:
        print("Space to roll...")
        key = m.getch() # Get a single character from the keyboard
        if key == b" ": # Check if it is a space
            break # Exit the loop
    print("Rolling...")
    flair_roll = roll_d4()
    final_drink["flair"] = flair_roll
    time.sleep(1.5)
    print("You rolled for " + str(flair_roll) + " types of flair")
else:
    print("Your drink contains no flair")
    final_drink["flair"] = "no flair"

# rolling ingredients-------------------
    #spirits ---------------------------
print("Lets roll for your " + str(spirits_roll) + " spirits.")
for k, v in spirits.items():
        time.sleep(0.15)
        print(k, v)
while True:
    print("Space to roll...")
    key = m.getch()
    if key == b" ":
        break
for roll in range(spirits_roll):
    rolled_number = roll_d20()
    print("Rolling...")
    time.sleep(1.5)
    print("Roll " + str(roll + 1) + ": You rolled a " + str(rolled_number))
    time.sleep(1.5)
    print(spirits[rolled_number])
    spirits_list.append(spirits[rolled_number])
time.sleep(1.5)
# mixers------------------------------
print("Lets roll for your " + str(mixers_roll) + " mixers.")
for k, v in mixers.items():
        time.sleep(0.15)
        print(k, v)
while True:
    print("Space to roll...")
    key = m.getch()
    if key == b" ":
        break
for roll in range(mixers_roll):
    rolled_number = roll_d20()
    print("Rolling...")
    time.sleep(1.5)
    print("Roll " + str(roll + 1) + ": You rolled a " + str(rolled_number))
    time.sleep(1.5)
    print(mixers[rolled_number])
    mixer_list.append(mixers[rolled_number])
time.sleep(1.5)

#------------Flair-------------------

total_flairs =[]

if flair == "flair":
    print("Lets roll for your " + str(flair_roll) + " flairs.")
    for k, v in flairs.items():
        time.sleep(0.15)
        print(k, v)
    while True:
        print("Space to roll...")
        key = m.getch()
        if key == b" ":
            break
    time.sleep(1.5)
    for roll in range(flair_roll):
        rolled_number = roll_d20()
        final_drink["flair"] = rolled_number
        print("Rolling...")
        time.sleep(1.5)
        print("Roll " + str(roll + 1) + ": You rolled a " + str(rolled_number))
        total_flairs.append(flairs[rolled_number])
        time.sleep(1.5)
        print(flairs[rolled_number])

print("Ready to roll to see what class your drink is? ")
time.sleep(1.5)
for k, v in classes.items():
    time.sleep(0.15)
    print(k)

while True:
    print("Space to roll...")
    key = m.getch()        
    if key == b" ":
        break
print("Rolling...")
time.sleep(1.5)
class_roll = roll_d12()
print("You rolled a " + str(class_roll))
time.sleep(1.5)
print("Your drink class is a " + classes_keys[class_roll - 1] + " class. " + classes_values[class_roll - 1])
final_drink["Class"] = classes_keys[class_roll - 1]
final_drink["Class obj"] = classes_values[class_roll - 1]
time.sleep(1.5)



print("Final Recipe: ")
print(f"A {final_drink['style']} {final_drink['Beverage']} with {final_drink["flair"]}.")
print(f"Spirits: {final_drink['spirits']}")
print(", ".join(spirits_list))
print(f"Mixers: {final_drink['mixers']}")
print(", ".join(mixer_list))
if flair == "flair":
    print(f"Flair: {final_drink['flair']}")
    print(", ".join(total_flairs))
print(f"This drink is a {final_drink['Class']} class. {final_drink['Class obj']}.")
print("Enjoy!")

