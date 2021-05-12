"""
Samuel and Jacob created this program
Made in Python 3.8
This program may include calculator etc

All programs made by us refrence is my github

Some programs were refrenced with my github
github.com/ttheholyone (Jacobs Github)

These programs are all made by us problem solving etc
If you beg to differ reverse search our code :D 

We know the code isn't the best and we fully agree to you
But as of now I am(Jacob) is teaching Samuel Python and I am not exactly worried about it
"""


# Imports the modules

import string # for password gen
import random # for ran num guesser, password gen, 8ball
from random import randint, choice # more for rannum guesser, password gen, 8ball
import sys # for the overall program
import os # for the overall program
import pyfiglet # just for fun
import pprint # just for fun
import colorama # just for fun
import time # slows things down
from colorama import init # colors for the text
from colorama import Fore, Back, Style # more colors for the text

init()


# Cool Boot Message not needed though feel free to delete it

print(Fore.LIGHTGREEN_EX + "CAL99 BOOTING..." + Fore.WHITE)
time.sleep(1)

# A custom clear as os.system('cls') only works for windows 

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


    # sees if you run out of guesses or not

    while True:
        if guess >= guesses:
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

        # ask for how many guesses some gets

        char = ask_for_rannumber(f"Please enter number to guess number must be {num1} - {num2}!\n")

        # Sees if number is too high

        if char > number:
            guess += 1
            clear()
            print(f"""
Too high!
You have guessed {guess} times!
You only have {guesses}! Be Careful!
Please try again!
        """)

      # sees if number is too low

        if char < number:
            guess += 1
            clear()
            print(f"""
Too low!
You have guessed {guess} times!
You only have {guesses}! Be Careful!
Please try again!
        """)

        
        # sees if number is right


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


    # This is the calculating

    opers = {
      '+': lambda a, b: a + b,
      '-': lambda a, b: a - b,
      '/': lambda a, b: a / b,
      '*': lambda a, b: a * b,
      '**': lambda a, b: a ** b
    }


    # This is what the user sees


    operspretty = {
    '+': 'Addition',
    '-': 'Subtraction',
    '*': 'Multiply',
    '/': 'Divide',
    '**': 'Pow'
    }

  # This makes the user the operators they can use

    def operschoice(operspretty):
        print("\n\nOperators to choose from:\n\n\n")
        for item, amount in operspretty.items():
            print("{} ({})".format(item, amount))
    clear()

        # This is error handling for the numbers you choose to calculate

    while True:
            try:
                num1 = int(input('Please choose a number: \n'))
                num2 = int(input('\n\nPlease choose another number: \n'))
                break
            except:
                print('Please enter a valid number')


    # shows the user the operators

    operschoice(operspretty)

    # this asks them to choose addition subtraction Multiply divide or pow

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

  # Options for the program

  char = input("""
Enter Q to quit
Enter C to convert Celcius into Fahrenheit
Enter F to convert Fahrenheit into Celcius  
""")

  # There is the main program

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

  # Options for the program

  cq = input('Press Q to quit or C to continue')
  if cq.lower() == 'q':
    options

  # If they got it here they clicked c to continue to the program

  if cq.lower() == 'c':
    pass

  # Here it asks you for what you want in the password

  a = int(input('Whats the minimum amount of length the password may have?(Recommended: 8)\n'))
  b = int(input('Whats the longest your password can be?(Recommended: 32)\n'))

  # Makes the password

  characters = string.ascii_letters + string.punctuation + string.digits
  password = "".join(choice(characters) for x in range(randint(a, b)))

  # Prints the password to the console

  print(str('Boom! Your new password is: "' + password) + '"')

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


# 8 Ball Game spelt eightballgame because python doesnt let that in there functions

def eightballgame():

  # Word list for all the answers it can give

	words = ["Yes", 'No', 'Im not sure..', 'As I See it, yes', 'Ask again later...', 'Better not tell you now', 'Cannot Predict now..', 'Concentrate and ask again.', 'Dont count on it', 'It is certain', 'It is decidedly so that the answer is N O', 'Most likely', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Outlook good', 'Reply hazy, try again', 'Signs point to yes', 'Very doubtful', 'Without a doubt', 'Yes - definitely', 'You may rely on it', 'Looks holy to me', 'Sam and Jacob agrees...', 'Sam and Jacob disagrees']

  # chooses a random word from that list

	ranwords = random.choice(words)

  # this asks the question

	ques = input('Enter the string you want the 8-ball to answer to! \n')
	
  # this answers the question

	print(f'Your question: {ques} has been answered carefully:\n\n{ranwords}')


# Greeting

name = input("What is your name? My name is " + Fore.BLUE + "Cal99" + Fore.WHITE + "!\n")
time.sleep(1)
print('Nice to meet you ' + Fore.BLUE + f'{name}' + Fore.WHITE + '!')
input("Press enter to continue\n")
clear()

def ask_for_option(message):
   while True:
       i = input(message)
       if i.isdigit():
        return int(i)
       else:
        print("That's not a number!")

def options():
    mainmenu = ask_for_option(Fore.LIGHTRED_EX + """

Short Description:

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

    # This goes to the program you chose in mainmenu

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

Made in Python 3.8
Developers: Sam and Jacob


All programs made by us refrence is my github

Some programs were refrenced with my github
github.com/ttheholyone (Jacobs Github)


Cal99 There is different Python programs you can use. Just choose a option and you may use a calculator, game and more!

This is a fun project me and my friend had been working on for a hobby.


These programs are all made by us problem solving etc
If you beg to differ reverse search our code :D 

We know the code isn't the best and we fully agree to you
But as of now I am(Jacob) is teaching Samuel Python and I am not exactly worried about it

Press enter to continue...

""")
      options()
    elif mainmenu == 7:
      clear()
      print(f"Sad to see you go... goodbye {name} ")
      time.sleep(3)
      sys.exit()
    else:
      options()
options()

  
# Should never show unless a error happened

print("\n\n\n\n\n\n\n\n\n\nShutting down")
