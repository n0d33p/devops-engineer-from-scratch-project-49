### Hexlet tests and linter status:
[![Actions Status](https://github.com/n0d33p/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/n0d33p/devops-engineer-from-scratch-project-49/actions)

# SonarQube

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=n0d33p_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=n0d33p_devops-engineer-from-scratch-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=n0d33p_devops-engineer-from-scratch-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=n0d33p_devops-engineer-from-scratch-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=n0d33p_devops-engineer-from-scratch-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=n0d33p_devops-engineer-from-scratch-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=n0d33p_devops-engineer-from-scratch-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=n0d33p_devops-engineer-from-scratch-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=n0d33p_devops-engineer-from-scratch-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=n0d33p_devops-engineer-from-scratch-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=n0d33p_devops-engineer-from-scratch-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=n0d33p_devops-engineer-from-scratch-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=n0d33p_devops-engineer-from-scratch-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=n0d33p_devops-engineer-from-scratch-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=n0d33p_devops-engineer-from-scratch-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=n0d33p_devops-engineer-from-scratch-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=n0d33p_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=n0d33p_devops-engineer-from-scratch-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=n0d33p_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=n0d33p_devops-engineer-from-scratch-project-49)

## 📖 Описание проекта

**Brain Games** — это набор из пяти консольных математических игр для развития мышления и проверки математических способностей. Каждая игра представляет собой серию из трех вопросов, на которые нужно дать правильные ответы подряд.

## 🎮 Доступные игры

1. **brain-even** — Определение четности числа
2. **brain-calc** — Вычисление результата выражения
3. **brain-gcd** — Нахождение наибольшего общего делителя
4. **brain-progression** — Поиск пропущенного числа в арифметической прогрессии
5. **brain-prime** — Определение простого числа

## ⚙️ Минимальные требования

- **Python** версии 3.10 или выше
- **pip** или **uv** для управления зависимостями
- **Git** для клонирования репозитория

## 🚀 Установка и запуск

### Установка с помощью uv (рекомендуется)

```bash
# Клонируйте репозиторий
git clone https://github.com/n0d33p/devops-engineer-from-scratch-project-49.git
cd devops-engineer-from-scratch-project-49

# Установите пакет
uv tool install .

# Проверьте, что команды доступны
brain-games --help 
```
## 🎯 Как играть?
После установки вы можете запустить любую игру простой командой:
```bash
# Запуск конкретной игры
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime

# Общее приветствие
brain-games
```
Цель игры: Правильно ответить на три вопроса подряд. После трех правильных ответов вы побеждаете!

## 📹 Демонстрация игр
🎲 Brain Even (Четное число)
Правила: Определите, является ли число четным. Ответьте "yes" для четных, "no" для нечетных.

https://asciinema.org/a/25Dxdy7O5Ht3AbhWKs5fwvYqh

Пример успешной игры:

```bash
brain-even
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer: no
Correct!
Question: 6
Your answer: yes
Correct!
Question: 7
Your answer: no
Correct!
Congratulations, Sam!
```

🧮 Brain Calc (Калькулятор)
Правила: Вычислите результат математического выражения (+, -, *).

https://asciinema.org/a/1FFchxFSUh406Zja4p0aoqlGx

```bash
brain-calc
Welcome to the Brain Games!
May I have your name? Alex
Hello, Alex!
What is the result of the expression?
Question: 25 * 7
Your answer: 145
'145' is wrong answer ;(. Correct answer was '175'.
Let's try again, Alex!
```

🔢 Brain GCD (Наибольший общий делитель)
Правила: Найдите наибольший общий делитель двух чисел.

https://asciinema.org/a/ReelKEmtmyz2IGHS9Wunwc194

📈 Brain Progression (Арифметическая прогрессия)
Правила: Найдите пропущенное число в арифметической прогрессии.

https://asciinema.org/a/BYG0mcYKH5ElRfgtk9EXAUZYf

🔢 Brain Prime (Простое число)
Правила: Определите, является ли число простым.

https://asciinema.org/a/zkuMzxOgT7vyWSboH4II8uz9I

👤 Автор
n0d33p

GitHub: @n0d33p

Проект: Brain Games

🙏 Благодарности
Проект создан в рамках обучения на Hexlet

Вдохновлен классическими математическими играми для развития мышления