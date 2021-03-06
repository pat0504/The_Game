 # Python Text Adventure RPG
 # Patrick's RPG

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100


 #### Player Setup #####
class Player:
     def __init__(self):
          self.name = ''
          self.hp = 0
          self.mp = 0
          self.job = ''
          self.location = 'b1'
          self.game_over = False
         
myPlayer = Player()
#### Enemy Setup ####
class Enemy:
      def __init__(self):
          self.hp = 0
          self.mp = 0
          self.attack = 0
          self.defense = 0

class Imp(Enemy):
      def __init__(self):
          self.hp = 40
          self.mp = 20
          self.attack = 10
          self.defense = 3


#### Title Screen ####
def title_screen_selections():
     option = input('> ')
     if option.lower() in ["play", "p"]:
          setup_game() # placeholder until written
     elif option.lower() == "help":
          help_menu()
     elif option.lower() == "quit":
          sys.exit()
     while option.lower() not in ['play', 'p', 'help', 'h', 'quit']:
          print("Please enter a valid command.")
          options = input("> ")
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
     print('- Current commands include "Move", "Examine" and "Help" to bring up this menu')
     print('- Type your commands to do them')
     print('- Good luck and have fun and do not die!')
     title_screen_selections()

def in_game_help():
     print(' ---------------------------')
     print('| Welcome to the help menu! |')
     print(' ---------------------------')
     print('- Current commands include "Move" and "Examine"')
     print('- Once you say move type which direction you want to move in')
     print('- Type your commands to do them')
     print('- Good luck and have fun and don\'t die!')
     prompt()
     
#### GAME INTERACTIVY ####

def prompt():
     print("\n" + "==============================")
     print("What would you like to do?")
     print("Hint: Try examining each zone!")
     action = input("> ")
     acceptable_actions =['move', 'go', 'travel', 'walk', 'quit'
                          , 'examine', 'help', 'inspect', 'interact'
                          , 'look']
     while action.lower() not in acceptable_actions:
          print("Unknown action, try again. \n Hint: Type help for a menu with all the commands you can do.")
          action = input("> ")
     if action.lower() == 'quit':
          sys.exit()
     elif action.lower() in ['move', 'go', 'travel', 'walk']:
          player_move(action.lower())
     elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
          player_examine(action.lower())
     elif action.lower() == 'help':
          in_game_help()

def player_move(myAction):
     ask = "Where would you like to move to?\n"
     print(myPlayer.location)
     dest = input(ask)
     if dest in ['up', 'north']:
          print(myPlayer.location)
          destination = zonemap[myPlayer.location][UP]
          movement_handler(destination)
     elif dest in ['left', 'west']:
          destination = zonemap[myPlayer.location][LEFT]
          movement_handler(destination)
     elif dest in ['right', 'east']:
          destination = zonemap[myPlayer.location][RIGHT]
          movement_handler(destination)
     elif dest in ['down', 'south']:
          destination = zonemap[myPlayer.location][DOWN]
          movement_handler(destination)


def movement_handler(destination):
     print("\nYou have moved to " + destination + ".")
     print("\n" + zonemap[destination][DESCRIPTION])
     myPlayer.location = destination

def player_examine(action):
     print(zonemap[''][EXAMINATION])
        

#### GAME FUNCTIONALITY ####

def main_game_loop():
     while myPlayer.game_over == False:
          prompt()
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
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examination'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'
ENEMY = ''

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,                 
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False
                 }

zonemap = {
     'a1': {
          ZONENAME: '',
          DESCRIPTION: 'You\'re in the woods above north from your house.',
          EXAMINATION: 'There\'s a lot of trees, nothing too interesting.',
          SOLVED: False,
          UP: '',
          DOWN: 'b1',
          LEFT: '',
          RIGHT: 'a2',
          ENEMY: '',
     },
     'a2': {
          ZONENAME: '',
          DESCRIPTION: 'description a2',
          EXAMINATION: 'examination a2',
          SOLVED: False,
          UP: '',
          DOWN: 'b2',
          LEFT: 'a1',
          RIGHT: 'a3',
          ENEMY: '',
     },
     'a3': {
          ZONENAME: '',
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
          EXAMINATION: 'Eh not much to do here, it\'s my home. East of my house through the woods, is the town entrance',
          SOLVED: False,
          UP: 'a1',
          DOWN: 'c1',
          LEFT: '',
          RIGHT: 'b3',
          ENEMY: '',
     },
     'b2': {
          ZONENAME: '',
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
          ZONENAME: '',
          DESCRIPTION: 'description b3',
          EXAMINATION: 'examination b3',
          SOLVED: False,
          UP: 'a3',
          DOWN: 'c3',
          LEFT: 'b2',
          RIGHT: 'b4',
          ENEMY: '',
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
     print(question1)

     player_name = input("> ")
     myPlayer.name = player_name

     question2 = "Oh " + player_name + " is it?\n"
     question2added = "What role would you like to play " + player_name + "\n"
     question2additional = "(Currently only warrior, priest, and mage are available)\n"

     for character in question2:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.04)
     for character in question2added:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.03)
     for character in question2additional:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.03)
     player_job = input("> ")

     valid_jobs = ['warrior', 'mage', 'priest']
     if player_job.lower() in valid_jobs:
          myPlayer.job = player_job
          print("You are now a " + player_job + "\n")
     while player_job.lower() not in valid_jobs:
          print("That is not a role you can play")
          player_job = input("> ")
          if player_job.lower() in valid_jobs:
               myPlayer.job = player_job
               print("You are now a " + player_job + "!\n")
             
###### PLAYER STATS ######

     if myPlayer.job is 'warrior':
          self.hp = 120
          self.mp = 20
     elif myPlayer.job is 'mage':
          self.hp = 40
          self.mp = 120
     elif myPlayer.job is 'priest':
          self.hp = 60
          self.mp = 60

#### INTRO ####
     question3 = "Welcome, " + player_name + " the fantastic " + player_job + "\n"
     for character in question3:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.05)


     speech1 = "Welcome to this fantasy world of adventure!\n"
     speech2 = "Let's hope you don't get too lost.\n"
     speech3 = "Good luck.\n"
     speech4 = "And have fun.\n"
     for character in speech1:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.04)    
     for character in speech2:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.04)
     for character in speech3:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.05)
     for character in speech4:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.06) 

     os.system('clear')
     print('################')
     print('# Let us begin #')
     print('################')

     main_game_loop()     


     
title_screen()
