#!/usr/bin/env python3
from labyrinth_game.player_actions import (
    get_input,
    move_player,
    show_inventory,
    take_item,
    use_item
)
from labyrinth_game.utils import (
    attempt_open_treasure, describe_current_room, solve_puzzle, show_help
)


def process_command(game_state, command):
    """Обработка команд пользователя."""
    parts = command.split()
    if not parts:
        return

    action = parts[0]
    argument = parts[1] if len(parts) > 1 else None

    match action:
        case 'look':
            describe_current_room(game_state)

        case 'go' if argument:
            move_player(game_state, argument)
            describe_current_room(game_state)

        case 'take' if argument:
            take_item(game_state, argument)

        case 'solve':
            if game_state['current_room'] == 'treasure_room':
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)

        case 'inventory':
            show_inventory(game_state)

        case 'use' if argument:
            use_item(game_state, argument)

        case 'quit' | 'exit':
            game_state['game_over'] = True
            print('Спасибо за игру!')

        case 'help':
            show_help()

        case _:
            print('Неизвестная команда. Введите "help" для списка команд.')


def main():
    """Функция main игры Лабиринт сокровищ."""
    print('Добро пожаловать в Лабиринт сокровищ!')

    game_state = {
        'player_inventory': [],  # Инвентарь игрока
        'current_room': 'entrance',  # Текущая комната
        'game_over': False,  # Значения окончания игры
        'steps_taken': 0  # Количество шагов
    }
    describe_current_room(game_state)

    while not game_state['game_over']:
        command = get_input('\nВведите команду: ')
        process_command(game_state, command)


if __name__ == '__main__':
    main()
