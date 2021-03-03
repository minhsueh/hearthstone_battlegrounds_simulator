

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
#1 star minion:
RockpoolHunter = minion(2, 3, 1, name = 'Rockpool Hunter', type_ = 'murloc', battlecry = None)
AcolyteOfCThun = minion(2, 2, 1, name = 'Acolyte of C\'Thun', taunt = True, reborn = True)
Alleycat = minion(1, 1, 1, name = 'Alleycat', battlecry = None)
Tabbycat = minion(1, 1, 1, name = 'Tabbycat')








