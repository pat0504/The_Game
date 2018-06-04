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

def attack(self, player, enemy1):
          if player.mattack == 0:
               enemy1.hp - player.attack
          elif player.attack == 0:
               enemy1.hp - player.mattack
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
     print(testEnemy.hp)
     action = input('> ')
     valid_actions = ['attack', 'defend', 'a', 'd']
     if action.lower() in valid_actions:
          if action.lower() in ['attack', 'a']:
               attack(myPlayer1, testEnemy)
               print(testEnemy.hp)
          elif action.lower() in ['defend', 'd']:
               print('hello')
     while action.lower() not in valid_actions:
          print("Invalid")
          if action.lower() in valid_actions:
               if action.lower() in ['attack', 'a']:
                    attack(myPlayer1, testEnemy)
                    print(testEnemy.hp)
               elif action.lower() in ['defend', 'd']:
                    print('hello')
          




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

title_screen()
