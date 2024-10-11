# Практическое занятие №2. Менеджеры пакетов

П.Н. Советов, РТУ МИРЭА

## Задача 1

Вывести служебную информацию о пакетах matplotlib. Разобрать основные элементы содержимого фацла со служебной информацией из пакета. Как получить пакет без манеджера пакетов, прямо из репозитория?

![Задание 1](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_2/1.jpg)

```
pip install git+https://github.com/matplotlib/matplotlib.git
cd matplotlib
python setup.py install
```

## Задача 2

Вывести служебную информацию о пакетах express. Разобрать основные элементы содержимого файла со служебной информацией пакета. Как получить пакет без менеджреа пакетов, прямо из репозитория?

![Задание 3](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_2/2.jpg)

## Задача 3

Сформировать graphiz-код и получить изображения зависимостей matplotlib и express

![Задание 3](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_2/3.png)

```
digraph matplotlib_deps {
    node [shape=box, style=filled, color=lightblue];
    "matplotlib" -> "numpy";
    "matplotlib" -> "pyparsing";
    "matplotlib" -> "cycler";
    "matplotlib" -> "pillow";
    "matplotlib" -> "kiwisolver";
    "matplotlib" -> "python-dateutil";
    "matplotlib" -> "six";
    "numpy" [color=lightyellow];
    "pyparsing" [color=lightyellow];
    "cycler" [color=lightyellow];
    "pillow" [color=lightyellow];
    "kiwisolver" [color=lightyellow];
    "python-dateutil" [color=lightyellow];
    "six" [color=lightyellow];
}
```

## Задача 4

Изучить основы программирования в ограничениях. Решить задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными. Найти минимальное решение для суммы 3 цифр.

![Задание 4](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_2/4.jpg)

```
include "globals.mzn";  
array[1..6] of var 0..9: digits;
constraint all_different(digits);
constraint
  digits[1] + digits[2] + digits[3] = digits[4] + digits[5] + digits[6];
var int: sum_digits = digits[1] + digits[2] + digits[3];
solve minimize sum_digits;
output [
  "Билет: \(show(digits[1]))\(show(digits[2]))\(show(digits[3]))\(show(digits[4]))\(show(digits[5]))\(show(digits[6]))\n",
  "Сумма цифр: \(sum_digits)\n"
];
```

## Задача 5

Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.

![Задание 5](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_2/5.jpg)

```
enum Menu = { M1_0_0, M1_1_0, M1_2_0, M1_3_0, M1_4_0, M1_5_0 };
enum Dropdown = { D1_8_0, D2_0_0, D2_1_0, D2_2_0, D2_3_0 };
enum Icons = { I1_0_0, I2_0_0 };
var Menu: selected_menu;
var Dropdown: selected_dropdown;
var Icons: selected_icons;
constraint
    (selected_menu == M1_0_0 -> selected_dropdown == D1_8_0 /\ selected_icons == I1_0_0) /\
    (selected_menu == M1_1_0 -> selected_dropdown == D1_8_0 /\ selected_icons == I1_0_0) /\
    (selected_menu == M1_2_0 -> selected_dropdown == D2_0_0 /\ selected_icons == I2_0_0) /\
    (selected_menu == M1_3_0 -> selected_dropdown == D2_1_0 /\ selected_icons == I2_0_0) /\
    (selected_menu == M1_4_0 -> selected_dropdown == D2_2_0 /\ selected_icons == I2_0_0) /\
    (selected_menu == M1_5_0 -> selected_dropdown == D2_3_0 /\ selected_icons == I2_0_0);
solve satisfy;
output [
    "Menu version: ", show(selected_menu), "\n",
    "Dropdown version: ", show(selected_dropdown), "\n",
    "Icons version: ", show(selected_icons), "\n"
];
```

## Задание 6

Решить на MiniZinc задачу о зависимостях пакетов для следующих данных:

![Задание 6](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_2/6.jpg)

```
int: root = 100;
var 100..300: foo;
var 100..300: target;
var 100..300: right;
var 100..300: left;
var 100..300: shared;
constraint
    if root = 100 then
        (foo >= 100 /\ foo < 200) /\ (target >= 200 /\ target < 300) endif;
constraint
    if (foo = 110) then
        (left >= 100 /\ left < 200) /\ (right >= 100 /\ right < 200) endif;
constraint    
    if (foo = 100) then true endif;
constraint
    if (left = 100) then
        shared >= 100 endif;     
constraint
    if (right = 100) then
        shared < 200 endif;    
constraint    
    if (shared = 200) then true endif;
constraint
    if (shared = 100) then
       (target >= 100 /\ target < 200) endif;   
constraint    
    if (target = 100 \/ target = 200) then true endif;
solve satisfy;
```

## Задание 7

```

```

