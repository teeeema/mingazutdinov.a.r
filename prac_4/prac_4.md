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
92604@Matebook-Tema MINGW64 ~
$ mkdir my

92604@Matebook-Tema MINGW64 ~
$ cd my

92604@Matebook-Tema MINGW64 ~/my
$ git init
Initialized empty Git repository in C:/Users/92604/my/.git/

92604@Matebook-Tema MINGW64 ~/my (master)
$ git config user.name "mingazutdinov.a.r"

92604@Matebook-Tema MINGW64 ~/my (master)
$ git config user.email "9260410487am@mail.ru"

92604@Matebook-Tema MINGW64 ~/my (master)
$ nano prog.py

92604@Matebook-Tema MINGW64 ~/my (master)
$ git config --global core.autocrlf false

92604@Matebook-Tema MINGW64 ~/my (master)
$ git add prog.py

92604@Matebook-Tema MINGW64 ~/my (master)
$ git commit -m "Добавление фвйла"
[master (root-commit) c9b348f] Добавление фвйла
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py
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
