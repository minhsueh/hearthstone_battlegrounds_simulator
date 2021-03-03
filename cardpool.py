

class minion():
    def __init__(self, 
                attack: int,
                blood: int, 
                star: int, 
                name: None,
                type_ = None, #beast, demon, dragon, elemental, mech, nurloc, pirate
                taunt = False,
                shield = False, 
                windfury = False,
                poison = False,
                cleave = False,
                reborn = False,
                **kwargs):
        #minion paroperites
        self.name = name
        self.attack = attack
        self.blood = blood
        self.star = star #1 - 6
        self.type = type_
        self.taunt = taunt
        self.shield = shield
        self.windfury = windfury
        self.poison = poison
        self.cleave = cleave
        self.reborn = reborn
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
FiendishServant,
Scallywag

start of combat:
RedWhelp

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


#1 star minion:
RockpoolHunter = minion(2, 3, 1, name = 'Rockpool Hunter', type_ = 'Murloc', battlecry = None)
AcolyteOfCThun = minion(2, 2, 1, name = 'Acolyte of C\'Thun', taunt = True, reborn = True)
Alleycat = minion(1, 1, 1, name = 'Alleycat', battlecry = None, type_ = 'Beast')
Tabbycat = minion(1, 1, 1, name = 'Tabbycat', type_ = 'Beast')
DeckSwabbie = minion(2, 2, 1, name = 'Deck Swabbie', type_ = 'Pirate')
DragonspawnLieutenant = minion(2, 3, 1, name = 'Dragonspawn Lieutenant', taunt = True, type_ = 'Dragon')
FiendishServant = minion(2, 1, 1, name = 'Fiendish Servant', deathrattle = None, type_ = 'Demon')
MicroMachine = minion(1, 2, 1, name = 'Micro Machine', type_ = 'Mech')
MicroMummy = minion(1, 2, 1, name = 'Micro Mummy', reborn = True, type_ = 'Mech')
MurlocTidecaller = minion(1, 2, 1, name = 'Murloc Tidecaller', type_ = 'Murloc')
MurlocTidehunter = minion(2, 1, 1, name = 'Murloc Tidehunter', battlecry = None, type_ = 'Murloc')
MurlocScout = minion(1, 1, 1, name = 'Murloc Scout', type_ = 'Murloc')
RedWhelp = minion(1, 2, 1, name = 'Red Whelp', type_ = 'Dragon')
RefreshingAnomaly = minion(1, 3, 1, name = 'Refreshing Anomaly', type_ = 'Elemental')
Scallywag = minion(2, 1, 1, name = 'Scallywag', type_ = 'Pirate')
SkyPirate = minion(1, 1, 1, name = 'Sky Pirate', type_ = 'Pirate')
ScavengingHyena = minion(2, 2, 1, name = 'Scavenging Hyena', type_ = 'Beast')
Sellemental = minion(2, 2, 1, name = 'Sellemental', type_ = 'Elemental')
ValgarHomunculus = minion(2, 4, 1, name = 'Valgar Homunculus', type_ = 'Demon')
WrathWeaver = minion(1, 3, 1, name = 'Wrath Weaver')





