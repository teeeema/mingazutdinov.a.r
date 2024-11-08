# Практическое занятие №4.

П.Н. Советов, РТУ МИРЭА

## Задача 1

![Задание 1](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_4/1.jpg)

```
git commit ""
git branch first
git branch second
git tag in
git commit ""
git commit ""
git checkout first
git commit ""
git commit ""
git checkout second
git commit ""
git commit ""
git checkout master
git merge first
git checkout second
git rebase master  
```

## Задача 2

![Задание 2](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_4/2.1.jpg)


![Задание 2](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_4/2.2.jpg)


```
git init
git config user.name "tema"
git config user.email "92678am@mail.com"
echo 'print("Hello, World!")' > prog.py
git add prog.py
git commit -m "first commit"

# Создание bare-репозитория
mkdir -p repository
cd repository
git init --bare server

# Возвращение в основной репозиторий, подключение к серверу и пуш
cd ..
git remote add server repository/server
git remote -v
git push server master

# Клонирование серверного репозитория в клиентский
git clone repository/server repository/client
cd repository/client
git config user.name "tema2"
git config user.email "retuern@gmail.com"

# Добавление нового файла и коммит
echo "Author Information:" > readme.md
git add readme.md
git commit -m "docs"

# Переименование удаленного репозитория и пуш
git remote rename origin server
git push server master

# Возвращение в основной репозиторий, чтобы сделать pull
cd ..
git pull server master --no-rebase  # Используем merge вместо rebase

# Внесение изменений и пуш
echo "Author: 92678am@mail.com" >> readme.md
git add readme.md
git commit -m "92678am@mail.com info"
git push server master

# Переход в клиентский репозиторий и внесение изменений
cd client
echo "Author: retuern@gmail.com" >> readme.md
git add readme.md
git commit -m "retuern@gmail.com info"

# Перед `push` выполняем `pull` с merge, чтобы избежать линейной истории
git pull server master --no-rebase
git push server master

# Получение последних изменений с сервера
git pull server master --no-rebase

# Последний коммит и пуш исправлений в readme
git add readme.md
git commit -m "readme fix"
git push server master

# Переход к bare-репозиторию и просмотр истории
cd ..
cd server
git log -n 5 --graph --decorate --all
```


## Задача 3

![Задание 3](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_4/3.jpg)

```
git init --bare server.git
git remote add server ../server.git/
git remote -v
git push server master
git clone server.git coder2
echo "Test" >> readme.md
git add readme.md
git commit -m "test info"
git push server master
echo "Test2" >> readme.md
git add readme.md
git config user.name "coder2"
git config user.email "coder2@gmail.com"
git commit -m "test2 info"
git pull --no-rebase origin master
git add readme.md
git commit -m "Final"
git push origin master
git log --graph --all
```

## Задача 4

![Задание 4](https://github.com/teeeema/mingazutdinov.a.r/blob/main/prac_4/4.jpg)

```
import os
import subprocess

def get_git_objects():
    try:
        result = subprocess.run(
            ['git', 'rev-list', '--all'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        objects = result.stdout.splitlines()

        for obj in objects:
            print(f"Git Commit: {obj}")
            try:
                content = subprocess.run(
                    ['git', 'cat-file', '-p', obj],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    check=True
                )
                print(content.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Error {obj}: {e.stderr}")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

if __name__ == "__main__":
    if not os.path.exists('.git'):
        print("Git not found")
    else:
        get_git_objects()
```
