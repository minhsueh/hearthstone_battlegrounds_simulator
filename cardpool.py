import random
from minion_ability import *
from copy import deepcopy

'''
tier1: 18 * 8
tier2: 15 * 8
tier3: 13 * 8
tier4: 11 * 8
tier5: 9 * 8
tier6: 6 * 8
'''


#1 star minion:
RockpoolHunter = minion(2, 3, 1, name = 'Rockpool Hunter', type_ = 'Murloc', battlecry = None)
AcolyteOfCThun = minion(2, 2, 1, name = 'Acolyte of C\'Thun', taunt = True, reborn = True)
Alleycat = minion(1, 1, 1, name = 'Alleycat', battlecry = None, type_ = 'Beast')
DeckSwabbie = minion(2, 2, 1, name = 'Deck Swabbie', type_ = 'Pirate')
DragonspawnLieutenant = minion(2, 3, 1, name = 'Dragonspawn Lieutenant', taunt = True, type_ = 'Dragon')
FiendishServant = minion(2, 1, 1, name = 'Fiendish Servant', type_ = 'Demon', deathrattle = FiendishServant_deathrattle)

MicroMachine = minion(1, 2, 1, name = 'Micro Machine', type_ = 'Mech')
MicroMummy = minion(1, 2, 1, name = 'Micro Mummy', reborn = True, type_ = 'Mech')
MurlocTidecaller = minion(1, 2, 1, name = 'Murloc Tidecaller', type_ = 'Murloc')
MurlocTidehunter = minion(2, 1, 1, name = 'Murloc Tidehunter', battlecry = None, type_ = 'Murloc')
RedWhelp = minion(1, 2, 1, name = 'Red Whelp', type_ = 'Dragon', round_start_effect = RedWhelp)
RefreshingAnomaly = minion(1, 3, 1, name = 'Refreshing Anomaly', type_ = 'Elemental')
Scallywag = minion(2, 1, 1, name = 'Scallywag', type_ = 'Pirate', deathrattle = Scallywag_deathrattle)
ScavengingHyena = minion(2, 2, 1, name = 'Scavenging Hyena', type_ = 'Beast')
Sellemental = minion(2, 2, 1, name = 'Sellemental', type_ = 'Elemental')
ValgarHomunculus = minion(2, 4, 1, name = 'Valgar Homunculus', type_ = 'Demon')
WrathWeaver = minion(1, 3, 1, name = 'Wrath Weaver')

MurlocScout = minion(1, 1, 1, name = 'Murloc Scout', type_ = 'Murloc')
SkyPirate = minion(1, 1, 1, name = 'Sky Pirate', type_ = 'Pirate', charge = True)
Tabbycat = minion(1, 1, 1, name = 'Tabbycat', type_ = 'Beast')



