# ========================================================== #

                      #--# Alon #--#

# ========================================================== #

# Добро пожаловать
print ("\nЗапуск программы 'Дискриминант'\n")

# Импорт библиотеки
import math

# Выражения
print ("Возможные выражения для этой программы:")
print ("1) a * x * x ± b * x ± c = 0")
print ("2) a * x * x ± b = 0")
print ("3) a * x * x ± c = 0\n")

# Запись данных в переменную a
while True:
    try:
        while True:
            a = float (input ("Введите a: "))
            if a == 0:
                print ("Переменная 'a' не может быть равна нулю")
            elif a != 0:
                print ("Переменная a:", a)
                break
        break
    except EOFError:
        print ("\nВы нажали сочетание клавиш 'Ctrl+D'")
    except ValueError:
        print ("Вы нажали клавишу 'Enter'")
    except KeyboardInterrupt:
        print ("\nВы нажали сочетание клавиш 'Ctrl+C'")

# Запись данных в переменную b
while True:
    try:
        b = float (input ("Введите b: "))
        print ("Переменная b:", b)
        break
    except EOFError:
        print ("\nВы нажали сочетание клавиш 'Ctrl+D'")
    except ValueError:
        print ("Вы нажали клавишу 'Enter'")
    except KeyboardInterrupt:
        print ("\nВы нажали сочетание клавиш 'Ctrl+C'")

# Запись данных в переменную c
while True:
    try:
        c = float (input ("Введите c: "))
        print ("Переменная c:", c)
        break
    except EOFError:
        print ("\nВы нажали сочетание клавиш 'Ctrl+D'")
    except ValueError:
        print ("Вы нажали клавишу 'Enter'")
    except KeyboardInterrupt:
        print ("\nВы нажали сочетание клавиш 'Ctrl+C'")

# Пропуск строки
print ('\n')

# Нахождение дискриминанта
if b != 0 and c != 0:
    d = b * b - 4 * a * c
    print ("Дискриминант:", d)
elif b == 0 and c != 0:
    d = -4 * a * c
    print ("Дискриминант:", d)

# Нахождение корней x1, x2 и показ результата программы 
if c == 0 and b != 0:
    x = -b / a
    print ("X: 0 или X:", x)
    exit ()
elif c == 0 and b == 0:
    print ("Дискриминант нельзя найти, так как c = 0 и b = 0")
    exit ()
elif d == 0:
    x = -b / 2 * a
    print ("X:", x)
elif d > 0:
    x1 = (-b + math.sqrt (d)) / 2 * a
    x2 = (-b - math.sqrt (d)) / 2 * a
    print ("X1: {0}, X2: {1}".format (x1, x2))
elif d < 0:
    print ("Итог: корней нет")

# ========================================================== #

                      #--# Alon #--#

# ========================================================== #