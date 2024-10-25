# Практическое занятие №3.

П.Н. Советов, РТУ МИРЭА

## Задача 1

Реализовать на Jsonnet приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.

![Задание 1](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_3/1.jpg)

```
{
 {
  groups: [
    "ИКБО-12-20", "ИКБО-13-20", "ИКБО-14-20", "ИКБО-15-20",
    "ИКБО-16-20", "ИКБО-17-20", "ИКБО-18-20", "ИКБО-19-20",
    "ИКБО-20-20", "ИКБО-21-20", "ИКБО-22-20", "ИКБО-23-20",
    "ИКБО-24-20", "ИКБО-25-20"
  ],
  students: [
    {
      age: 18,
      group: "ИКБО-10-20",
      name: "Василев И.И."
    },
    {
      age: 18,
      group: "ИКБО-5-20",
      name: "Петров П.П."
    },
    {
      age: 18,
      group: "ИКБО-20-20",
      name: "Сидоров С.С."
    },
    {
      age: 18,
      group: "ИКБО-10-20",
      name: "Смирнов А.А."
    }
  ],
  subject: "Конфигурационное управление"
}
```

## Задача 2

Реализовать на Dhall приведенный выше пример в формате JSON. Использовать в реализации свойство программируемости и принцип Dry

![Задание 3](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_3/2.1.jpg)
![Задание 3](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_3/2.2.jpg)

```
let List/groups =
      [ "ИКБО-12-20"
      , "ИКБО-13-20"
      , "ИКБО-14-20"
      , "ИКБО-15-20"
      , "ИКБО-16-20"
      , "ИКБО-17-20"
      , "ИКБО-18-20"
      , "ИКБО-19-20"
      , "ИКБО-20-20"
      , "ИКБО-21-20"
      , "ИКБО-22-20"
      , "ИКБО-23-20"
      , "ИКБО-24-20"
      , "ИКБО-25-20"
      ]
let students =
      [ { age = 18, group = "ИКБО-10-20", name = "Василев И.И." }
      , { age = 18, group = "ИКБО-5-20", name = "Петров П.П." }
      , { age = 18, group = "ИКБО-20-20", name = "Сидоров С.С." }
      , { age = 18, group = "ИКБО-10-20", name = "Смирнов А.А." }
      ]
let subject = "Конфигурационное управление"
in { groups = List/groups, students = students, subject = subject }
```

## Задача 3

Для решения дальнейших задач потребуется программа на Питоне, представленная в методичке к 3 практической работе. Разбираться в самом языке Питон при этом необязательно.
Реализовать грамматики, описывающие следующие языки (для каждого решения привести БНФ). Код решения должен содержаться в переменной BNF:

Язык нулей и единиц.
10
100
11
101101
000

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

Язык правильно расставленных скобок двух видов.
(({((()))}))
{}
{()}
()
{}

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

Язык выражений алгебры логики.
((~(y & x)) | (y) & ~x | x) & x
у & ~ (у)
((y) & y & ~y)
~x
~((x) & y | (y) | (x)) & x | x | (y & ~y)

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

