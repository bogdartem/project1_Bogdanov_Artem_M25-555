#!/usr/bin/env python3
from labyrinth_game.utils import describe_current_room
# import labyrinth_game.constants
# import labyrinth_game.player_actions


def main():
    """Main function of the labyrinth game."""
    # print("Первая попытка запустить проект!")
    game_state = {
        'player_inventory': [],  # Инвентарь игрока
        'current_room': 'entrance',  # Текущая комната
        'game_over': False,  # Значения окончания игры
        'steps_taken': 0  # Количество шагов
    }
    describe_current_room(game_state)


if __name__ == "__main__":
    main()
