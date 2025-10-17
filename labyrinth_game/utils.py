from labyrinth_game.constants import ROOMS


def get_input(prompt='> '):
    """Ввод команды."""
    try:
        return input(prompt).strip().lower()
    except (KeyboardInterrupt, EOFError):
        print('Выход из игры.')
        return 'quit'


def describe_current_room(game_state):
    """Описание текущей комнаты."""
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    print(f'== {current_room.upper()} ==')
    print(room_data['description'])
    if room_data['items']:
        print('Заметные предметы: ', ', '.join(room_data['items']))
    if room_data['exits']:
        print('Выходы: ', ', '.join(room_data['exits'].keys()))
    if room_data['puzzle'] is not None:
        print('Кажется, здесь есть загадка (используйте команду solve).')


def show_help():
    """Показать доступные команды."""
    print('\nДоступные команды:')
    print('  go <direction>  - перейти в направлении (north/south/east/west)')
    print('  look            - осмотреть текущую комнату')
    print('  take <item>     - поднять предмет')
    print('  use <item>      - использовать предмет из инвентаря')
    print('  inventory       - показать инвентарь')
    print('  solve           - попытаться решить загадку в комнате')
    print('  quit            - выйти из игры')
    print('  help            - показать это сообщение')


def solve_puzzle(game_state):
    """Решение загадки в текущей комнате."""
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]

    if room_data['puzzle'] is None:
        print('Загадок здесь нет.')
        return

    question, correct_answer = room_data['puzzle']

    print(f'\n{question}')
    user_answer = get_input('Ваш ответ: ')

    if user_answer.strip().lower() == correct_answer.lower():
        print('Правильно! Загадка решена.')
        room_data['puzzle'] = None
        if current_room == 'hall':
            game_state['player_inventory'].append('treasure_key')
            print('Вы получили treasure_key!')
    else:
        print('Неверно. Попробуйте снова.')


def attempt_open_treasure(game_state):
    """Попытка открыть сундук с сокровищами."""
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    inventory = game_state['player_inventory']

    if current_room != 'treasure_room' or (
        'treasure_chest' not in room_data['items']
    ):
        print('Здесь нечего открывать.')
        return

    if 'treasure_key' in inventory:
        print('Вы применяете ключ, и замок щёлкает. Сундук открыт!')
        room_data['items'].remove('treasure_chest')
        print('В сундуке сокровище! Вы победили!')
        game_state['game_over'] = True
        return

    print('Сундук заперт. У вас нет подходящего ключа.')
    choice = get_input('Попробовать ввести код? (да/нет): ').lower()

    if choice in ['да', 'yes', 'y']:
        if room_data['puzzle']:
            _, correct_code = room_data['puzzle']
            user_code = get_input('Введите код: ')

            if user_code.strip() == correct_code:
                print('Код принят! Сундук открывается...')
                room_data['items'].remove('treasure_chest')
                print('В сундуке сокровище! Вы победили!')
                game_state['game_over'] = True
            else:
                print('Неверный код. Сундук остается запертым.')
        else:
            print('Нет доступных кодов для взлома.')
    else:
        print('Вы отступаете от сундука.')
