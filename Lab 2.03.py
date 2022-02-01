'''
##########################################
Lab 2.03 - Game Show
##########################################
In your Notebook
Follow the flow of execution in the following programs and predict what will happen for each
one
---------------------------------------
Example 1
---------------------------------------
a = input("What... is your quest")
b = "to seek the holy grail"
if a != b:
    print("Go On. Off you go")
else:
    b = input("What...is the air-speed velocity of an unladen swallow?")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHHH [Bridgekeeper was thrown over bridge]")
    else:
        print("[you were thrown over bridge]")

Prediction:     [you were thrown over bridge]
Actual:         error for me

---------------------------------------
Example 2
---------------------------------------
user_input = input("What is your favorite color")
if user_input == 'blue':
    print("Blueskadoo")
elif user_input == "red":
    print("Roses are red!")
elif user_input == "yellow":
    print("Mellow Yellow")
elif user_input == "green":
    print("Green Machine")
elif user_input == "orange":
    print("Orange you glad I didn't say banana.")
elif user_input == "black":
    print("I see a red door and I want it painted black")
elif user_input == "purple":
    print("And we'll never be royalllssss")
elif user_input == "pink":
    print("Pinky- and the Brain")
else:
    print("I don't recognize that color. Is it even...??")

Prediction:     It will print one of those responses corrisponding with the color the user chose
Actual:         Did exactly how i predicted

---------------------------------------
In your Notebook
---------------------------------------
Translate this Snap! program into a Python program
***Refer to the image provided on Moodle located below the Lab 2.03 link***
Write program below:
x = int(input ("what is x "))
y = int(input ("what is y "))
z = int(input ("what is z ")) 
if (x + y > z) and (x + z > y) and (y + z > x):
    print(f'perueter of the triange is {x + y + z}')

    #is it a right triangle
    if x ** 3 + y ** 2 == z ** 2:
        print('this is a right triangle')

        # determine if isoscolies, scaline or equiladeral
    if x==y and y==z:
        print('this is an equilateral triangle')
    elif x==y or z==y or x==z:
        print('this is an icosolies triangle')
    else:
        print(' this is a scaline triangle')
else:
    print ('this is not a triangle')

'''
# prizes

prize1= 'car'
prize2= 'xbox'
prize3= 'laptop'
prize4= 'vacation'
prize5= 'headphones'
prize6= 'ps5'
prize7= 'phone'
prize8= 'nintendo switch'
prize9= 'Meta Quest 2'
prize10= 'video camera'

#user chooses door

user_chooses_the_door_with_a_prize_behind_it = input ('which door whould you like to choose? [1-10] ')

#user gets a prize

if user_chooses_the_door_with_a_prize_behind_it == '1':
    print(prize1)
    if user_chooses_the_door_with_a_prize_behind_it == '2':
        print(prize2)
    if user_chooses_the_door_with_a_prize_behind_it == '3':
        print(prize3)
    if user_chooses_the_door_with_a_prize_behind_it == '4':
        print(prize4)
    if user_chooses_the_door_with_a_prize_behind_it == '5':
        print(prize5)
    if user_chooses_the_door_with_a_prize_behind_it == '6':
        print(prize6)
    if user_chooses_the_door_with_a_prize_behind_it == '7':
        print(prize7)
    if user_chooses_the_door_with_a_prize_behind_it == '8':
        print(prize8)
    elif user_chooses_the_door_with_a_prize_behind_it == '9':
        print(prize9)
    else:
        print(prize10)