### Задача 1
Написать программу на Питоне, которая транслирует граф зависимостей civgraph в makefile в духе примера выше. Для мало знакомых с Питоном используется упрощенный вариант civgraph: civgraph.json.

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

# Функция генерации Makefile с проверкой на уже выполненные задачи
def generate_makefile(civgraph, target):
    visited = set()
    result = []
    completed_tasks = load_completed_tasks()

    def visit(tech):
        if tech in visited or tech in completed_tasks:
            return
        visited.add(tech)
        for dep in civgraph.get(tech, []):
            visit(dep)
        result.append(tech)

    visit(target)

    for task in result:
        if task not in completed_tasks:
            print(task)
            completed_tasks.add(task)

    save_completed_tasks(completed_tasks)

if __name__ == '__main__':
    civgraph = load_civgraph('civgraph.json')
    target = input('Enter the target technology: ')
    generate_makefile(civgraph, target)
```


### Задача 3
Добавить цель clean, не забыв и про "животное".

```
import json
import os

COMPLETED_TASKS_FILE = "completed_tasks.txt"

def load_completed_tasks():
    if os.path.exists(COMPLETED_TASKS_FILE):
        with open(COMPLETED_TASKS_FILE, 'r') as f:
            return set(f.read().splitlines())
    return set()

def save_completed_tasks(completed_tasks):
    with open(COMPLETED_TASKS_FILE, 'w') as f:
        f.write('\n'.join(completed_tasks))

def clean():
    if os.path.exists(COMPLETED_TASKS_FILE):
        os.remove(COMPLETED_TASKS_FILE)
        print("Cleaned completed tasks.")

def generate_makefile(civgraph, target):
    visited = set()
    result = []
    completed_tasks = load_completed_tasks()

    def visit(tech):
        if tech in visited or tech in completed_tasks:
            return
        visited.add(tech)
        for dep in civgraph.get(tech, []):
            visit(dep)
        result.append(tech)

    visit(target)

    for task in result:
        if task not in completed_tasks:
            print(task)
            completed_tasks.add(task)

    save_completed_tasks(completed_tasks)

if __name__ == '__main__':
    civgraph = load_civgraph('civgraph.json')
    action = input('Enter action (make/clean): ')

    if action == 'clean':
        clean()
    else:
        target = input('Enter the target technology: ')
        generate_makefile(civgraph, target)
```

### Задача 4
Написать makefile для следующего скрипта сборки:

```
CC=gcc  # Или другой компилятор, например, clang
CFLAGS=-o prog
SRC=prog.c data.c
ARCHIVE=distr.zip

# Цель по умолчанию
all: prog files.lst archive

# Компиляция программы
prog: $(SRC)
	$(CC) $(SRC) $(CFLAGS)

# Создание списка файлов
files.lst:
	dir /B > files.lst  # В Windows используется команда dir. Для Linux: ls > files.lst

# Архивация проекта
archive: prog files.lst
	7z a $(ARCHIVE) *.*

# Очистка проекта
clean:
	del prog.exe files.lst $(ARCHIVE)  # В Windows используется команда del. Для Linux: rm -f prog files.lst $(ARCHIVE)
```
