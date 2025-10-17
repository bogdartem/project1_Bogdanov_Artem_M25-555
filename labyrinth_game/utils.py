import math

from labyrinth_game.constants import COMMANDS, ROOMS


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
    for command, description in COMMANDS.items():
        # Форматирование с выравниванием
        print(f'  {command:<16} - {description}')


def solve_puzzle(game_state):
    """Решение загадки в текущей комнате."""
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]

    if room_data['puzzle'] is None:
        print('Загадок здесь нет.')
        return

    question, correct_answer = room_data['puzzle']

    print(f'\n{question}')
    user_answer = get_input('Ваш ответ: ').strip().lower()

    # Проверка альтернативных ответов
    correct_answers = [correct_answer.lower()]
    
    # Добавляем альтернативные варианты для числовых ответов
    if correct_answer == '10':
        correct_answers.extend(['десять', '10'])
    elif correct_answer == 'шаг шаг шаг':
        correct_answers.extend(['шагшагшаг', 'step step step'])
    elif correct_answer == 'резонанс':
        correct_answers.extend(['resonance'])
    elif correct_answer == 'дыхание':
        correct_answers.extend(['breath', 'дыханье'])
    elif correct_answer == 'имя':
        correct_answers.extend(['name', 'name'])

    if user_answer in correct_answers:
        print('Правильно! Загадка решена.')
        room_data['puzzle'] = None
        
        # Награда в зависимости от комнаты
        match current_room:
            case 'hall':
                game_state['player_inventory'].append('treasure_key')
                print('Вы получили treasure_key!')
            case 'trap_room':
                print('Плиты перестали двигаться. Теперь можно безопасно перемещаться.')
            case 'library':
                game_state['player_inventory'].append('ancient_scroll')
                print('Вы нашли древний свиток!')
            case 'garden':
                game_state['player_inventory'].append('silver_amulet')
                print('Вы получили серебряный амулет!')
            case 'observatory':
                print('Карты на столе теперь выглядят понятнее.')
    else:
        print('Неверно. Попробуйте снова.')
        # Особый эффект для trap_room
        if current_room == 'trap_room':
            print('Неправильный ответ активирует защитный механизм!')
            trigger_trap(game_state)


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

def pseudo_random(seed, modulo):
    """Псевдослучайный генератор на основе синуса."""
    if modulo == 0:
        return 0
    
    # Используем формулу для генерации псевдослучайного числа
    x = math.sin(seed * 12.9898) * 43758.5453
    fractional = x - math.floor(x)
    result = int(fractional * modulo)
    
    return result


def trigger_trap(game_state):
    """Активация ловушки с негативными последствиями."""
    print('Ловушка активирована! Пол стал дрожать...')
    
    inventory = game_state['player_inventory']
    
    if inventory:
        item_index = pseudo_random(game_state['steps_taken'], len(inventory))
        lost_item = inventory.pop(item_index)
        print(f'Из вашего инвентаря выпал и потерялся: {lost_item}')
    else:
        chance = pseudo_random(game_state['steps_taken'], 10)
        if chance < 3:
            print('Вы не удержались и упали в пропасть! Игра окончена.')
            game_state['game_over'] = True
        else:
            print('Вам чудом удалось удержаться! Вы уцелели.')


def random_event(game_state):
    """Случайные события при перемещении."""
    # 10% шанс события
    if pseudo_random(game_state['steps_taken'], 10) != 0:
        return
    
    event_type = pseudo_random(game_state['steps_taken'] + 1, 3)
    current_room = game_state['current_room']
    inventory = game_state['player_inventory']
    
    match event_type:
        case 0:  # Находка
            print('\n Вы заметили что-то блестящее на полу...')
            ROOMS[current_room]['items'].append('coin')
            print('Вы нашли монетку! Она добавлена в комнату.')
        
        case 1:  # Испуг
            print('\n Вы слышите странный шорох...')
            if 'sword' in inventory:
                print('Вы достаете меч, и шорох мгновенно стихает.')
            else:
                print('Шорох становится громче... Вам стало не по себе.')
        
        case 2:  # Ловушка
            if current_room == 'trap_room' and 'torch' not in inventory:
                print('\n Вы чувствуете, что наступили на что-то подозрительное...')
                trigger_trap(game_state)
