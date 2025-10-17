from labyrinth_game.constants import ROOMS


def show_inventory(game_state):
    """Показать инвентарь."""
    if not game_state['player_inventory']:
        print('Инвентарь пуст.')
    elif game_state['player_inventory']:
        print(f'Инвентарь игрока: {', '.join(game_state['player_inventory'])}')


def move_player(game_state, direction: str):
    """Пойти в направлении."""
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    
    if direction not in room_data['exits']:
        print('Нельзя пойти в этом направлении.')
        return
    
    next_room = room_data['exits'][direction]
    
    if next_room == 'treasure_room':
        if 'treasure_key' not in game_state['player_inventory']:
            print('Дверь заперта. Нужен ключ, чтобы пройти дальше.')
            return
        else:
            print('Вы используете найденный ключ, '
                  'чтобы открыть путь в комнату сокровищ.')
    
    game_state['current_room'] = next_room
    game_state['steps_taken'] += 1
    
    from labyrinth_game.utils import random_event
    random_event(game_state)


def take_item(game_state, item_name):
    """Взять предмет."""
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    room_items = room_data['items']

    if item_name == 'treasure_chest':
        print("Вы не можете поднять сундук, он слишком тяжелый.")
        return

    if item_name in room_items:
        game_state['player_inventory'].append(item_name)
        room_items.remove(item_name)
        print('Вы подняли: ', item_name)
    elif item_name not in room_items:
        print('Такого предмета здесь нет.')


def use_item(game_state, item_name):
    """Использовать предмет из инвентаря."""
    inventory = game_state['player_inventory']

    if item_name not in inventory:
        print('У вас нет такого предмета.')
        return

    match item_name:
        case 'torch':
            print('Вы зажигаете факел. Стало светлее, '
                  'теперь можно разглядеть детали комнаты.')

        case 'sword':
            print('Вы достаете меч. Чувствуется уверенность в своих силах!')

        case 'bronze_box':
            print('Вы открываете бронзовую шкатулку. Внутри что-то блестит...')
            if 'rusty_key' not in inventory:
                inventory.append('rusty_key')
                print('Вы нашли rusty_key и добавили его в инвентарь!')
            else:
                print('Шкатулка пуста.')
        case 'treasure_key':
            if game_state['current_room'] == 'treasure_room':
                from labyrinth_game.utils import attempt_open_treasure
                attempt_open_treasure(game_state)
            else:
                print('Этот ключ выглядит особенным. '
                      'Возможно, он подойдет к чему-то важному.')
        case _:
            print(f'Вы не знаете, как использовать {item_name}.')
