# Установка зависимостей
install:
	poetry install

# Запуск проекта
project:
	poetry run project

# Запуск напрямую через Python
run:
	poetry run python -m labyrinth_game.main

# Активация виртуального окружения
shell:
	poetry shell

# Запуск тестов (если будут)
test:
	poetry run pytest

# Форматирование кода (если установлен black)
format:
	poetry run black labyrinth_game/

# Проверка стиля кода (если установлен flake8)
lint:
	poetry run flake8 labyrinth_game/

# Очистка временных файлов
clean:
	rm -rf __pycache__
	rm -rf labyrinth_game/__pycache__
	rm -rf .pytest_cache

# Показать help
help:
	@echo "Доступные команды:"
	@echo "  make install    - установить зависимости"
	@echo "  make project    - запустить проект"
	@echo "  make run        - запустить через Python"
	@echo "  make shell      - активировать виртуальное окружение"
	@echo "  make test       - запустить тесты"
	@echo "  make clean      - очистить временные файлы"