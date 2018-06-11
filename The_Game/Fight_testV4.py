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
          self.activedefense = 0
          self.defense = 0
          self.wallet = 0
          self.action = 0

def attack(player, enemy1):
     player.action = player.action - 1
     if player.mattack <= 0 and enemy1.activedefense == 0:
          enemy1.hp = enemy1.hp - (player.attack - (enemy1.defense/3))
     if player.mattack <= 0 and enemy1.activedefense == 1:
          enemy1.hp = enemy1.hp - (player.attack - (enemy1.defense/2))
          enemy1.activedefense = 0
     if player.attack <= 0 and enemy1.activedefense == 0:
          enemy1.hp = enemy1.hp - (player.mattack - (enemy1.mdefense/3))
     if player.attack <= 0 and enemy1.activedefense == 1:
          enemy1.hp = enemy1.hp - (player.mattack - (enemy1.mdefense/2))
          enemy1.activedefense = 0
     enemy1.hp = int(enemy1.hp)
     print(enemy1.hp)
     print(player.action)

def defend(player):
     player.activedefense = player.activedefense + 1
     print("You will now take less damage from the next attack you recieve")
     player.action = player.action - 1

def enemy_defend(enemy):
     enemy.activedefense = player.activedefense + 1
     print("The enemy's defenses grow stronger")
     enemy.action = player.action - 1
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
          self.action = 0

class Imp(Enemy):
     def __init__(self):
          self.hp = 40
          self.mp = 20
          self.attack = 0
          self.mattack = 7
          self.defense = 3
          self.mdefense = 4
          

class Father(Enemy):
     def __init__(self):
          self.hp = 20
          self.mp = 0
          self.attack = 2
          self.mattack = 0
          self.defense = 3
          self.mdefense = 3

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

def player_turn():
     while myPlayer1.action >= 1:
          player_action = input('> ')
          valid_actions = ['attack', 'defend', 'a', 'd']
          if player_action.lower() in valid_actions:
               if player_action.lower() in ['attack', 'a']:
                    print(myPlayer1.action)
                    attack(myPlayer1, testEnemy)
               elif player_action.lower() in ['defend', 'd']:
                    defend(myPlayer1)
                    print(myPlayer1.activedefense)
     while player_action.lower() not in valid_actions:
          print("Invalid")
          player_action = input('> ')
          if action.lower() in valid_actions:
               if player_action.lower() in ['attack', 'a']:
                    attack(myPlayer1, testEnemy)
                    print(testEnemy.hp)
                    myPlayer1.action = myPlayer.action - 1
                    print(myPlayer.action)
               elif player_action.lower() in ['defend', 'd']:
                    print('hello')
                    myPlayer1.action = myPlayer.action - 1
                    print(myPlayer.action)
          
def end_player_turn(enemy1, player1):
     if player1.action <= 1:
          enemy1.action = 2
          print(enemy1.action)
          print("hello")
          enemy_turn(enemy1, player1)

def enemy_turn(enemy, player):
     while enemy.action >= 1:
          random_action = random.randint(1, 2)
          if random_action == 1:
               print("The enemy attacked!")
               attack(enemy, player)
          if random_action == 2:
               enemy_defend(enemy)
     if enemy.action <= 1:
          player_turn()
          


myPlayer = Player()
myPlayer1 = Player()
testEnemy = Imp()
testEnemy.activedefense = 1
def Fight_test():
     print("test")
     role_selection()
     print("Fight time")
     myPlayer1.action = 2
     print("Enemy HP: " + str(testEnemy.hp))
     print("Enemy Defenses: \n" "  magical: " + str(testEnemy.mdefense) + "\n  physical: " + str(testEnemy.defense))
     print("Player Attack:\n  magical: " + str(myPlayer1.mattack) + "\n  physical: " + str(myPlayer1.attack))
     while myPlayer1.hp >= 0 and testEnemy.hp >=0:
          player_turn()
     if myPlayer1.action <= 1:
               end_player_turn(testEnemy, myPlayer1)
     
          


def role_selection():
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
     while option.lower() not in ['play', 'p', 'help', 'h', 'quit', 'test', 'attack']:
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
