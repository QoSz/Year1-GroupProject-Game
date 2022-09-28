# ######################################################################################################## #

# Importing from python library
import time 
import sys
try :
    import winsound
except :
    pass
# ######################################################################################################### #  #

# Importing from module
from help import *
from map import rooms
from player import *
from items import *
from evidence import *
from notepad import *

# ######################################################################################################## #

#The music starts
try :
    winsound.PlaySound("Haunted-house.wav", winsound.SND_LOOP | winsound.SND_ASYNC )
except :
    pass

#############################################################################################################

#The Welcome Message

print("""
██████████████████████████████████████
█─▄─▄─█▄─▄▄─██▀▄─██▄─▀█▀─▄███▀░██░▄▄▄█
███─████─▄█▀██─▀─███─█▄█─█████░██▄▄▄▒█
▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▀▄▄▄▀▄▄▄▄▀
""")

print("""
▀█▀ █░█ █▀▀   █▀█ █▀ █▄█ █▀▀ █░█ █▀█   █▀▄▀█ █░█ █▀█ █▀▄ █▀▀ █▀█ █▀▀ █▀█   █▀█ █▄░█   ▀█▀ █░█ █▀▀   █░░ █▀█ █▀█ █▀ █▀▀
░█░ █▀█ ██▄   █▀▀ ▄█ ░█░ █▄▄ █▀█ █▄█   █░▀░█ █▄█ █▀▄ █▄▀ ██▄ █▀▄ ██▄ █▀▄   █▄█ █░▀█   ░█░ █▀█ ██▄   █▄▄ █▄█ █▄█ ▄█ ██▄
""")

WelcomeMessage = """
  Created by team 15

  Welcome to The Psycho Murderer On The Loose

  It is the 1920s. The United Kingdom is going through a financial crisis due to the corruption 
  
  in the government. This caused a lot of mafia activity and gun violence. It is a casual rainy 
  
  day as you walk down through the crowded slums of Birmingham, wearing your long black coat, 
  
  black fedora hat, smoking a big old Cuban cigar, minding your own business trying to get to the 
  
  Pub after a long hard day of work. As you arrive at the Pub, you sit in your usual corner, reading 
  
  the newspaper as you sip your scotch whiskey. Just as you enter a peaceful state, the young waiter 
  
  at the Pub shouts "Mr Edgar Allan. There is someone for you on the line." You thought to yourself 
  
  who would be calling at such an odd hour of the day, as you pick up the phone listening to the static 
  
  from the other end, you reply "Hello." The man on the other line seems to be panicked and in a rush 
  
  replied with a deep voice "You need to come down to the Buckingham Palace, the Queen has just been assassinated."



  This is a murder mystery game. Your objective is to find the murderer by gathering evidence

  and making a decision based on the evidence collected who the murderer is.

  To get help you may execute on of the commands on the list printed out to you above the interaction cursor
  
  """ 

ClearLine()
print()
print("The Psycho Murderer On The Loose")
print("--------------------------------")
print()

#Looping through the welcome message and printting them
for WelcomeMessages in WelcomeMessage:
  time.sleep(0.001) # In seconds
  sys.stdout.write(WelcomeMessages)
  sys.stdout.flush()
ClearLine()

print("""TIP: To collect evidence you will need to take a picture
TIP: Examine items to see their function""")

# ##########################################################################################################

# Function to create a list of items.
def list_of_items(items):
  listeditems = []
  for s in range(len(items)):
    listeditems.append((items[s]["name"]))
  items6 = (', '.join(listeditems))
  return items6

def list_of_evidence(evidence):
  listedevidence = []
  for s in range(len(evidence)):
    listedevidence.append((evidence[s]["name"]))
  evidence6 = (', '.join(listedevidence))
  return evidence6

############################################################################################################

# Function to display the notepad.
def notepad():
    print("An Officer has taken statements from all of the people before you arrived.")
    print("You can: ")
    for i in people:
        print("READ " + str(i).upper() + " to display the statement of " + str(people[i]["name"]) + ".")
    print("CLOSE NOTEPAD to display none of the statements.")

    while True:
        answer = input("What you do next: ").lower()
        answer = remove_punct(answer)
        print()

        if answer == "read butler":
            statements(answer)
            break
        elif answer == "read charles":
            statements(answer)
            break
        elif answer == "read maid":
            statements(answer)
            break
        elif answer == "read chauffeur":
            statements(answer)
            break
        elif answer == "read gardener":
            statements(answer)
            break
        elif answer == "read sandler":
            statements(answer)
            break
        elif answer == "read lohan":
            statements(answer)
            break
        elif answer == "read duffner":
            statements(answer)
            break
        elif answer == "read ray":
            statements(answer)
            break
        elif answer == "read dane":
            statements(answer)
            break
        elif answer == "read nicko":
            statements(answer)
            break
        elif answer == "read lowe":
            statements(answer)
            break
        elif answer == "close notepad":
            break
        else:
            print("Incorrect input")
            print()

############################################################################################################

# Function to display the statements form notepad.py.
def statements(command):
    cmd = str(command.split()[1])
    print(people[cmd]["statement"])

############################################################################################################

# Function to initiate an arrest.
def arrest():
    print("Who do you want to arrest?")
    print("You can: ")
    for i in people:
        print("ARREST " + str(i).upper() + " to arrest " + str(people[i]["name"]) + ".")
    print("EXIT ARREST if you want to make your decision later.")

    while True:
        answer = input("The murderer is: ").lower()
        answer = remove_punct(answer)
        print()

        if answer == "arrest butler":
            remove_life()
            break
        elif answer == "arrest charles":
            remove_life()
            break
        elif answer == "arrest maid":
            remove_life()
            break
        elif answer == "arrest chauffeur":
            remove_life()
            break
        elif answer == "arrest gardener":
            remove_life()
            break
        elif answer == "arrest sandler":
            win()
            break
        elif answer == "arrest lohan":
            remove_life()
            break
        elif answer == "arrest duffner":
            remove_life()
            break
        elif answer == "arrest ray":
            remove_life()
            break
        elif answer == "arrest dane":
            remove_life()
            break
        elif answer == "arrest nicko":
            remove_life()
            break
        elif answer == "arrest lowe":
            remove_life()
            break
        elif answer == "exit arrest":
            break
        else:
            print("Sorry Try Again!")
            print()

############################################################################################################

win_game = False
lose_game = False
life = 2
# Function removes a life if the player guesses wrong.
def remove_life():
    global life
    life = life - 1
    print("You have arrested the WRONG person.")
    print("You have " + str(life) + " attempt(s) remaining.")
    lose(life)

############################################################################################################

# Function that checks if life = 0 so that you lose the game.
def lose(life):
    global lose_game
    if life == 0:
        lose_game = True

############################################################################################################

# Function that ends the game as you have arrested the murderer.
def win():
    global win_game
    win_game = True

############################################################################################################

# Function to print the items in a room.
def print_room_items(room):
  if room["items"] != [] or room["evidence"] !=[] :
    print("There is", list_of_items(room["items"]),list_of_evidence(room["evidence"]), "here.\n")

############################################################################################################

# Function to print the items in your inventory.
def print_inventory_items(items):
  print("You have", list_of_items(items)+".\n")

############################################################################################################

# Function to print the information about the room you're in.
def print_room(room):
  print()
  print(room["name"].upper())
  print()
  if current_room["light"] == "dark":
      print("This room is DARK so you cannot see anything. Try to light it with something so you can see the items found here.")
  else:
      print(room["description"])
      print()
      print_room_items(room)

############################################################################################################

# Function that returns the room that an exit leads to.
def exit_leads_to(exits, direction):
  return rooms[exits[direction]]["name"]

############################################################################################################

#Function to display where the exits are in a room.
def print_exit(direction, leads_to):
  print("GO " + direction.upper() + " to " + leads_to + ".")

############################################################################################################

# Function to check if the winsound module can be imported, and if not the play music/stop music actions
# won't be displayed
def music_module() :
    try :
        import winsound
    except:
        return False

############################################################################################################

# Function that prints the actions you can take in a room.
def print_menu(exits, room_items, inv_items):
  print ("You can:")
  for direction in exits:
    print_exit(direction, exit_leads_to(exits, direction))
    
  if current_room["light"] == "dark":
      pass
  
  else:
      for s in range(len(room_items)):
          itemid = ((room_items[s]["id"].upper()))
          itemname = ((room_items[s]["name"]))
          print ('TAKE', itemid, 'to take', itemname + ".")


      for s in range(len(inv_items)):
          itemid = ((inv_items[s]["id"].upper()))
          itemname = ((inv_items[s]["name"]))
          print ('EXAMINE', itemid, 'to examine your', itemname + ".")
          
  #for s in range(len(inv_items)):
  #      itemid = ((inv_items[s]["id"].upper()))
  #      itemname = ((inv_items[s]["name"]))
  #      print ('DROP', itemid, 'to drop your', itemname)
        
  for i in range(0, len(inv_items)):
        if (inv_items[i]["id"]).upper() == "FINGERPRINTKIT" or  (inv_items[i]["id"]).upper() == "MAGNIFYINGGLASS":
          pass

        else:
          print("USE " + (inv_items[i]["id"]).upper() + " to use your " + (inv_items[i]["name"]) + ".")
       
  print("OPEN NOTEPAD to check statements.")
  print("VIEW EVIDENCE to assess the evidence so far collected.")
  print("MAKE ARREST to take down the murderer.")
  if music_module() == False :
      pass
  else :
      print("Type \"stop music\" to stop music." )
      print("Type \"play music\" to play music.")
  print ("What do you want to do?")

############################################################################################################

# Function to check if an exit is valid.
def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits

############################################################################################################

# Function for the go command.
def execute_go(direction):
    global current_room
    if (is_valid_exit(current_room["exits"], direction)):
        current_room = rooms[current_room["exits"][direction]]
    else:
        print ("You cannot go there.")

############################################################################################################

# Function for the take command.
def execute_take(item_id):
    global inventory
    global current_room

    if current_room["light"] == "dark":
        print("Sorry it is too dark in this room, you cannot do that.")
        return
    else:
        for i in current_room["items"]:
            if (item_id) == i["id"]:
                current_room["items"].remove(i)
                inventory.append(i)
                return

    print('You cannot take that.')

############################################################################################################

# Function for the drop command.
def execute_drop(item_id):
    global inventory
    global current_room
    
    for x in inventory:
        if (item_id == x["id"]):
            current_room["items"].append(x)
            inventory.remove(x)
            return
          
    print('You cannot drop that.')

############################################################################################################

#Function for the examine command.
def execute_examine(item_id):
    global inventory
    for x in inventory:
      if (item_id == x["id"]):
        print (x["description"])
        return

    print ('You cannot examine that.')

############################################################################################################

#Function to stop music
def execute_stop() :
    try :
        winsound.PlaySound(None, winsound.SND_ASYNC) 
    except :
        pass
    
###########################################################################################################

#Function to play music
def execute_play() :
    try :
        winsound.PlaySound("Haunted-house.wav", winsound.SND_LOOP | winsound.SND_ASYNC )
    except :
        pass
    
############################################################################################################

#function for the use command
def execute_use(item_id):
    
    global current_room


    have = []
    for i in range(0, len(inventory)):
      have.append(inventory[i]["id"])

    if item_id in have:
    
      if item_id == "torch":
          if current_room["light"] == "light":
              print("There is no need to use the torch. This room is light.")
          else:
              current_room["light"] = "light"
              

      if item_id == "dnakit":
          count = len(current_room["dna"])
          if count == 0:
            print("Sorry, there is no dna in this room.")

          elif count == 1:
            print("There was", count, "type of dna found in this room.")
            print("DNA found for:")
            for i in range(0,count):
              print(current_room["dna"][i])

          else:
            print("There were", count, "types of dna found in this room.")
            print("DNA found for:")
            for i in range(0,count):
              print(current_room["dna"][i])
      

      if item_id == "magnifyingglass":  
          print("You cannot use it here. Use it on the evidence.")
      
      if item_id == "fingerprintkit":         
          print("You cannot use it here. Use it on the evidence.")
      

      if item_id == "camera":
        if current_room["light"] == "dark" :
            print("Too dark for the camera to capture anything.")
        else:
            inroom = list_of_items(current_room["evidence"])
            if inroom == "":
                print("There is no evidence to collect in this room.")
            else:
                if any(item in current_room["evidence"] for item in evidence) == True :
                    print("You already have the item(s) from this room in the evidence.")
                else :
                    if "gun" in inroom :
                        print(inroom, "have been added to evidence.")
                        evidence.extend(current_room["evidence"]) 
                    elif "garden shears" in inroom :
                        print(inroom, "have been added to evidence.")
                        evidence.extend(current_room["evidence"])
                    else :
                        print(inroom, "has been added to evidence.")
                        evidence.extend(current_room["evidence"])
             
              

    else:
      print("You cannot use an item you do not have!")

############################################################################################################

# Function to use magnifying glass and fingerprint kit on the evidence.
def execute_use_evidence(item_id, evidence_item) :
    global evidence
    if item_id == "magnifyingglass" :
        for i in range(0,len(evidence)) :
            if evidence_item == evidence[i]["id"] :
                if evidence[i]["blood"] == "yes" :
                    print("There is blood on the " + evidence[i]["id"] +". Wonder who's it is...")
                else :
                    print("There is no blood on the " +evidence[i]["id"]+".")
            else :
                pass
    elif item_id == "fingerprintkit" :
        for i in range(0,len(evidence)) :
            if evidence_item == evidence[i]["id"] :
                if evidence[i]["fingerprints"] == [] :
                    print("There are no fingerprints on the " + evidence[i]["id"] + ".")
                else :
                    print("There are the fingerprints of the following people : ")
                    for x in range(0,len(evidence[i]["fingerprints"])) :
                        print(evidence[i]["fingerprints"][x])
            else :
                pass
    else :
        print("You cannot use that on this item.")
                    
    

############################################################################################################

def view_evidence():
  if evidence == []:
    print("You have not yet collected any evidence. Please return later.")
    
  else:
    item_list = []
    print("The following evidence has been collected. Please choose an item to look at:")
    while True :
        for i in range(len(evidence)):
            print(evidence[i]["id"].upper())
            item_list.append(evidence[i]["id"])
        print("NONE to exit")
        
        choice = input("> ").lower()
        choice = remove_punct(choice)
        if choice == "none" :
           print()
           return False
        elif choice not in item_list:
           print("You do not have this item in evidence.")
        else :
            try:
                while True :
                    print()
                    for i in range(0, len(inventory)):
                        if (inventory[i]["id"]).upper() == "FINGERPRINTKIT" : 
                            print("USE " + inventory[i]["id"].upper() + " to use your " + inventory[i]["name"] + " on the " + choice +".")
                        elif (inventory[i]["id"]).upper() == "MAGNIFYINGGLASS" :
                            print("USE " + inventory[i]["id"].upper() + " to use your " + inventory[i]["name"] + " on the " +choice +".")   
                        else:
                            pass
                    print("BACK to choose another item from the evidence.")
                    print("NONE to exit the \"view evidence\".")
                    print("What do you want to do?") 
     
                    action = input(">")
                    norm_action = normalise_input(action)
                    if norm_action[0] == "use" :
                        if len(norm_action) > 1:
                            if norm_action[1] == "magnifying" and norm_action[2] == "glass" :
                                execute_use_evidence("magnifyingglass", choice)
                            elif norm_action[1] == "fingerprint" and norm_action[2] == "kit" :
                                execute_use_evidence("fingerprintkit", choice)
                            else :
                                execute_use_evidence(norm_action[1], choice)
                        else :
                            print("Use what?")
                    elif norm_action[0] == "none" :
                        return False
                    elif norm_action[0] == "back" :
                        break
                    else :
                        print("You cannot do that.")
            except :
                if norm_action[0] == "back" :
                    return True
                else :
                    return False

############################################################################################################

# Function to execture the chosen command.
def execute_command(command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "examine":
        if len(command) > 1:
            if command[1] == "magnifying" and command[2]=="glass" : 
                execute_examine("magnifyingglass")
            elif command[1] =="fingerprint" and command[2]=="kit" :
                execute_examine("fingerprintkit")
            elif command[1] =="dna" and command[2]=="kit" :
                execute_examine("dnakit")
            else:
                execute_examine(command[1])
        else:
            print("Examine what?")

    elif command[0] == "use":
        if len(command) > 1:
            if command[1] == "magnifying" and command[2] =="glass" :  
                execute_use("magnifyingglass")
            elif command[1] == "fingerprint" and command[2] == "kit":
                execute_use("fingerprintkit")
            elif command[1] =="dna" and command[2] == "kit" :
                execute_use("dnakit")
            else:
                execute_use(command[1])
        else:
            print("Use what?")

    elif command[0] == "open" and command[1] == "notepad":
        notepad()

    elif command[0] == "view" and command[1] == "evidence":
        view_evidence()

    elif command[0] == "make" and command[1] == "arrest":
        arrest()
    
    elif command[0] == "stop" :
        if len(command) > 1:
            if command[1] == "music" :
                execute_stop()
        else :
            print("Stop what?")
    
    elif command[0] == "play" :
        if len(command) > 1:
            if command[1] == "music" :
                execute_play()
        else : 
            print("Play what?")

    else:
        print("This makes no sense.")

############################################################################################################

# Function to print menu and ask for the user input.
def menu(exits, room_items, inv_items):
    print_menu(exits, room_items, inv_items)
    user_input = input("> ")
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

############################################################################################################

# Function to move the user.
def move(exits, direction):
    return rooms[exits[direction]]

############################################################################################################

# The main function of the game.
def main():

    while True:
        print_room(current_room)
        print_inventory_items(inventory)
        command = menu(current_room["exits"], current_room["items"], inventory)
        execute_command(command)

        if win_game:
            print("""
█▀▀ █▀█ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀ █   █▄█ █▀█ █░█   █░█ ▄▀█ █░█ █▀▀   █░█░█ █▀█ █▄░█   ▀█▀ █░█ █▀▀   █▀▀ ▄▀█ █▀▄▀█ █▀▀ ░
█▄▄ █▄█ █░▀█ █▄█ █▀▄ █▀█ ░█░ ▄█ ▄   ░█░ █▄█ █▄█   █▀█ █▀█ ▀▄▀ ██▄   ▀▄▀▄▀ █▄█ █░▀█   ░█░ █▀█ ██▄   █▄█ █▀█ █░▀░█ ██▄ ▄ 

Good job of finding the psycho murderer Adam Sander. The Birmingham Police Department arrested Adam Sandler 
on the 13th of December 1920 at 3:30 am. He was taken to the county jail where he spent the night and faced 
trial on the 14th at 9:00 am where he plead guilty. He was charged for the double murder, of Elizabeth Alexandra 
who was murdered on the 13th, and an ongoing case of the murder of William Smith on the 1st of December. 
The judge sentenced him to a double life sentence, which in the court of the law states that it leads to the death penalty. 
On the 15th of December 1920 at 11 am Adam Sandler was publically shamed and executed.""")
            break
        if lose_game:
            print("UNLUCKY! YOU HAVE LOST THE GAME - BUT FEEL FREE TO PLAY AGAIN :)")
            break

if __name__ == "__main__":
    main()
