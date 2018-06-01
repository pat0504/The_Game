 # Python Text Adventure RPG
 # Patrick's RPG

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100
debug = 1



     
def slowType(speech, speed):
     if debug > 0:
          for character in speech:
               sys.stdout.write(character)
               sys.stdout.flush()
               time.sleep(speed)
               speed = 0.001
     if debug < 0:
          for character in speech:
               sys.stdout.write(character)
               sys.stdout.flush()
               time.sleep(speed)


 #### Player Setup #####
class Player:
     def __init__(self):
          self.name = ''
          self.hp = 0
          self.mp = 0
          self.job = ''
          self.role = ''
          self.location = 'b1'
          self.game_over = False
          self.attack = 0
          self.mattack = 0
          self.mdefense = 0
          self.defense = 0
          self.wallet = 0

def attack(player, enemy):
          if player.mattack == 0:
               enemy.hp - (player.attack - 20%(enemy.defense))
          if self.attack == 0:
               enemy.hp - (player.mattack - 20%(enemy.mdefense))
#### Enemy Setup ####
class Enemy:
      def __init__(self, hp, mp, attack, mattack, defense, mdefense, defeated = False):
          self.hp = hp
          self.mp = mp
          self.attack = attack
          self.mattack = mattack
          self.defense = defense
          self.mdefense = mdefense
          self.defeated = defeated

class Imp(Enemy):
     def __init__(self):
          super(40, 20, 0, 7, 3, 4, False)
          

class Father(Enemy):
     def __init__(self):
          super(20, 0, 2, 0, 3, 3, False)

class Fire_Giant(Enemy):
     def __init__(self):
          self.hp = 300
          self.mp = 200
          self.attack = 0
          self.mattack = 80
          self.defense = 70
          self.mdefense = 60

class Demon_King(Enemy):
     def __init__(self):
          self.hp = 300
          self.mp = 100
          self.attack = 80
          self.mattack = 0
          self.defense = 100
          self.mdefense = 110
         
myPlayer = Player()
myPlayer1 = Player()
testEnemy = Fire_Giant()
def Fight_test():
     print("test")
     player_job = input('> ')
     
     valid_jobs = ['warrior', 'w', 'Warrior', 'm', 'Mage', 'mage']
     if player_job.lower() in valid_jobs:
          myPlayer1.job = player_job
          print("You are now a " + player_job + "\n")
          print(myPlayer1.job)
          if myPlayer1.job in ['warrior', 'w', 'Warrior']:
                    myPlayer1.hp = 120
                    myPlayer1.mp = 20
                    myPlayer1.attack = 6
                    myPlayer1.mattack = 0
                    myPlayer1.defense = 8
                    myPlayer1.mdefense = 7
                    myPlayer1.role = "Warrior"
          elif myPlayer1.job in ['mage', 'm', 'Mage']:
                    myPlayer1.hp = 70
                    myPlayer1.mp = 80
                    myPlayer1.attack = 0
                    myPlayer1.mattack = 8
                    myPlayer1.defense = 4
                    myPlayer1.mdefense = 5
                    myPlayer1.role = "Mage"
     while player_job.lower() not in valid_jobs:
          print("That is not a role you can play")
          player_job = input("> ")
          if player_job.lower() in valid_jobs:
               myPlayer1.job = player_job
               print("You are now a " + player_job + "!\n")
               if myPlayer1.job in ['Warrior', 'w', 'warrior']:
                    myPlayer1.hp = 40
                    myPlayer1.mp = 20
                    myPlayer1.attack = 6
                    myPlayer1.mattack = 0
                    myPlayer1.defense = 8
                    myPlayer1.mdefense = 7
                    myPlayer1.role = "Warrior"
               elif myPlayer1.job in ['mage', 'm', 'Mage']:
                    myPlayer1.hp = 30
                    myPlayer1.mp = 50
                    myPlayer1.attack = 0
                    myPlayer1.mattack = 8
                    myPlayer1.defense = 4
                    myPlayer1.mdefense = 5
                    myPlayer.role = "Mage"
     print("Fight time")
     action = input('> ')
     valid_actions = ['attack', 'defend']
     if action.lower() in valid_actions:
          if action.lower() in ['attack', 'a']:
               attack(myPlayer1, testEnemy)
               print(testEnemy.hp)
          elif action.lower() in ['defend', 'd']:
               print('hello')
               



#### Title Screen ####
def title_screen_selections():
     option = input('> ')
     if option.lower() in ["play", "p"]:
          setup_game() # placeholder until written
     elif option.lower() == "help":
          help_menu()
     elif option.lower() == "quit":
          sys.exit()
     elif option.lower() == "test":
          Fight_test()
     while option.lower() not in ['play', 'p', 'help', 'h', 'quit']:
          print("Please enter a valid command.")
          option = input("> ")
          if option.lower() in ["play", "p"]:
               setup_game() # placeholder until written
          elif option.lower() in ["help", "h"]:
               help_menu()
          elif option.lower() == "quit":
               sys.exit()

def title_screen():
     os.system('clear')
     print('-----------------------')
     print('| Welcome to my Game! |')
     print('-----------------------')
     print('       - Play -       ')
     print('       - Help -       ')
     print('       - Quit -       ')
     title_screen_selections()

def help_menu():
     print('-----------------------')
     print('| Welcome to my Game! |')
     print('-----------------------')
     print('- Current commands include "Move", "Examine", "Stats", \n- And "Help" to bring up this menu in game')
     print('- Type your commands to do them')
     print('- Good luck and have fun and do not die!')
     title_screen_selections()

def in_game_help():
     print(' ---------------------------')
     print('| Welcome to the help menu! |')
     print(' ---------------------------')
     print('- Current commands include "Move", "Examine", "Stats", \n- And "Help" to bring up this menu in game')
     print('- Once you say "Move" type which direction you want to move in')
     print('- You can go left, right, up, and down.')
     print('- Type your commands to do them')
     print('- Good luck, have fun, and don\'t die!')
     prompt()
     
#### GAME INTERACTIVY ####

def prompt():
     print("\n" + "==============================")
     print("What would you like to do?")
     print("Hint: Try examining each zone!")
     action = input("> ")
     acceptable_actions =['move', 'go', 'travel', 'walk', 'quit'
                          , 'examine', 'help', 'inspect', 'interact'
                          , 'look','stats', 'statistics', 'my stats', 'mystats', 'mystatistics', 'my statistics'
                          , 'what are my stats?', 'what are my stats', 'test']
     while action.lower() not in acceptable_actions:
          print("Unknown action, try again. \n Hint: Type help for a menu with all the commands you can do.")
          action = input("> ")
     if action.lower() == 'quit':
          sys.exit()
     elif action.lower() == 'test':
          myPlayer.hp -= 1000
     elif action.lower() in ['move', 'go', 'travel', 'walk']:
          player_move(action.lower())
     elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
          player_examine(action.lower())
     elif action.lower() == 'help':
          in_game_help()
     elif action.lower() in ['stats', 'statistics', 'my stats', 'mystats', 'mystatistics', 'my statistics',
                             'what are my stats?', 'what are my stats']:
          display_stats(myPlayer)

def player_move(myAction):
     ask = "Where would you like to move to?\n"
     print("You are currently located in " + myPlayer.location)
     dest = input(ask)
     if dest.lower() in ['up', 'north']:
          destination = zonemap[myPlayer.location][UP]
          movement_handler(destination)
     elif dest.lower() in ['left', 'west']:
          destination = zonemap[myPlayer.location][LEFT]
          movement_handler(destination)
     elif dest.lower() in ['right', 'east']:
          destination = zonemap[myPlayer.location][RIGHT]
          movement_handler(destination)
     elif dest.lower() in ['down', 'south']:
          destination = zonemap[myPlayer.location][DOWN]
          movement_handler(destination)

def display_stats(hero):
     print("Name: " + hero.name)
     print("Class: " + hero.role)
     print("HP: " + str(hero.hp))
     print("MP: " + str(hero.mp))
     print("Attack: " + str(hero.attack))
     print("Magic Attack: " + str(hero.mattack))
     print("Defense: " + str(hero.defense))
     print("Magic Defense: " + str(hero.mdefense))



def movement_handler(destination):
     if len(destination) < 1:
          print('You can not go there')
          prompt()
     else:
          print("============================")
          print("\nYou have moved to " + destination + ".")
          print(zonemap[destination][DESCRIPTION])
          myPlayer.location = destination
          print(zonemap[myPlayer.location][ZONENAME])
          #############################

def player_examine(action):
     print("===========================")
     print(zonemap[myPlayer.location][EXAMINATION])
     if len(zonemap[myPlayer.location][ENEMY]) < 1:
          print("No enemies in the area")
          blue = False
          if blue == False:
               print('goodbye')
     elif len(zonemap[myPlayer.location][ENEMY]) > 1:
          print("enemy in area")
          blue = True
          if blue == True:
               print('hello')
        

#### GAME FUNCTIONALITY ####

def main_game_loop():
     while myPlayer.hp >= 0:
          prompt()
     while myPlayer.hp <= 0:
          death_screen()
     
     
    # here handle if puzzles have been solved, boss defeated, explored everything, etc.


#### VISUAL MAP ####
"""
 a1 a2 a3 a4
-------------
|  |  |  |  | a4
-------------
|  |  |  |  | b4
-------------
|  |  |  |  | c4
-------------
|  |  |  |  | d4
-------------
"""
ZONENAME = 'zonename'
DESCRIPTION = 'description'
EXAMINATION = 'examination'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'
ENEMY = 'enemy'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,                 
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False
                 }

zonemap = {
     'a1': {
          ZONENAME: 'Training Grounds',
          DESCRIPTION: 'The place where you spar with your father,\nHey look there he is now.',
          EXAMINATION: 'Hey son want to spar with me?',
          SOLVED: False,
          UP: '',
          DOWN: 'b1',
          LEFT: '',
          RIGHT: 'a2',
          ENEMY: 'Imp'
     },
     'a2': {
          ZONENAME: 'a2 ZN',
          DESCRIPTION: 'description a2',
          EXAMINATION: 'examination a2',
          SOLVED: False,
          UP: '',
          DOWN: 'b2',
          LEFT: 'a1',
          RIGHT: 'a3',
          ENEMY: 'Imp',
     },
     'a3': {
          ZONENAME: 'a3 ZN',
          DESCRIPTION: 'description a3',
          EXAMINATION: 'examination a3',
          SOLVED: False,
          UP: '',
          DOWN: 'b3',
          LEFT: 'a2',
          RIGHT: 'a4',
          ENEMY: '',
     },
     'a4': {
          ZONENAME: '',
          DESCRIPTION: 'description a4',
          EXAMINATION: 'examination a4',
          SOLVED: False,
          UP: '',
          DOWN: 'b4',
          LEFT: 'a3',
          RIGHT: '',
          ENEMY: '',
     },
     'b1': {
          ZONENAME: '',
          DESCRIPTION: 'Your place of residence. It\'s surrounded by woods',
          EXAMINATION: 'Eh not much to do here, it\'s my home. \nEast of my house through the woods, is the town entrance.\nI should probably go visit my Father up north first though.',
          SOLVED: False,
          UP: 'a1',
          DOWN: 'c1',
          LEFT: '',
          RIGHT: 'b3',
          ENEMY: '',
     },
     'b2': {
          ZONENAME: 'b2 ZN',
          DESCRIPTION: 'The woods East of your house. ',
          EXAMINATION: 'You see a gate further East.',
          SOLVED: False,
          UP: 'a2',
          DOWN: 'c2',
          LEFT: 'b1',
          RIGHT: 'b3',
          ENEMY: '',
     },
     'b3': {
          ZONENAME: 'Town Gate',
          DESCRIPTION: 'The Entrance to the town',
          EXAMINATION: 'There\'s a gate keeper defending off against an Imp!\nI have to help him!',
          SOLVED: False,
          UP: 'a3',
          DOWN: 'c3',
          LEFT: 'b2',
          RIGHT: 'b4',
          ENEMY: 'Imp',
     },
     'b4': {
          ZONENAME: '',
          DESCRIPTION: 'description b4',
          EXAMINATION: 'examination b4',
          SOLVED: False,
          UP: 'a4',
          DOWN: 'c4',
          LEFT: 'b3',
          RIGHT: '',
          ENEMY: '',
     },
     'c1': {
          ZONENAME: '',
          DESCRIPTION: 'description c1',
          EXAMINATION: 'examination c1',
          SOLVED: False,
          UP: 'b1',
          DOWN: 'd1',
          LEFT: '',
          RIGHT: 'c2',
          ENEMY: '',
     },
     'c2': {
          ZONENAME: '',
          DESCRIPTION: 'description c2',
          EXAMINATION: 'examination c2',
          SOLVED: False,
          UP: 'b2',
          DOWN: 'd2',
          LEFT: 'c1',
          RIGHT: 'c3',
          ENEMY: '',
     },
     'c3': {
          ZONENAME: '',
          DESCRIPTION: 'description c3',
          EXAMINATION: 'examination c3',
          SOLVED: False,
          UP: 'b3',
          DOWN: 'd3',
          LEFT: 'c2',
          RIGHT: 'c4',
          ENEMY: '',
     },
     'c4': {
          ZONENAME: '',
          DESCRIPTION: 'description c4',
          EXAMINATION: 'examination c4',
          SOLVED: False,
          UP: 'b4',
          DOWN: 'd4',
          LEFT: 'c3',
          RIGHT: '',
          ENEMY: '',
     },
     'd1': {
          ZONENAME: '',
          DESCRIPTION: 'description d1',
          EXAMINATION: 'examination d1',
          SOLVED: False,
          UP: 'c1',
          DOWN: '',
          LEFT: '',
          RIGHT: 'd2',
          ENEMY: '',
          },
     'd2': {
          ZONENAME: '',
          DESCRIPTION: 'description d2',
          EXAMINATION: 'examination d2',
          SOLVED: False,
          UP: 'c2',
          DOWN: '',
          LEFT: 'd1',
          RIGHT: 'd3',
          ENEMY: '',
     },
     'd3': {
          ZONENAME: '',
          DESCRIPTION: 'description d3',
          EXAMINATION: 'examination d3',
          SOLVED: False,
          UP: 'c3',
          DOWN: '',
          LEFT: 'd2',
          RIGHT: 'd4',
          ENEMY: '',
     },
     'd4': {
          ZONENAME: '',
          DESCRIPTION: 'description d4',
          EXAMINATION: 'examination d4',
          SOLVED: False,
          UP: 'c4',
          DOWN: '',
          LEFT: 'd3',
          RIGHT: '',
          ENEMY: '',
     }
     }


def setup_game():
     os.system('clear')
     question1 = "Hello, What is your name traveler? \n"
     slowType(question1, 0.01)

     player_name = input("> ")
     myPlayer.name = player_name

     question2 = "Oh " + player_name + " is it?\n"
     question2added = "What role would you like to play " + player_name + "\n"
     question2additional = "(Currently only warrior and mage are available)\n"
     slowType(question2, 0.03)
     slowType(question2added, 0.04)
     slowType(question2additional, 0.002)
     player_job = input("> ")

     valid_jobs = ['warrior', 'w', 'Warrior', 'm', 'Mage', 'mage']
     if player_job.lower() in valid_jobs:
          myPlayer.job = player_job
          print("You are now a " + player_job + "\n")
          if myPlayer.job in ['warrior', 'w', 'Warrior']:
                    myPlayer.hp = 120
                    myPlayer.mp = 20
                    myPlayer.attack = 6
                    myPlayer.mattack = 0
                    myPlayer.defense = 8
                    myPlayer.mdefense = 7
                    myPlayer.role = "Warrior"
          elif myPlayer.job in ['mage', 'm', 'Mage']:
                    myPlayer.hp = 70
                    myPlayer.mp = 80
                    myPlayer.attack = 0
                    myPlayer.mattack = 8
                    myPlayer.defense = 4
                    myPlayer.mdefense = 5
                    myPlayer.role = "Mage"
     while player_job.lower() not in valid_jobs:
          print("That is not a role you can play")
          player_job = input("> ")
          if player_job.lower() in valid_jobs:
               myPlayer.job = player_job
               print("You are now a " + player_job + "!\n")
               if myPlayer.job in ['Warrior', 'w', 'warrior']:
                    myPlayer.hp = 40
                    myPlayer.mp = 20
                    myPlayer.attack = 6
                    myPlayer.mattack = 0
                    myPlayer.defense = 8
                    myPlayer.mdefense = 7
                    myPlayer.role = "Warrior"
               elif myPlayer.job in ['mage', 'm', 'Mage']:
                    myPlayer.hp = 30
                    myPlayer.mp = 50
                    myPlayer.attack = 0
                    myPlayer.mattack = 8
                    myPlayer.defense = 4
                    myPlayer.mdefense = 5
                    myPlayer.role = "Mage"


#### INTRO ####
     question3 = "Welcome, " + player_name + " the fantastic " + myPlayer.role + "\n"
     slowType(question3, 0.03)


     speech1 = "Welcome to this fantasy world of adventure!\n"
     speech2 = "Let's hope you don't get too lost.\n"
     speech3 = "Good luck.\n"
     speech4 = "And have fun.\n"
     slowType(speech1, 0.04)
     slowType(speech2, 0.04)
     slowType(speech3, 0.004)
     slowType(speech4, 0.006)
 
## end setup

     os.system('clear')
     print('################')
     print('# Let us begin #')
     print('################')

     main_game_loop()

##### Death Screen #####
def death_screen_selection():
     option2 = input('> ')
     if option2.lower() in ["y", "yes"]:
          title_screen()
     elif option2.lower() in ["n", "no"]:
          sys.exit()
     while option2.lower() not in ['y', 'yes', 'n', 'no']:
          print("Please enter a valid command.")
          option2 = input("> ")
          if option2.lower() in ["y", "yes"]:
               title_screen()
          elif option2.lower() in ["n", "no"]:
               print('Bye, See you next time!')
               sys.exit()

def death_screen():
     print('You have died.')
     print('Want to go again?')
     death_screen_selection()
     

          
##### Fight system #####
          
               
               
          
     #def initFight():

##### Player Tutorial #####
     #def Father_fight
      #    if 



title_screen()
