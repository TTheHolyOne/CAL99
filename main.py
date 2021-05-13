"""
DISCORD: TTHEHOLYONE#1642

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
from random import randint, choice # more for rannum guesser, password gen, 8ball, dice roll


# If you are running this program via repl.it please go into shell and enter this:
#    pip install google_trans_new    in shell

from google_trans_new import google_translator # for translator


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
print(r"""

 _____ _   _ _____ _   _ _____ _   __   _______ _   _ _____                                  
|_   _| | | |  ___| | | |  _  | |  \ \ / |  _  | \ | |  ___|                                 
  | | | |_| | |__ | |_| | | | | |   \ V /| | | |  \| | |__                                   
  | | |  _  |  __||  _  | | | | |    \ / | | | | . ` |  __|                                  
  | | | | | | |___| | | \ \_/ | |____| | \ \_/ | |\  | |___                                  
  ___ \_| |_______\_| |_/\___/\_____/\_/  \___/\_| \_\____/                                  
 / _ \| \ | |  _  \                                                                          
/ /_\ |  \| | | | |                                                                          
|  _  | . ` | | | |                                                                          
| | | | |\  | |/ /                                                                           
\_____\_________/___     _____ _____ _____    ___ ______ _   _  ___  _   _ _____ ___________ 
/  ___|/ _ \|  \/  |    /  __ |  _  |  _  |  / _ \|  _  | | | |/ _ \| \ | /  __ |  ___|  _  \
\ `--./ /_\ | .  . |    | /  \| |_| | |_| | / /_\ | | | | | | / /_\ |  \| | /  \| |__ | | | |
 `--. |  _  | |\/| |    | |   \____ \____ | |  _  | | | | | | |  _  | . ` | |   |  __|| | | |
/\__/ | | | | |  | |    | \__/.___/ .___/ / | | | | |/ /\ \_/ | | | | |\  | \__/| |___| |/ / 
\____/\_| |_\_|  |_/     \____\____/\____/  \_| |_|___/  \___/\_| |_\_| \_/\____\____/|___/  
                                                                                             
                                                                                             

""")
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

  # all the answers it can answer too

  words = ['Yes', 'No', 'Im not sure...', 'As I see it, yes', 'Ask again later..', 'Better not tell you', 'Cannot Predict now..', 'Concentrate and ask again.', 'Dont count on it..', 'It is certain', 'It is decidedly so that the answser is N O', 'Most likely', 'M reply is no', 'My sources say no', 'Outlook not so good', 'Outlook good', 'Reply hazy, try again', 'Signs point to yes', 'Very doubtful', 'Without a doubt', 'Yes - Definitely','You may rely on it']

  # Chooses a random word

  ranwords = random.choice(words)

  # Asks question

  ques = input('Enter the string you want the 8Ball to answer too! \n')
  
  # Answers question
  clear()
  print("Thinking...\n\n")
  time.sleep(2)

  print(Fore.LIGHTCYAN_EX + 'Your question: \n' + Fore.LIGHTRED_EX + f'{ques}' + Fore.LIGHTMAGENTA_EX + f'\nhas been answered carefully:\n\n{ranwords}\n')

  # goes back to main menu

  input('Press enter to quit')
  clear()
  options()


# Translator to translate stuff I guess

def googletranslator():
	# Options

	options = int(input('1: Translate\n2: See all LANGUAGES you can translate.\n(Important because you need to know the names to be able to translate..)\n3: Quit\n'))
	translator = google_translator()

	# Select the options
	if options == 1:
		langtgt = input('\n\nWhat language do you want it to translate the text to? \n')
		orgin = input('\n\nWhat is the text you want to translate? \n')
    
		#translate code

		result = translator.translate(orgin, lang_tgt=langtgt)
		detector = google_translator()
		detect_results = detector.detect(orgin)
		print('\n\nTranslating....\n')

		time.sleep(1)
		
    #translate output

		print(f'The language you you just translated was: {detect_results}\nAnd translated into {langtgt} is: \n{result}\n')   
	elif options == 2:

    # Languages you can choose from


		language = {   "af": "afrikaans",
    "sq": "albanian",
    "am": "amharic",
    "ar": "arabic",
    "hy": "armenian",
    "az": "azerbaijani",
    "eu": "basque",
    "be": "belarusian",
    "bn": "bengali",
    "bs": "bosnian",
    "bg": "bulgarian",
    "ca": "catalan",
    "ceb": "cebuano",
    "ny": "chichewa",
    "zh-cn": "chinese (simplified)",
    "zh-tw": "chinese (traditional)",
    "co": "corsican",
    "hr": "croatian",
    "cs": "czech",
    "da": "danish",
    "nl": "dutch",
    "en": "english",
    "eo": "esperanto",
    "et": "estonian",
    "tl": "filipino",
    "fi": "finnish",
    "fr": "french",
    "fy": "frisian",
    "gl": "galician",
    "ka": "georgian",
    "de": "german",
    "el": "greek",
    "gu": "gujarati",
    "ht": "haitian creole",
    "ha": "hausa",
    "haw": "hawaiian",
    "iw": "hebrew",
    "hi": "hindi",
    "hmn": "hmong",
    "hu": "hungarian",
    "is": "icelandic",
    "ig": "igbo",
    "id": "indonesian",
    "ga": "irish",
    "it": "italian",
    "ja": "japanese",
    "jw": "javanese",
    "kn": "kannada",
    "kk": "kazakh",
    "km": "khmer",
    "ko": "korean",
    "ku": "kurdish (kurmanji)",
    "ky": "kyrgyz",
    "lo": "lao",
    "la": "latin",
    "lv": "latvian",
    "lt": "lithuanian",
    "lb": "luxembourgish",
    "mk": "macedonian",
    "mg": "malagasy",
    "ms": "malay",
    "ml": "malayalam",
    "mt": "maltese",
    "mi": "maori",
    "mr": "marathi",
    "mn": "mongolian",
    "my": "myanmar (burmese)",
    "ne": "nepali",
    "no": "norwegian",
    "ps": "pashto",
    "fa": "persian",
    "pl": "polish",
    "pt": "portuguese",
    "pa": "punjabi",
    "ro": "romanian",
    "ru": "russian",
    "sm": "samoan",
    "gd": "scots gaelic",
    "sr": "serbian",
    "st": "sesotho",
    "sn": "shona",
    "sd": "sindhi",
    "si": "sinhala",
    "sk": "slovak",
    "sl": "slovenian",
    "so": "somali",
    "es": "spanish",
    "su": "sundanese",
    "sw": "swahili",
    "sv": "swedish",
    "tg": "tajik",
    "ta": "tamil",
    "te": "telugu",
    "th": "thai",
    "tr": "turkish",
    "uk": "ukrainian",
    "ur": "urdu",
    "uz": "uzbek",
    "vi": "vietnamese",
    "cy": "welsh",
    "xh": "xhosa",
    "yi": "yiddish",
    "yo": "yoruba",
    "zu": "zulu",
    "fil": "Filipino",
    "he": "Hebrew",}
		print(language)                                             
	elif options == 3:
		options()
	else:
		print('\nI\'m not sure what you mean') 


# Story Game program will take inputs from user and make it into a Story 
def storygame():

  # asks for a name

  name = input('Please enter a name! \n')
  # asks for the age

  age = int(input('Please enter a age! \n'))

  #asks for the food you like to eat

  namefood = input('Please enter what you like to eat! \n')

  # asks for the dogs name

  petname = input("Please enter your dogs name! \n")

  # Asks for what your dog likes to eat

  dogfood = input('Please enter what your dog likes to eat! \n')

  # asks for what u call ur house

  house = input('Please enter what you call your house! \n')

# Choose a story you want to read

  option = input('Please enter what story you want to read \n1 - Normal \n2 - Strange\n')

# The first story

  if option == '1':

    # normal story

    qp = input(f'My name is {name} and I am '+ str({age}) + ' years old. I have a dog named {petname}. My dog likes to eat {dogfood}. I love to eat {namefood}!\n I call my lovely house {house}\n\n')
  elif option == '2':

    # making the inputs uppercase all letters

    name = name.upper()
    namefood = namefood.upper()
    petname = petname.upper()
    dogfood = dogfood.upper()
    house = house.upper()

    # Story number 2

    # weird story

    qp = print(f'My nameee is {name} and I hunt and growl for {namefood}. I have A servant named {petname}.\nI eat {dogfood} with my dog at times... I live in a red place where I call {house}')
  input("Press enter to quit..")
  options()


# Dice Roll

def dice():
    number = input("Press enter to roll!")
    rannumber = random.randint(1, 6) # 1 - 6
    print("Rolling the dice...\n")
    time.sleep(1)
    clear()
    print(f'The Dice Rolled: {rannumber}')
    input("Press enter to quit")
    clear()
    options()


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


# Options for the program with fun colors!


def options():
    mainmenu = ask_for_option(Fore.LIGHTRED_EX + """

Short Description:

Hello this is Cal99, your game manager you can \nplay multiple games that I have stored so that \nyou can enjoy! 

"""

+ Fore.LIGHTGREEN_EX + """

OPTIONS:

""" + Fore.LIGHTYELLOW_EX + """
1: Random Number Guessing Game 

2: Calculator(Advanced)

3: Tempature Convertor 

4: Password Generator

5: Character Sorter

6: 8Ball Game 

7: Translator

8: Story Game

9: Dice Roll

10: About
"""
+ Fore.LIGHTRED_EX + """
11: Quit

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
      eightballgame()
    elif mainmenu == 7:
      googletranslator()
    elif mainmenu == 8:
      storygame()
    elif mainmenu == 9:
        dice()
    elif mainmenu == 10:
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

# sad to see you go :(
      options()
    elif mainmenu == 11:
      clear()
      print(f"Sad to see you go... goodbye {name} ")
      time.sleep(3)
      sys.exit()
    else:
      options()
options()
while True:
  input('Press enter to continue')
  options()

  
# Should never show unless a error happened

# Prints shutting down if a error happens

print("\n\n\n\n\n\n\n\n\n\nShutting down")


