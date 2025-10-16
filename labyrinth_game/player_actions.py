from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room


def show_inventory(game_state):
    if not game_state['player_inventory']:
        print('Инвентарь пуст.')
    elif game_state['player_inventory']:
        print(f'Инвентарь игрока: {', '.join(game_state['player_inventory'])}')


def get_input(prompt='> '):
    try:
        pass  # дописать
    except (KeyboardInterrupt, EOFError):
        print('Выход из игры.')
        return 'quit' 


def move_player(game_state, direction: str):
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    if direction in room_data['exits'].keys():
        print('\nВыход в другую комнату есть\n')
        game_state['current_room'] = room_data['exits'][direction]  # Обновите текущую комнату.
        game_state['steps_taken'] += 1  # Увеличьте шаг на единицу.
        describe_current_room(game_state)  # Выведите описание новой комнаты.
    elif direction not in room_data['exits'].keys():
        print('Нельзя пойти в этом направлении.')
    pass  # дописать
