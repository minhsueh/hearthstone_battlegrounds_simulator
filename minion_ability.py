
import random
from cardpool import *

class minion():
    def __init__(self, 
                attack: int,
                blood: int, 
                tier: int, 
                name: None,
                type_ = None, #beast, demon, dragon, elemental, mech, nurloc, pirate
                taunt = False,
                shield = False, 
                windfury = False,
                poison = False,
                cleave = False,
                reborn = False,
                charge = False,
                position = -1,
                **kwargs):
        #minion paroperites
        self.name = name
        self.attack = attack
        self.blood = blood
        self.tier = tier #1 - 6
        self.type = type_
        self.taunt = taunt
        self.shield = shield
        self.windfury = windfury
        self.poison = poison
        self.cleave = cleave
        self.reborn = reborn
        self.charge = charge
        self.position = position
        #combat parameters
        self.already_attacked = False


        '''
        self.round_start_effect = False
        self.attacking_effect = False
        self.deathrattle = False
        self.friend_die = False
        self.been_attacking = False

        self.multiple_battlecry = False
        self.multiple_summon = False
        self.multiple_deathrattle = False
        '''
        self.skill = kwargs
        '''
        {
        'battlecry': , 
        'round_start_effect': ,
        'attacking_effect': , 
        'deathrattle': ,
        'friend_die': ,
        'been_attacking': 
        'multiple_battlecry':
        'multiple_summon': Khargar->2, gold Khargar->3
        'multiple_deathrattle': baren->2; gold baren->3
        }
        '''
'''
To do list:
--------------------
first version:::::
deathrattle:

start of combat:


ScavengingHyena
--------------------
battlecry:
RockpoolHunter
Alleycat
DeckSwabbie
RefreshingAnomaly
RockpoolHunter
ValgarHomunculus

other:
MurlocTidecaller
MicroMummy
MicroMachine
WrathWeaver
'''

#general function:
def add_attack_to_friend(itself, A_deck, B_deck):
    random.choice(A_deck.deck).attack += itself.attack



#class minion_skill_round_start_effect():

def RedWhelp(itself, attacker, defender):
    dmg = 0
    for i in attacker.deck:
        if i.type == 'Dragon':
            dmg += 1
    random.choice(defender.deck).blood -= dmg



#class deathrattle():
def FiendishServant_deathrattle(itself, A_deck, B_deck):
    random.choice(A_deck.deck).attack += itself.attack

def Scallywag_deathrattle(itself, A_deck, B_deck): 
    #ref: https://www.youtube.com/watch?v=RrCFhSBRBeQ, 5:38
    SkyPirate = minion(1, 1, 1, name = 'Sky Pirate', type_ = 'Pirate', charge = True)
    A_deck.summon(itself.position, SkyPirate)

