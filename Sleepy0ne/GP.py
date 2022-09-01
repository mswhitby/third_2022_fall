def Player_stats(player):
  hp = 50
  Def = 20
  Attack = 15
  print("Hp: " + str(hp) + "Def: " + str(Def) + "Ak: " + str(Attack))
#  end:
  
  if hp == 0:
    print("GAME OVER")
color_checker = [
  "Red", "orange", "yellow", "green", "blue", "indigo", "violet" ,"Black", "white" , "pink"
  ]
def color_list(): 
  print("Red, orange, yellow, green, blue, indigo, violet ,Black, white,pink.")
def green(color):
   x = 0
   while color not in color_checker:
    print("Try again")
    color = input("Different color.")
    x += 1
    if x == 10:
      return color
  
  
#The start

name = input("Welcome, To begin. Please enter a Name. Let be known you will use this name all throught the game. ")

yesorno = input(name + ", Are you sure this is the name you want? (Can't go back after you decide!)")

if "yes" in yesorno:
 color_list()
 color = input("Good, Now. What color? (Please pick from the Rainbow. Black and white are a choice too.)")
 green(color)
 
 print(color + (". Thank you for your time. Lets. Begin."))
 
 print("You wake awaken deep in forest agaisnt a tree. It seems you've forgotten everything but you name. Your name is " + name + ". You look around a bit to notice large claw marks agaisnt the trees and dirt.")
 
 choice = input("What do you do? (run away, Look around more, investigate the claw marks.)")
 if "run away" is choice:
  print("You enter fight or filght. But at the sight of the claw marks. You Book it in a random direction")
 
 if "Look around more" is choice:
  print("You take a better look at your surroundings. You find that on the ground are dead bodies in armor. The ground is burnt from a fire of sorts.")
  choice2 = input("What do you do?")
 if "investigate the clawmarks" is choice:
   print("You take a look at the marks. You have no idea what they are. You sit staring at them wondering what they are. You so focus on trying to firgure out what they are you don't notices what's behind you until you feel a cut go down the middle of your body.")
   