import csv
import os
from collections import defaultdict
import unittest
from collections import defaultdict

def read_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        config = {}
        for row in reader:
            key = row[0].strip()     # Убираем пробелы в начале и конце ключа
            value = row[1].strip()   # Убираем пробелы в начале и конце значения
            config[key] = value
        return config


# Получение зависимостей пакета (например, на основе файла Packages или словаря)
def get_dependencies(package, depth, max_depth, dependencies, visited):
    if depth >= max_depth:  # если достигли максимальной глубины, остановка
        return
    if package in visited:
        return
    visited.add(package)
    
    # Пример зависимостей
    package_dependencies = {
        'pkgA': ['pkgB', 'pkgC'],
        'pkgB': ['pkgD'],
        'pkgC': ['pkgD', 'pkgE'],
        'pkgD': [],
        'pkgE': ['pkgF'],
        'pkgF': []
    }

    for dep in package_dependencies.get(package, []):
        dependencies[package].add(dep)
        get_dependencies(dep, depth + 1, max_depth, dependencies, visited)


# Генерация кода для Graphviz
def generate_graphviz_code(dependencies):
    code = ["digraph dependencies {"]
    for pkg, deps in dependencies.items():
        for dep in deps:
            code.append(f'    "{pkg}" -> "{dep}";')
    code.append("}")
    return "\n".join(code)

# Основная функция для построения графа
def build_dependency_graph(config_path):
    # Чтение конфигурации
    config = read_config(config_path)
    package = config["Имя анализируемого пакета"]
    max_depth = int(config["Максимальная глубина анализа зависимостей"])
    output_file = config["Путь к файлу-результату в виде кода"]

    # Получение зависимостей
    dependencies = defaultdict(set)
    visited = set()
    get_dependencies(package, 0, max_depth, dependencies, visited)

    # Генерация Graphviz-кода
    graphviz_code = generate_graphviz_code(dependencies)
    print(graphviz_code)  # вывод на экран

    # Запись в файл
    with open(output_file, 'w') as f:
        f.write(graphviz_code)

# Тестирование
import unittest

class TestDependencyVisualizer(unittest.TestCase):
    def test_get_dependencies(self):
        # Определяем dependencies как defaultdict
        dependencies = defaultdict(set)
        # Запускаем функцию с нужными параметрами
        get_dependencies('pkgA', 0, 2, dependencies, set())
        
        # Ожидаемое значение для проверки
        expected = {
            'pkgA': {'pkgB', 'pkgC'},
            'pkgB': {'pkgD'},
            'pkgC': {'pkgD', 'pkgE'}
        }
        # Сравниваем результат функции с ожидаемым значением
        self.assertEqual(dict(dependencies), expected)

    # Дополнительные тесты могут быть добавлены здесь




    def test_generate_graphviz_code(self):
        dependencies = {
            'pkgA': {'pkgB', 'pkgC'},
            'pkgB': {'pkgD'},
        }
        generated_code = generate_graphviz_code(dependencies)
        
        expected_code = """
        digraph dependencies {
            "pkgA" -> "pkgB";
            "pkgA" -> "pkgC";
            "pkgB" -> "pkgD";
        }
        """
        
        # Убираем отступы и преобразуем строки в множества для неупорядоченного сравнения
        generated_lines = set(line.strip() for line in generated_code.strip().splitlines())
        expected_lines = set(line.strip() for line in expected_code.strip().splitlines())
        
        self.assertEqual(generated_lines, expected_lines)



if __name__ == "__main__":
    unittest.main()
