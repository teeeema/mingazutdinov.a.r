# Практическое занятие №1. Введение, основы работы в командной строке

## Задача 1

Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).

![Задание 1](https://github.com/teeeema/mingazutdinov.a.r/blob/main/1.jpg)

## Задача 2

Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов, как показано в примере ниже:

![Задание 2](https://github.com/teeeema/mingazutdinov.a.r/blob/main/2.jpg)

## Задача 3

Написать программу banner средствами bash для вывода текстов, как в следующем примере (размер баннера должен меняться!):

![Задание 2](https://github.com/teeeema/mingazutdinov.a.r/blob/main/3.jpg)

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

![Задание 4](https://github.com/teeeema/mingazutdinov.a.r/blob/main/4.jpg)

```
#!/bin/bash
file="$1"
identifiers=$(grep -o -E '\b[a-zA-Z]*\b' "$file" | sort -u)
echo "Идентификаторы:"
echo "$identifiers"
```

## Задача 5

Написать программу для регистрации пользовательской команды (правильные права доступа и копирование в /usr/local/bin).

![Задание 5](https://github.com/teeeema/mingazutdinov.a.r/blob/main/5.jpg)

```
#!/bin/bash
file=$1
chmod 755 "./$file"
sudo cp "$file" /usr/local/bin/
```

## Задача 6

Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.

```
#!/bin/bash
if [ -z "$1" ]; then
    echo "Использование: $0 <каталог>"
    exit 1
fi
DIR=$1
find "$DIR" -type f \( -name "*.c" -o -name "*.js" -o -name "*.py" \) | while read -r file; do
    first_line=$(head -n 1 "$file")
    if [[ "$file" == *.py && "$first_line" =~ ^# ]]; then
        echo "Файл $file: содержит комментарий в первой строке."
    elif [[ "$file" == *.c && ("$first_line" =~ ^// || "$first_line" =~ ^/\*) ]]; then
        echo "Файл $file: содержит комментарий в первой строке."
    elif [[ "$file" == *.js && "$first_line" =~ ^// ]]; then
        echo "Файл $file: содержит комментарий в первой строке."
    else
        echo "Файл $file: не содержит комментарий в первой строке."
    fi
done
```

## Задача 7

Написать программу для нахождения файлов-дубликатов (имеющих 1 или более копий содержимого) по заданному пути (и подкаталогам).

```
#!/bin/bash
if [ -z "$1" ]; then
    echo "Использование: $0 <каталог>"
    exit 1
fi
DIR=$1
declare -A file_hashes
find "$DIR" -type f | while read -r file; do
    file_hash=$(sha256sum "$file" | awk '{print $1}')
    if [[ -n "${file_hashes[$file_hash]}" ]]; then
        echo "Найден дубликат: $file"
        echo "Оригинал: ${file_hashes[$file_hash]}"
    else
        file_hashes["$file_hash"]=$file
    fi
done
```

## Задача 8

Написать программу, которая находит все файлы в данном каталоге с расширением, указанным в качестве аргумента и архивирует все эти файлы в архив tar.

```
#!/bin/bash
if [ "$#" -ne 2 ]; then
    echo "Использование: $0 <каталог> <расширение>"
    exit 1
fi
DIR=$1
EXTENSION=$2
ARCHIVE_NAME="archive_$(date +%Y%m%d_%H%M%S).tar"
find "$DIR" -type f -name "*.$EXTENSION" | tar -cvf "$ARCHIVE_NAME" -T -
if [ $? -eq 0 ]; then
    echo "Файлы с расширением .$EXTENSION успешно архивированы в $ARCHIVE_NAME"
else
    echo "Ошибка при создании архива"
    exit 1
fi
```

## Задача 9

Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.

```
#!/bin/bash
if [ "$#" -ne 2 ]; then
    echo "Использование: $0 <входной_файл> <выходной_файл>"
    exit 1
fi
INPUT_FILE=$1
OUTPUT_FILE=$2
if [ ! -f "$INPUT_FILE" ]; then
    echo "Ошибка: входной файл '$INPUT_FILE' не существует."
    exit 1
fi
sed 's/    /\t/g' "$INPUT_FILE" > "$OUTPUT_FILE"
if [ $? -eq 0 ]; then
    echo "Замена успешно выполнена. Результат сохранён в '$OUTPUT_FILE'."
else
    echo "Ошибка при обработке файла."
    exit 1
fi
```

## Задача 10

Написать программу, которая выводит названия всех пустых текстовых файлов в указанной директории. Директория передается в программу параметром. 

```
#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Использование: $0 <директория>"
    exit 1
fi
DIR=$1
if [ ! -d "$DIR" ]; then
    echo "Ошибка: Директория '$DIR' не существует."
    exit 1
fi
find "$DIR" -type f -name "*.txt" -empty
if [ $? -eq 0 ]; then
    echo "Поиск завершён."
else
    echo "Ошибка при поиске."
    exit 1
fi

```
