"""
Samuel and Jacob created this program
Made in Python 3.8
This program may include calculator etc

All programs made by us refrence is my github

Some programs were refrenced with my github
github.com/ttheholyone (Jacobs Github)

"""

import string
import random
from random import randint, choice
import sys
import os
import pyfiglet
import pprint
import colorama
import time
from colorama import init
from colorama import Fore, Back, Style
init()

print("CAL99 BOOTING...")

def clear():
  print("\n"*100)


# Random number game!

def program():
    def ask_for_number(message):
        while True:
            i = input(message)
            if i.isdigit():
                return int(i)
            else:
                print("That's not a number!")

    num1 = ask_for_number("Enter the first number: ")
    num2 = ask_for_number("Enter the second number: ")

    input("Press enter to proceed...\n")
    time.sleep(3)
    clear()

    # Asking for how many guesses the user gets

    number = random.randint(num1, num2)
    print(f"The random number will be {num1} - {num2}")
    input("Press enter to proceed...\n")
    time.sleep(1)
    clear()
# error handling
    def ask_for_guesses(message):
        while True:
            i = input(message)
            if i.isdigit():
                return int(i)
            else:
                print("That's not a number!")
    guesses = ask_for_guesses("Enter amount of guesses you would like...\n")
    guess = 0

        # Starting the game...

    while True:
        if guess > guesses:
            print("Out of guesses\n:( Try again")
            input("Press enter to proceed")
            options()

# error handling
        def ask_for_rannumber(message):
            while True:
                i = input(message)
                if i.isdigit():
                    return int(i)
                else:
                    print("Hey! Thats not a number..!")

        char = ask_for_rannumber(f"Please enter number to guess number must be {num1} - {num2}!\n")
        if char > number:
            guess += 1
            clear()
            print(f"""
Too high!
You have guessed {guess} times!
You only have {guesses}! Be Careful!
Please try again!
        """)
        if char < number:
            guess += 1
            clear()
            print(f"""
Too low!
You have guessed {guess} times!
You only have {guesses}! Be Careful!
Please try again!
        """)
        if char == number:
            guess += 1
            input(f"""
You got it!
You have guessed {guess} times!
You had {guesses} guesses!
Great Job!
Press enter to proceed!
""")
            options()


# Calculator



def calculator():
    input("""
Welcome to Cal V2!
This program is a advance calculator that allows \nyou to perform calculations using two numbers and a character that indicates which math operation toperform.

Press enter to proceed

""")
    clear()
    opers = {
      '+': lambda a, b: a + b,
      '-': lambda a, b: a - b,
      '/': lambda a, b: a / b,
      '*': lambda a, b: a * b,
      '**': lambda a, b: a ** b
    }
    operspretty = {
    '+': 'Addition',
    '-': 'Subtraction',
    '*': 'Multiply',
    '/': 'Divide',
    '**': 'Pow'
    }
    def operschoice(operspretty):
        print("\n\nOperators to choose from:\n\n\n")
        for item, amount in operspretty.items():
            print("{} ({})".format(item, amount))
    clear()
    while True:
            try:
                num1 = int(input('Please choose a number: \n'))
                num2 = int(input('\n\nPlease choose another number: \n'))
                break
            except:
                print('Please enter a valid number')
    operschoice(operspretty)
    choice = input('\n\n\nPlease choose from the choices above\n')
    clear()
    if choice in opers:
        print('\n\nCalculating...')
        time.sleep(1)
        print(f"\n\nAnswer: \n{opers[choice](num1,num2)}")
        options()
    else:
         print("Given operator not found") #checks if the read value is in the opers dictionairy

# Tempature Convertor

def tempconv():
  char = input("""
Enter Q to quit
Enter C to convert Celcius into Fahrenheit
Enter F to convert Fahrenheit into Celcius  
""")
  if char.lower() == 'q':
    options()
  if char.lower() == 'c':
    c = input('Please enter the Celcius of a number you want to convert: \n')
    first = int(c) * 2
    second = first + 30
    print(f'Your estimated temperature in degrees Fahrenheit \nis °F {second}!')
  elif char.lower() == 'f':
    f = input(f'Please enter the Fahrenheit of a number you want to convert: \n')
    first = int(f) - 30
    second = first / 2
    print(f'Your estimated temperature in degrees Celcius \nis °C {second}!')


# Password Generator

def passwordgen():

  cq = input('Press Q to quit or C to continue')
  if cq.lower() == 'q':
    options
  if cq.lower() == 'c':
    pass
  a = int(input('Whats the minimum amount of length the password may have?(Recommended: 8)\n'))
  b = int(input('Whats the longest your password can be?(Recommended: 32)\n'))
  characters = string.ascii_letters + string.punctuation + string.digits
  password = "".join(choice(characters) for x in range(randint(a, b)))
  print(str('Boom! Your new password is: "' + password) + '"')
  print(cq)
  input('Press enter to proceed')
  options()

# Character Sorter

def sorter():
  number = input('Please enter the number or string you want to sort!\n')
  sort = sorted(number)
  print('Here is your string/number sorted! \n')
  print(sort)
  print(f'Your original string/number was \n {number}!')  
  options()

def ask_for_option(message):
   while True:
       i = input(message)
       if i.isdigit():
        return int(i)
       else:
        print("That's not a number!")

def options():
    mainmenu = ask_for_option(Fore.LIGHTRED_EX + """
Hello this is Cal99, your game manager you can \nplay multiple games that I have stored so that \nyou can enjoy! 

OPTIONS:

1: Random Number Guessing Game 
2: Calculator(Advanced)
3: Tempature Convertor 
4: Password Generator
5: Character Sorter
6: About
7: Quit
""")
    if mainmenu == 1:
      program()
    elif mainmenu == 2:
      calculator()
    elif mainmenu == 3:
      tempconv()
    elif mainmenu == 4:
      passwordgen()
    elif mainmenu == 5:
      sorter()
    elif mainmenu == 6:
      clear()
      input("""

About Cal99:

Developers: Sam and Jacob

Cal99 There is different Python programs you can use. Just choose a option and you may use a calculator, game and more!

This is a fun project me and my friend had been working on for a hobby.

Press enter to continue...

""")
      options()
    elif mainmenu == 7:
      clear()
      sys.exit()
    else:
      options()
options()

  
# Should never show unless a error happened

print("\n\n\n\n\n\n\n\n\n\nShutting down")
