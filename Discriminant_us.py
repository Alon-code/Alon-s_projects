# ========================================================== #

                      #--# Alon #--#

# ========================================================== #

# Welcome
print ("\nLaunch program 'Discriminant'\n")

# Import libraries
import math
import sys

# Expressions
print ("Possible expressions for this program:")
print ("1) a * x * x ± b * x ± c = 0")
print ("2) a * x * x ± b = 0")
print ("3) a * x * x ± c = 0\n")

# Write var a
while True:
    try:
        while True:
            a = float (input ("Write a: "))
            if a == 0:
                print ("Variable 'a' can't be zero")
            elif a != 0:
                print ("Variable a:", a)
                break
        break
    except EOFError:
        print ("\nYou pressed keyboard shortcut 'Ctrl+D'")
    except ValueError:
        print ("Write number")
    except KeyboardInterrupt:
        print ("\nYou pressed keyboard shortcut 'Ctrl+C'")

# Write var b
while True:
    try:
        b = float (input ("Write b: "))
        print ("Variable b:", b)
        break
    except EOFError:
        print ("\nYou pressed keyboard shortcut 'Ctrl+D'")
    except ValueError:
        print ("Write number")
    except KeyboardInterrupt:
        print ("\nYou pressed keyboard shortcut 'Ctrl+C'")

# Write var c
while True:
    try:
        c = float (input ("Write c: "))
        print ("Variable c:", c)
        break
    except EOFError:
        print ("\nYou pressed keyboard shortcut 'Ctrl+D'")
    except ValueError:
        print ("Write number")
    except KeyboardInterrupt:
        print ("\nYou pressed keyboard shortcut 'Ctrl+C'")

# Empty string
print ('\n')

# Discriminant
if b != 0 and c != 0:
    d = b * b - 4 * a * c
    print ("Discriminant:", d)
elif b == 0 and c != 0:
    d = -4 * a * c
    print ("Discriminant:", d)

# X1 and X2 with result
try:
    if c == 0 and b != 0:
        x = -b / a
        print ("As a result: X = 0 or X =", x)
        sys.exit ()
    elif c == 0 and b == 0:
        print ("As a result: discriminant cannot be found, because c = 0 и b = 0")
        sys.exit ()
    elif d == 0:
        x = -b / 2 * a
        print ("As a result: X =", x)
        print ("End of program")
    elif d > 0:
        x1 = (-b + math.sqrt (d)) / 2 * a
        x2 = (-b - math.sqrt (d)) / 2 * a
        print ("As a result: X1 = {0}, X2 = {1}".format (x1, x2))
        print ("End of program")
    elif d < 0:
        print ("As a result: no roots")
except SystemExit:
    print ("End of program")

# ========================================================== #

                      #--# Alon #--#

# ========================================================== #
