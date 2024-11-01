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
