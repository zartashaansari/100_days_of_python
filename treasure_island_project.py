print(r'''
   /\                                                        /\
  |  |                                                      |  |
 /----\                  Lord Dark's Keep                  /----\
[______]             Where Brave Knights Tremble          [______]
 |    |         _____                        _____         |    |
 |[]  |        [     ]                      [     ]        |  []|
 |    |       [_______][ ][ ][ ][][ ][ ][ ][_______]       |    |
 |    [ ][ ][ ]|     |  ,----------------,  |     |[ ][ ][ ]    |
 |             |     |/'    ____..____    '\|     |             |
  \  []        |     |    /'    ||    '\    |     |        []  /
   |      []   |     |   |o     ||     o|   |     |  []       |
   |           |  _  |   |     _||_     |   |  _  |           |
   |   []      | (_) |   |    (_||_)    |   | (_) |       []  |
   |           |     |   |     (||)     |   |     |           |
   |           |     |   |      ||      |   |     |           |
 /''           |     |   |o     ||     o|   |     |           ''\
[_____________[_______]--'------''------'--[_______]_____________]
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
move1=input("left or right?").lower()
if move1=='left':
    move2=input("swim or wait").lower()
    if(move2== 'wait'):
        move3=input("Which door?").lower()
        if(move3=='yellow'):
            print("You win!")
        elif(move3=='blue'):
            print("Eaten by Beasts.Game over")
        elif(move3=='red'):
            print("Burned by fire.Game over")
        else:
            print("Game over.")

    else:
        print("Attacked by trout.Game over")
else:
    print("Fall into a hole.Game over")
