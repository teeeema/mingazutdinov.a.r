# Практическое занятие №3.

П.Н. Советов, РТУ МИРЭА

## Задача 1

![Задание 1](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_3/1.jpg)

```
{
  local groups = [
  "ИКБО-1-24",
  "ИКБО-2-24",
  "ИКБО-3-24",
  "ИКБО-4-24",
  "ИКБО-5-24",
  "ИКБО-6-24",
  "ИКБО-7-24",
  "ИКБО-8-24",
  "ИКБО-9-24",
  "ИКБО-10-24",
  "ИКБО-11-24",
  "ИКБО-12-24",
  "ИКБО-13-24",
  "ИКБО-14-24",
  "ИКБО-15-24",
  "ИКБО-16-24",
  "ИКБО-17-24",
  "ИКБО-18-24",
  "ИКБО-19-24",
  "ИКБО-20-24",
  "ИКБО-21-24",
  "ИКБО-22-24",
  "ИКБО-23-24",
  "ИКБО-24-24"
];
local student(name, age, group, subject) = {
  name: name,
  age: age,
  group: group,
  subject: subject,
};
local students = [
  student("Иванов И.И.", 19, "ИКБО-4-24", "Конфигурационное управление"),
  student("Петров П.П.", 18, "ИКБО-5-24", "Конфигурационное управление"),
  student("Сидоров С.С.", 18, "ИКБО-5-24", "Конфигурационное управление"),
  student("Лазаренко С.А.", 19, "ИКБО-6-24", "Конфигурационное управление")
];
{
  groups: groups,
  students: students,
}
```

## Задача 2

![Задание 3](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_3/2.jpg)

```
```

## Задача 3

![Задание 3](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_3/3.png)

```
import random
def parse_bnf(text):
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar
def generate_phrase(grammar, start):
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join(generate_phrase(grammar, name) for name in seq)
    return str(start)
BNF = """
E = "0" E | "1" E | ""
"""
for i in range(10):
    phrase = generate_phrase(parse_bnf(BNF), 'E')
    if phrase:
        print(phrase.replace('"', ''))
```

## Задача 4

![Задание 4](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_3/4.jpg)

```
import random
def parse_bnf(text):
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar
def generate_phrase(grammar, start, max_depth=10, current_depth=0):
    if current_depth > max_depth:
        return ""
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join(generate_phrase(grammar, name, max_depth, current_depth + 1) for name in seq)
    return str(start)
BNF = """
E = P E | F E | P | F 
P = "(" P ")" | "(" ")" 
F = "{" F "}" | "{}"
"""
for i in range(10):
    phrase = generate_phrase(parse_bnf(BNF), 'E')
    if phrase:
        print(phrase.replace('"', ''))
```

## Задача 5

![Задание 5](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_3/5.jpg)

```
import random

def parse_bnf(text):
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start, max_depth=10, current_depth=0):
    if current_depth > max_depth:
        return ""
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join(generate_phrase(grammar, name, max_depth, current_depth + 1) for name in seq)
    return str(start)

BNF = '''
E = ( E B F ) | U ( E ) | F
F = P B P | U P | P
P = x | y | (x) | (y)
U = ~
B = & | V
'''

def format_phrase(phrase):
    output = []
    prev_char = None
    open_count = 0
    for char in phrase:
        if char in ['x', 'y']:
            if prev_char in ['x', 'y']:
                continue
            output.append(char)
        elif char in ['&', '|']:
            if len(output) < 2 or output[-1] in ['&', '|'] or (prev_char in ['(', ')']):
                continue
            output.append(char)
        elif char == '(':
            if prev_char == '(':
                continue
            output.append(char)
            open_count += 1
        elif char == ')':
            if output and output[-1] == '(':
                output.pop()
                open_count -= 1
                continue
            if open_count > 0:
                output.append(char)
                open_count -= 1
        prev_char = char
    output = [c for c in output if not (c == '(' and (prev_char == '(' or (len(output) > 1 and output[-2] == '(')))]
    return ''.join(output)
for i in range(10):
    phrase = generate_phrase(parse_bnf(BNF), 'E')
    if phrase:
        formatted_phrase = format_phrase(phrase)
        if formatted_phrase:
            print(formatted_phrase.replace('"', ''))
```

