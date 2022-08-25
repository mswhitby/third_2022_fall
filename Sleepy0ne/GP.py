#The start
name = input("Welcome, To begin. Please enter a Name. Let be known you will use this name all throught the game. ")
yesorno = input(name + ", Are you sure this is the name you want? (Can't go back after you decide!)")
if "yes" in yesorno:
  print("Then let's begin.")
else:
    name2 = input("Enter name: ")
    print(name2 + ", Hopefully this is what yu wanted. Let's begin." )

