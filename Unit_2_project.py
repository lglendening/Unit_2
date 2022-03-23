#Text Monster game


#simple game board


from multiprocessing.connection import wait


dungeon = [
    ['empty', 'sword!', 'stairs down'],
     ['monster', 'magic stones', 'stairs down'],
      ['monster', 'beast', '7,000 gold bars']
      ]


#player info

dead = False

inventory = []

current_room = 0
current_floor = 0
location = dungeon[current_floor][current_room]


#game loop

while True:

    #update location
    location = dungeon[current_floor][current_room]

    #describe where they are
    if location == "empty":
        print("Nothing is here. Feels creepy though.")
    elif location == 'sword!':
        print("You see a wall of swords. Should you take one.")
    elif location == 'stairs down':
        print("that is some staris going down.")
    elif location == 'monster':
        print('You see some sort of monster. You need to fight it to go any further. Be careful though.')
    elif location == 'magic stones':
        print ("Mostly its an empty room. But theres a box in the cornner, a jared, shining light emiting under the candle light. Should you grab them or keep on walkin? ")
    elif location == 'beast':
        print("Theres a big gigantic monster. This has to be it. The End. Right?  Go on FIGHT!!!!")
    elif location == '7,000 gold bars':
        print('this is it. the end. the room filled of stolen loot. you are going to go down as a hero for the town.')
        break

    #player  choices

    player_choices = input("what would you like to do? [left, right, up, down, fight, grab]: ")


    if player_choices == 'right':
        current_room += 1
        if current_room == 3:
            print("you cant go any further")
            current_room = 2
            print(location)
    elif player_choices == 'left':
        current_room -= 1
        if current_room == -1:
            print("you cant go any further")
            current_room = 0
            print(location)
    elif player_choices == 'grab' and location == 'sword!':
        inventory = 'sword'
        print('you grabed a long sword and named it slicey.')
        if 'sword' in inventory:
            print('You should keep going but keep an eye out')
    elif player_choices == 'grab' and location == 'magic stones':
        inventory == 'stones'
        print('you pick up the stones and put them in your pocket.')
    elif player_choices == 'down' and location == 'stairs down':
        current_floor += 1
        current_room = 0
    elif player_choices == 'fight' and location == 'monster':
        if 'sword' in inventory:
            print('after about 10 minutes of fighting. You are victorious! The monster had some crazy powers and was a struggle to defeat. Wonder if it was gauarding anything.')
            dungeon[current_floor][current_room] = 'empty'
            print(f'curren'empty'
        else:
            print('you should have had the stones on you you imbisle. You got beaten to death.')
            dead = True
            break

if dead == True:
    print("you lose")
else:
    print("You win..........................................................................")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print("As you were walking out of the Dungeon to tell the village of the gold that was stolen you fall into a trap. The trap had poison spikes at the bottom. As you yell for help, no one comes. They cant hear you. You are too deep down. No one comes. You bleed out and die. Alone. You kinda completed your mission, but didnt return. You arent a hero anymore. No one knows who you are or will know who you are anymore.")
    t room is now {dungeon[current_floor][current_room]}')
        else:
            print('you didnt have a sword on you so now you dead')
            dead = True
            break
    elif player_choices == 'fight' and location=='beast':
        if  'sword' in inventory:
            print("There is a big monster so you fight for about 45 miniutes you are almost dead and are stuggling to keep your balance. This is the end. Then you realize the magic stones are in your pocket. You get back on your feet and hit the boss with your fist with the stones in your palm. They are a huge blast and you go flying back onto a wall and pass out for a day. You wake up and are dehidrated and hungry. But this cant be it. So you get on your feet.")
            dungeon[current_floor][current_room] = 'empty'
        else:
            print('you should have had the stones on you you imbisle. You got beaten to death.')
            dead = True
            break

if dead == True:
    print("you lose")
else:
    print("You win..........................................................................")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print("As you were walking out of the Dungeon to tell the village of the gold that was stolen you fall into a trap. The trap had poison spikes at the bottom. As you yell for help, no one comes. They cant hear you. You are too deep down. No one comes. You bleed out and die. Alone. You kinda completed your mission, but didnt return. You arent a hero anymore. No one knows who you are or will know who you are anymore.")
    
