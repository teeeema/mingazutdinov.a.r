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

```
$ npm show express
name: 'express',
version: '4.18.2',
description: 'Fast, unopinionated, minimalist web framework',
main: 'index.js',
dependencies: {
  accepts: '^1.3.5',
  'array-flatten': '1.1.1',
  'body-parser': '1.20.0',
  'content-disposition': '0.5.4',
  // другие зависимости...
},
author: 'TJ Holowaychuk <tj@vision-media.ca>',
license: 'MIT',
repository: {
  type: 'git',
  url: 'git+https://github.com/expressjs/express.git'
},
homepage: 'https://expressjs.com/',
bugs: { url: 'https://github.com/expressjs/express/issues' },
maintainers: [ ... ],
keywords: [ 'express', 'framework', 'web', 'rest', 'http', 'node' ]
```

## Задача 3

Сформировать graphiz-код и получить изображения зависимостей matplotlib и express

![Задание 3](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_2/3.jpg)

```

```

## Задача 4

Изучить основы программирования в ограничениях. Решить задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными. Найти минимальное решение для суммы 3 цифр.

```

```

## Задача 5
