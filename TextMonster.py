#to use the random function, we need to import a library for it: 
import random


#Create the rooms
b1Rooms = ['Lake of the Maiden','Swamp of Dawn','Parallel Plains','Floating Spires','Goliath\'s Tomb']#level Counter 0-4 - Floor 1
b2Rooms = ['Pit of Confusion','Valley of the Griffon','Mermaid\'s Meadow','Siren\'s Room','Sapphire Falls']#level counter 5-9 - Floor 2
b3Rooms = ['Graveyard','Dracula\'s Catacomb','Crystal Cavern','Lava Pit','Dragon\'s Lair']#level counter 10-14 - Floor 3

#random objects that can be found in rooms
roomObject = ['sword', 'magic stones','nothing']

#the user's 'bag'
userItems = []

#Keeps track of what room the user is in.
levelCounter = 0

#See if our player is dead so we can break out of loop execution
playerDead = 0

#Added random number generator for rolling a D20 to determine successful attacks
dice=random.randint(1,20)


#function to ask the user what direction they want to go and some logic to do something with it. 
def directionToGo():
    global levelCounter # we have to set the variable to global inside our function in order to be able to use it outside this function
    if levelCounter < 14:
        printRoom(levelCounter)
        #ask user what direction they want to go
        directionChoice = str(input("What direction do you want to go? You can answer left, right, up or down. "))
        if directionChoice == "left":
            if levelCounter != 0 and levelCounter != 5 and levelCounter != 10:
                levelCounter -=1
            elif levelCounter == 0:
                print("Sorry, you can't move left. Try again.")
       
        elif directionChoice == "right":
            if  levelCounter < 14 and levelCounter != 4 and levelCounter != 9:
                levelCounter += 1
            else:
                print("Sorry, you can't move right. Try again.")
       
        elif directionChoice == "up":
            if levelCounter == 3 or levelCounter == 6 or  levelCounter  == 9:
                levelCounter += 5
            else:
                print("Sorry, you can't go upstairs.")
       
        elif directionChoice == "down":
            if levelCounter  == 7 or levelCounter == 12 and levelCounter > 5:
                levelCounter -= 5
            else:
                print("Sorry, you can't go downstairs.")
        listCheck()
        monsterAction(levelCounter)
    else:
        monsterAction(levelCounter)
        
    #Puts some spaces in 
    print (" ")
    

#item choice function - puts a random item in the rooms, lets user choose to keep or toss it. 
#TO DO: fix bug if more than one item of same type in bag - remove 1st item of type in bag
def listCheck(): 
    print("You have the following items in your bag: " + str(userItems))
    userItemsLength = len(userItems)
    if userItemsLength < 3:
        #put a random item in the room for i in roomObject:
        rand_item = random.choice(roomObject)
        print("You found a " + rand_item + ".")
        print(" ")
        if rand_item != "nothing":
            userSelect = input("Would you like to keep it? Say y or n: ")
            if userSelect == 'y':
                userItems.append(rand_item)
    else: 
        discardItem = input("You have too many items. Do you want to discard one? ")
        if discardItem == 'y':
            print(userItems)
            discardChoice = input("Which item do you want to discard? ")
            #here's an example of a definition passing in a parameter
            removeItem(discardChoice)
    print(" ")       


def removeItem(item):
    # We can only have three items in the bag, and if there is more than one of any given item
    #we need to remove only one selection. So we sort the list and remove the middle element, as the middle
    #will always contain a duplicate when sorted.
    if userItems.count(item) > 1:
        userItems.sort()
        del userItems[1]

def printRoom(levelCounter):
    #print the room the user is in
    print("Level Counter: " + str(levelCounter))
    if levelCounter < 5:
         print("You are in room " + b1Rooms[levelCounter] + "." + "\r\r")
    if levelCounter > 4 and levelCounter <= 9:
        levelCounter = levelCounter - 5
        print("You are in room " +b2Rooms[levelCounter] + "."+ "\r\r")
        #reset level counter so we can use it again. 
        levelCounter = levelCounter + 5
    if levelCounter > 9 and levelCounter !=14:
        levelCounter = levelCounter - 10
        print("You are in room " + b3Rooms[levelCounter] + "."+ "\r\r")
        levelCounter = levelCounter + 10


#make the following a function to fight a monster. 
def monsterAction(levelCounter): 
    fightMonster = random.randint(0, 1)
    global playerDead
    if fightMonster == 0 and levelCounter < 14:
        print("There is no monster in this room. You win this round.")
    elif fightMonster == 1 and levelCounter < 14:
        print("Time to fight a monster. ")
        print("                                            _")
        print("               /                             )")
        print("              (                             |\\")
        print("              /|                             \\\\")
        print("             //                               \\\\")
        print("            ///                                \\|")
        print("           /( \\                                 )\\")
        print("           \\\\  \\_                               //)")
        print("            \\\\  :\\__                           ///")
        print("             \\\\     )                         // \\")
        print("              \\\\:  /                         // |/")
        print("               \\\\ / \\                       //  \\")
        print("                /)   \\     ___..-\'         ((  \\_|")
        print("               //     /  .\'  _.\'           \\ \\  \\")
        print("              /|       \\(  _\\_____          \\ | /")
        print("             (| _ _  __/          \'-.       ) /.\'")
        print("              \\\\ .  \'-.__ \\          \\_    / / \\")
        print("               \\\\_\'.     > \'-._   \'.   \\  / / /")
        print("                \\ \\      \\     \\    \\   .\' /.\'")
        print("                 \\ \\  \'._ /     \\  /   / .\' |")
        print("                  \\ \\_     \\_   |    .\'_/ __/")
        print("                   \\  \\      \\_ |   / /  _/ \\_")
        print("                    \\  \\       / _.\' /  /     \\")
        print("                     \\   |     /.\'   / .\'       \'-,_")
        print("                      \\   \\  .\'   _.\'_/             \\")
        print("         /\\    /\\      ) ___(    /_.\'           \\    |")
        print("        | _\\__// \\    (.\'      _/               |    |")
        print("        \\/_  __  /--\'`    ,                   __/    /")
        print("        (_ ) /b)  \  \'.   :            \___.-:_/ \\__/")
        print("        /:/:  ,     ) :        (      /_.\'_/-\' |_ _ /")
        print("       /:/: __/\\ >  __,_.----.__\\    /        (/(/(/")
        print("      (_(,_/V .\'/--\'    _/  __/ |   /")
        print("       VvvV  //`    _.-\' _.\'     \\   \\")
        print("         n_n//     (((/->/        |   /")
        print("         '--'         ~='          \\  |")
        print("                                    | |_,,,")
        print("                       snd          \\  \\  /")
        print("                                     \'.__)")
        if levelCounter < 14:
            if len(userItems) == 0:
                print("Sorry, you died.")
                playerDead = 1
                print(" ")
            else:
                bagSelection = input("You have " + str(userItems) + " in your bag. What would you like to use? ")
                if bagSelection == 'magic stones' or 'sword':
                    removeItem(bagSelection)
                    print('Congratulations! You beat the monster!')
    elif levelCounter == 14:
        print("You must have both magic stones and swords to win.")
        #sets cannot take duplicates, so if the user has an extra sword or magic stones, we take them out.
        itemSet = set(userItems)
        if len(itemSet) == 2:
            print("You used your sword and magic stones to beat the monster. You win!!!")
        else: 
            print("Sorry, you didn\'t have enough weapons to beat the monster and died. You lose.")
        return
    print(" ")







#start the game - upstairs are on rooms 3, 6, and 9. Down stairs are on rooms 4, 8, and 12. 
while levelCounter < 14 and playerDead == 0:
    directionToGo()

 
