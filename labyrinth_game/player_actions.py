def show_inventory(game_state):
    if not game_state['player_inventory']:
        print('Инвентарь пуст.')
    elif game_state['player_inventory']:
        print(f'Инвентарь игрока: {', '.join(game_state['player_inventory'])}')

def get_input(prompt="> "):
    try:
        pass
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit" 
