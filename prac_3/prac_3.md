# Практическое занятие №3.

П.Н. Советов, РТУ МИРЭА

## Задача 1

![Задание 1](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_2/1.jpg)

```
{
  "groups": [
    "ИКБО-1-20",
    "ИКБО-2-20",
    ...
  ],
  "students": [
    {
      "age": 19,
      "group": "ИКБО-4-20",
      "name": "Иванов И.И."
    },
    ...
  ],
  "subject": "Конфигурационное управление"
}
```

## Задача 2

![Задание 3](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_2/2.jpg)

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

![Задание 3](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_2/3.png)

```

```

## Задача 4

![Задание 4](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_2/4.jpg)

```

```

## Задача 5

![Задание 5](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_2/5.jpg)

```

```

