### Задача 1
Написать программу на Питоне, которая транслирует граф зависимостей civgraph в makefile в духе примера выше. Для мало знакомых с Питоном используется упрощенный вариант civgraph: civgraph.json.

![Задание 1](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_6/1.jpg)

```
import json
def load_civgraph(file):
    with open(file, 'r') as f:
        return json.load(f)
def generate_makefile(civgraph, target):
    visited = set()    
    stack = set()       
    result = []         
    dependencies = {}    
    def visit(tech):
        if tech in stack:
            raise ValueError(f"Cycle detected in dependencies involving '{tech}'")
        if tech in visited:
            return
        stack.add(tech) 
        visited.add(tech)
        deps = civgraph.get(tech, [])
        dependencies[tech] = deps
        for dep in deps:
            visit(dep)
        result.append(tech)
        stack.remove(tech)   
    visit(target)
    print("### Generated Makefile ###\n")
    for task in reversed(result): 
        deps = " ".join(dependencies[task])
        print(f"{task}: {deps}")
    print("\n### End of Makefile ###")
if __name__ == '__main__':
    try:
        civgraph = load_civgraph('civgraph.json')
        target = input('Enter the target technology: ') 
        generate_makefile(civgraph, target)
    except ValueError as e:
        print("Error:", e)
    except FileNotFoundError:
        print("Error: civgraph.json file not found.")
    except json.JSONDecodeError:
        print("Error: Failed to parse civgraph.json. Please check the JSON format.")

```

### Задача 2
Реализовать вариант трансляции, при котором повторный запуск make не выводит для civgraph на экран уже выполненные "задачи".

![Задание 2](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_6/2.jpg)


```
import json
import os

# Файл для сохранения выполненных задач
COMPLETED_TASKS_FILE = "completed_tasks.txt"

# Загрузка списка выполненных задач из файла
def load_completed_tasks():
    if os.path.exists(COMPLETED_TASKS_FILE):
        with open(COMPLETED_TASKS_FILE, 'r') as f:
            return set(f.read().splitlines())
    return set()

# Сохранение выполненных задач в файл
def save_completed_tasks(completed_tasks):
    with open(COMPLETED_TASKS_FILE, 'w') as f:
        f.write('\n'.join(completed_tasks))

# Загрузка графа зависимостей из JSON-файла
def load_civgraph(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Функция генерации Makefile с проверкой на уже выполненные задачи
def generate_makefile(civgraph, target):
    visited = set()  # Множество для отслеживания посещенных узлов
    result = []      # Список для хранения задач в порядке выполнения
    completed_tasks = load_completed_tasks()  # Загружаем выполненные задачи

    # Рекурсивная функция для обхода зависимостей
    def visit(tech):
        # Если задача уже посещена или выполнена ранее, пропускаем её
        if tech in visited or tech in completed_tasks:
            return
        visited.add(tech)
        # Рекурсивный вызов для зависимых задач
        for dep in civgraph.get(tech, []):
            visit(dep)
        # Добавляем задачу в итоговый список для выполнения
        result.append(tech)

    # Запускаем обход графа с целевой задачи
    visit(target)

    # Выводим и сохраняем только невыполненные задачи
    for task in result:
        if task not in completed_tasks:
            print(task)  # Печатаем задачу
            completed_tasks.add(task)  # Добавляем задачу в список выполненных

    # Сохраняем обновленный список выполненных задач
    save_completed_tasks(completed_tasks)

if name == 'main':
    # Загружаем граф зависимостей из файла
    civgraph = load_civgraph('civgraph.json')
    # Запрашиваем у пользователя целевую задачу
    target = input('Введите целевую технологию: ')
    # Генерируем Makefile с учетом выполненных задач
    generate_makefile(civgraph, target)
```

```
{
    "mathematics": ["mysticism", "drama_poetry"],
    "mysticism": ["polytheism"],
    "drama_poetry": ["writing"],
    "writing": ["code_of_laws"],
    "code_of_laws": ["foreign_trade"],
    "foreign_trade": ["currency"],
    "currency": ["sailing"],
    "sailing": ["celestial_navigation"],
    "celestial_navigation": ["astrology"],
    "astrology": ["bronze_working"],
    "bronze_working": ["mining"],
    "mining": []
}

```


### Задача 3
Добавить цель clean, не забыв и про "животное".

![Задание 3](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_6/3.jpg)

```
import json
import os
import sys
sys.stdin.reconfigure(encoding='utf-8')

# Файл для сохранения выполненных задач
COMPLETED_TASKS_FILE = "completed_tasks.txt"

# Загрузка списка выполненных задач из файла
def load_completed_tasks():
    if os.path.exists(COMPLETED_TASKS_FILE):
        with open(COMPLETED_TASKS_FILE, 'r') as f:
            return set(f.read().splitlines())
    return set()

# Сохранение выполненных задач в файл
def save_completed_tasks(completed_tasks):
    with open(COMPLETED_TASKS_FILE, 'w') as f:
        f.write('\n'.join(completed_tasks))

# Загрузка графа зависимостей из JSON-файла
def load_civgraph(filename):
    if not os.path.exists(filename):
        print(f"Файл '{filename}' не найден. Пожалуйста, убедитесь, что файл существует.")
        return {}
    with open(filename, 'r') as f:
        return json.load(f)

# Очищает список выполненных задач
def clean():
    if os.path.exists(COMPLETED_TASKS_FILE):
        os.remove(COMPLETED_TASKS_FILE)
        print("Список выполненных задач очищен.")
    else:
        print("Список выполненных задач уже пуст.")

# Функция генерации Makefile с проверкой на уже выполненные задачи
def generate_makefile(civgraph, target):
    visited = set()  # Множество для отслеживания посещенных узлов
    result = []      # Список для хранения задач в порядке выполнения
    completed_tasks = load_completed_tasks()  # Загружаем выполненные задачи

    # Рекурсивная функция для обхода зависимостей
    def visit(tech):
        # Если задача уже посещена или выполнена ранее, пропускаем её
        if tech in visited or tech in completed_tasks:
            return
        visited.add(tech)
        # Рекурсивный вызов для зависимых задач
        for dep in civgraph.get(tech, []):
            visit(dep)
        # Добавляем задачу в итоговый список для выполнения
        result.append(tech)

    # Запускаем обход графа с целевой задачи
    visit(target)

    # Выводим и сохраняем только невыполненные задачи
    for task in result:
        if task not in completed_tasks:
            print(task)  # Печатаем задачу
            completed_tasks.add(task)  # Добавляем задачу в список выполненных

    # Сохраняем обновленный список выполненных задач
    save_completed_tasks(completed_tasks)

if name == 'main':
    # Загружаем граф зависимостей из файла
    civgraph = load_civgraph('civgraph.json')
    # Запрашиваем у пользователя действие: 'make' для выполнения или 'clean' для очистки
    action = input("Введите 'make' для сборки, 'clean' для очистки: ").strip().lower()
    
    if action == 'clean':
        clean()  # Запускаем очистку списка выполненных задач
    elif action == 'make':
        target = input('Введите целевую технологию: ')
        generate_makefile(civgraph, target)
    else:
        print("Неверная команда. Используйте 'make' для сборки или 'clean' для очистки.")
```

### Задача 4
Написать makefile для следующего скрипта сборки:

```
# Компилятор и его флаги
CC = gcc
CFLAGS = -o prog

# Названия файлов и архивов
OBJ_FILES = data.c prog.c
PROG = prog
FILE_LIST = files.lst
ARCHIVE = distrib.zip

# Основное правило: сборка программы
all: $(PROG) $(FILE_LIST) $(ARCHIVE)

# Правило для компиляции программы
$(PROG): $(OBJ_FILES)
	$(CC) $(OBJ_FILES) $(CFLAGS)

# Создание списка файлов
$(FILE_LIST):
	@echo "Creating file list..."
	dir /b > $(FILE_LIST) # Команда для Windows
	# Для Unix-систем можно использовать:
	# ls > $(FILE_LIST)

# Создание архива
$(ARCHIVE): $(FILE_LIST)
	@echo "Creating archive..."
	7z a $(ARCHIVE) $(FILE_LIST)

# Команда для очистки всех сгенерированных файлов
clean:
	@echo "Cleaning up..."
	rm -f $(PROG) $(FILE_LIST) $(ARCHIVE) # Команда для Unix
	# del $(PROG) $(FILE_LIST) $(ARCHIVE) # Команда для Windows
```
