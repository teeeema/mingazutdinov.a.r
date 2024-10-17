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
let GroupPrefix = "ИКБО"
let Year = "20"
let makeGroup = λ(n : Natural) → GroupPrefix ++ "-" ++ Natural/show n ++ "-" ++ Year
let groups = 
      [ makeGroup 1
      , makeGroup 2
      , makeGroup 3
      , makeGroup 4
      , makeGroup 5
      , makeGroup 6
      , makeGroup 7
      , makeGroup 8
      , makeGroup 9
      , makeGroup 10
      , makeGroup 11
      , makeGroup 12
      , makeGroup 13
      , makeGroup 14
      , makeGroup 15
      , makeGroup 16
      , makeGroup 17
      , makeGroup 18
      , makeGroup 19
      , makeGroup 20
      , makeGroup 21
      , makeGroup 22
      , makeGroup 23
      , makeGroup 24
      ]
let students =
      [ { age = 19, group = makeGroup 4, name = "Иванов И.И." }
      , { age = 18, group = makeGroup 5, name = "Петров П.П." }
      , { age = 18, group = makeGroup 5, name = "Сидоров С.С." }
      ]
let subject = "Конфигурационное управление"
in { groups = groups, students = students, subject = subject }
```

## Задача 3

![Задание 3](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_3/3.png)

```

```

## Задача 4

![Задание 4](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_3/4.jpg)

```

```

## Задача 5

![Задание 5](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_3/5.jpg)

```

```

