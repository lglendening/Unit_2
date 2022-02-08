'''
#################
Lab 2.06
#################
1. In your Notebook
-------------------
Predict what will be printed then type the program in your console to confirm
Example 1
    a = 0
    while a < 10:
        print(a)

prediction: nothing
actual:     nothing

Example 2


prediction:     1
actual:         nothing

2. In your Notebook
-------------------
Create a set of test cases for the following sample code and predict the behavior
    a = input("Would you like to quit: ")
    while a != "y" and a != "n" :
        a = input("Would you like to quit: ")

test cases: 'y', 'n', 'q', 'cat'

3. Implement the Tic Tac Toe game using a while loop
----------------------------------------------------
Allow users to keep playing (max 9 times).

Use variables to decide whose turn it is, and greet them as Xs or Os.

User picks a location on the board according to the number:
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9


Depending on the position user gave, update the corresponding position of the board to reflect that.

Print the updated board out.

You will not need to determine the winner at this point.
(Copy and paste your previous tic-tac-toe version and modify the code to implement the above)
'''
# board

board = [[1, 2, 3] , [4, 5, 6] , [7, 8, 9]]



turns = 9
while turns > 0:
    turns = turns-1

    print("---------")  
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("---------")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("---------")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    print("---------")


#player turn

    turn = int(input("pick a number to where to place your x: "))

    if turn==1:
        board[0][0] = 'x'
    elif turn==2:
        board[0][1] = 'x'
    elif turn==3:
        board[0][2] = 'x'
    elif turn==4:
        board[1][0] = 'x'
    elif turn==5:
        board[1][1] = 'x'
    elif turn==6:
        board[1][2] = 'x'
    elif turn==7:
        board[2][0] = 'x'
    elif turn==8:
        board[2][1] = 'x'
    elif turn==9:
        board[2][2] = 'x'


#update board

 

    print("---------")
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("---------")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("---------")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    print("---------")


#player turn

    turn = int(input("pick a number to where to place your o: "))

    if turn==1:
        board[0][0] = 'o'
    elif turn==2:
        board[0][1] = 'o'
    elif turn==3:
        board[0][2] = 'o'
    elif turn==4:
        board[1][0] = 'o'
    elif turn==5:
        board[1][1] = 'o'
    elif turn==6:
        board[1][2] = 'o'
    elif turn==7:
        board[2][0] = 'o'
    elif turn==8:
        board[2][1] = 'o'
    elif turn==9:
        board[2][2] = 'o'

