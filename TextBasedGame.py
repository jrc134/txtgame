#Karla Cruz
rooms = {               #create a dictionary
    'Communal Room': {'South': 'Vanilla Room', 'West': 'Toshi Room', 'North': 'Bridge Room', 'East': 'Chocolate Room',
                      'item': 'no item'},
    'Vanilla Room': {'North': 'Communal Room', 'East': 'Forest Room', 'item': 'food'},
    'Forest Room': {'West': 'Vanilla Room', 'item': 'sword'},
    'Bridge Room': {'East': 'Donut Room', 'South': 'Communal Room', 'item': 'elixir'},
    'Donut Room': {'West': 'Bridge Room', 'item': 'horse'},
    'Chocolate Room': {'North': 'Browsers Castle', 'West': 'Communal Room', 'item': 'key'},
    'Toshi Room': {'East': 'Communal Room', 'item': 'map'},
    'Browsers Castle': {'South': 'Chocolate Room'},  #Final Room
    }
introduction = 'Welcome to the Super Marco Adventure game!'
user_instruction = 'Travel through all eight rooms to collect all six items and reach Browsers Castle to win.'

move_direction = ['North', 'East', 'South', 'West']
print(introduction)
print(user_instruction)
print('Directions: You may move North, South, East, or West!') #user instruction
room_position = 'Communal Room'
inventory = []

while True:
    if room_position == 'Browsers Castle':
        if len(inventory) == 6:
            print('Congratulations! You have reached Browsers Castle and won the game!')
            print('You have made it to Browsers Castle with all six items, you defeated Browser,')
            print('and saved Princess Nectarine! She is very grateful and gives you a kiss on the cheek!')
            print('Thanks for playing!')
        else:
            print('You failed to collect all six items before entering Browsers Castle!')
            print('Browser defeated you and you failed to save Princess Nectarine.')
            print('Play Again?')

    print('You are currently in the {}.'.format(room_position))
    print('Your current inventory: {}.'.format(inventory))

    move_command = input('\nEnter the moves command to move between rooms or exit the game:')
    if move_command in move_direction:
        move_command = move_command.replace("go", "")
        if move_command in rooms[room_position].keys():
            room_position = rooms[room_position][move_command]
            print(room_position)
        else:
            print('Invalid move!')

    else:
        print('Invalid input')

    
    take_command = input('\nTake item:')
    
    """
    If take_command is yes then enter pickup
    """
    def pickup():
            if rooms[room_position]['item'] not in inventory:
                inventory.append(rooms[room_position]['item'])
                #user_item = input('')
                
            elif rooms[room_position]['item'] in inventory:
                print('You already have this item')
                exit()
            else:
                print('You are leaving this item behind.')
    if take_command == 'yes':
        pickup()
    else:
        pass
    #user_item = 'item'
"""
    def game(item):

        pick_up_item = input('\nYes')

        if item in rooms[room_position]:
            game(rooms[room_position]['item'])
            inventory.append('A')

        if item in inventory:
            print('You already have this item!')
            print(" ".join(inventory))
            inventory.append('B')

        elif item not in inventory:
            print('You see a', item)
            print('Would you like to pick it up? \n')
            user_item = input('')
            if user_item == 'Yes':
                print('item has been added\n')
                inventory.append(item)
            else:
                print('You are leaving this item behind.')
"""
 