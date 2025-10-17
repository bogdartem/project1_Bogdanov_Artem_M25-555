from labyrinth_game.constants import ROOMS


def show_inventory(game_state):
    """Показать инвентарь."""
    if not game_state['player_inventory']:
        print('Инвентарь пуст.')
    elif game_state['player_inventory']:
        print(f'Инвентарь игрока: {', '.join(game_state['player_inventory'])}')


def get_input(prompt='> '):
    """Ввод команды."""
    try:
        return input(prompt).strip().lower()
    except (KeyboardInterrupt, EOFError):
        print('Выход из игры.')
        return 'quit'


def move_player(game_state, direction: str):
    """Пойти в направлении."""
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    if direction in room_data['exits'].keys():
        game_state['current_room'] = room_data['exits'][direction]
        game_state['steps_taken'] += 1
    elif direction not in room_data['exits'].keys():
        print('Нельзя пойти в этом направлении.')


def take_item(game_state, item_name):
    """Взять предмет."""
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    room_items = room_data['items']

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
