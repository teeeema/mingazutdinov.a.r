# Практическое занятие №1. Введение, основы работы в командной строке

## Задача 1

Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).

![Задание 1](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_1/1.jpg)

## Задача 2

Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов, как показано в примере ниже:

![Задание 2](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_1/2.jpg)

## Задача 3

Написать программу banner средствами bash для вывода текстов, как в следующем примере (размер баннера должен меняться!):

![Задание 2](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_1/3.jpg)

```
#!/bin/bash
if [ $# -eq 0 ]; then
    echo "Использование: $0 \"текст\""
    exit 1
fi
TEXT="$1"
TEXT_LENGTH=${#TEXT}
BANNER_LENGTH=$((TEXT_LENGTH + 4))
echo "+$(printf "%-${TEXT_LENGTH}s" "" | tr ' ' '-')+"
echo "| ${TEXT} |"
echo "+$(printf "%-${TEXT_LENGTH}s" "" | tr ' ' '-')+"
```

## Задача 4

Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).

![Задание 4](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_1/4.jpg)

```
#!/bin/bash
file="$1"
identifiers=$(grep -o -E '\b[a-zA-Z]*\b' "$file" | sort -u)
echo "Идентификаторы:"
echo "$identifiers"
```

## Задача 5

Написать программу для регистрации пользовательской команды (правильные права доступа и копирование в /usr/local/bin).

![Задание 5](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_1/5.jpg)

```
#!/bin/bash
file=$1
chmod 755 "./$file"
sudo cp "$file" /usr/local/bin/
```

## Задача 6

Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.

![Задание 6](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_1/6.jpg)

```
#!/bin/bash
for file in *.c *.js *.py; do
    line=$(head -n 1 "$file")
    if [[ $line == "#"* || $line == "//"* || $line == "/*"* ]]; then
        echo "Файл $file начинается с комментария"
    else
        echo "Файл $file не начинается с комментария"
    fi
done
```

## Задача 7

Написать программу для нахождения файлов-дубликатов (имеющих 1 или более копий содержимого) по заданному пути (и подкаталогам).

![Задание 7](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_1/7.jpg)

```
#!/bin/bash

# Хеш-таблица
declare -A duplicats

# Рекурсивная функция для поиска и вывода дубликатов
findDuplicates() 
{
    local dir="$1"
    for file in "$dir"/*; do
        if [[ -f "$file" ]]; then
            file=$(basename "$file")
            if [ duplicats["$file"] ]; then
                duplicats["$file"]=$((duplicats["$file"] + 1))
            else
                duplicats["$file"]=1
            fi
            if [ "${duplicats["$file"]}" -eq 2 ]; then
                echo "Файл-дубликат - '$file'"
            fi
        elif [[ -d "$file" ]]; then
            findDuplicates "$file"
        fi
    done
}
findDuplicates "."
```

## Задача 8

Написать программу, которая находит все файлы в данном каталоге с расширением, указанным в качестве аргумента и архивирует все эти файлы в архив tar.

![Задание 8](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_1/8.jpg)

```
#!/bin/bash
files=( $(find . -type f -name "*.$1") )
tar -cvf "archive.tar" "${files[@]}"
echo "Архив создан"
```

## Задача 9

Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.

![Задание 9](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_1/9.jpg)

```
#!/bin/bash
# sed s/что_заменять/на_что_заменять/опции
# g - Замените все вхождения строки в файле
# > - передача вывода второму аргументу
sed 's/    /\t/g' "$1" > "$2"
# Выводим сообщение об успешном завершении скрипта
echo "Файл исправлен"
```

## Задача 10

Написать программу, которая выводит названия всех пустых текстовых файлов в указанной директории. Директория передается в программу параметром. 

![Задание 10](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_1/10.jpg)

```
#!/bin/bash
# Итерируемся по всем файлам в директории, проверяем, что это текстовый файл и он пустой
for file in "$1"/*; do
    # Если найден файл и данный файл имеет размер 0 (т.е -s - true, если размер файла больше 0), 
    if [[ -f "$file" && ! -s "$file" ]]; then
        echo "Пустой файл: $file"
    fi
done
```
