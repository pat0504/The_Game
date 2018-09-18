import random
import textwrap
import sys
import os
import time

def attack(player, enemy):
    player.actions = player.actions - 1
    print("\n")
    enemy.hp = enemy.hp - (round(player.attack - enemy.defense))
    if enemy.hp <= 0:
        enemy.hp = 0
    print(player.Class + " did " + str(round(player.attack - enemy.defense)) + " damage to " + enemy.Class)
    print(enemy.Class + " has " + str(enemy.hp) + " hp remaining")
    print(player.Class + " has " + str(player.actions) + " action left for next turn")
          
class Player:
    def __init__(self):
        self.Class = ''
        self.role = ''
        self.hp = 0
        self.attack = 0
        self.defense = 0
        self.actions = 0


class You(Player):
    def __init__(self):
        self.Class = 'The Player'
        self.role = 'good'
        self.hp = 50
        self.attack = 15
        self.defense = 5
        self.actions = 0

class Enemy(Player):
    def __init__(self):
        self.Class = 'The Enemy'
        self.role = 'bad'
        self.hp = 40
        self.attack = 15
        self.defense = 6
        self.actions = 0


You1 = You()
The_Enemy = Enemy()

print(The_Enemy.hp)
print("You did " + str(You1.attack - The_Enemy.defense) + " damage to " + str(The_Enemy.Class))
The_Enemy.hp = The_Enemy.hp - int(You1.attack - The_Enemy.defense)
def enemy_description(enemy):
    print("Enemy HP: " + str(enemy.hp))
    print("Enemy Defense: " + str(enemy.defense))
    print("Enemy Attack: " + str(enemy.attack))
    
def player_turn(player, enemy):
    while player.hp > 0 and enemy.hp > 0:
        if player.actions >= 1 and player.role == 'good':
            print("\n" + "It is your turn.")
            player_action = input('> ')
            valid_actions = ['attack', 'a']
            if player_action.lower() in valid_actions:
                attack(player, enemy)
            while player_action.lower() not in valid_actions:
                print("Invalid Command")
                player_action = input('> ')
                if player_action.lower() in valid_actions:
                    attack(player, enemy)
        if player.actions == 0 and enemy.actions == 0:
            enemy.actions = enemy.actions + 2
            player.role = 'exhausted'
        if enemy.actions > 1 and player.role == 'exhausted':
            die = random.randint(1,6)
            print("Die roll: " + str(die))
            if die >= 1:
                attack(enemy, player)
        if enemy.actions == 1 and player.role == 'exhausted':
            die = random.randint(1,6)
            print("Die roll: " + str(die))
            if die >= 1:
                attack(enemy, player)
        if enemy.actions == 0 and player.role == 'exhausted':
            player.role = 'good'
            player.actions = player.actions + 2
    if player.hp > 0 and enemy.hp <= 0:
        print(player.Class + " has defeated " + enemy.Class + "!")
        
    
    
        
            
            
enemy_description(The_Enemy)
You1.actions = 2
player_turn(You1, The_Enemy)













    
