# HearthStone battlegrounds winning simularor

'''
To do list:

minion:
when summon mech, having sheild?
lose shield, add attack
baron, khadgar

comabt:


card_pool:


'''

class minion_skill_round_start_effect():

    def RedWhelp(A_deck, B_deck):
        dmg = 0
        for i in A_deck
            if i.type = dragon:
                dmg += 1
        random.choice(B_deck).blood -= dmg



class minion():
    def __init__(self, 
                attack: int,
                blood: int, 
                star: int, 
                name: None,
                type_ = None, #beast, demon, dragon, elemental, mech, nurloc, pirate
                **kwargs):
        #minion paroperites
        self.name = name
        self.attack = attack
        self.blood = blood
        self.star = star #1 - 6
        self.type = type_
        self.taunt = False
        self.shield = False
        self.windfury = False
        self.poison = False
        self.cleave = False
        self.reborn = False
        self.round_start_effect = False
        self.attacking_effect = False
        self.deathrattle = False
        self.friend_die = False
        self.been_attacking = False
        
        #combat parameters
        self.already_attacked = False


        self.skill = **kwargs
        '''
        {'round_start_effect': ,
        'attacking_effect': , 
        'deathrattle': ,
        'friend_die': ,
        'been_attacking': 
        }
        '''

class deck():
    def __init__(self):
        self.deck = []

    def add(self, minion):
        self.deck.append(minion)

    def death(self,minion_position):
        self.deck.pop(minion_position)
    
    def deck_add_blood(self, blood_AddValue):
        for i in self.deck:
            i.blood += blood_AddValue

    def deck_add_attack(self, attack_AddValue):
        for i in self.deck:
            i.attack += attack_AddValue

    def deck_add_shield(self, type):
        for i in self.deck:
            i.shield = True

    def taunt_exist(self):
        taunt_list = []
        for i in range(len(self.deck)):
            if self.deck[i].taunt:
                taunt_list.append(i)
        return(taunt_list)

    def round_start_effect_exist(self):
        effect_list = []
        for i in range(len(self.deck)):
            if self.deck[i].round_start_effect:
                effect_list.append(i)
        return(effect_list)

    def check_attacker_position(self):

        if self.deck[-1].already_attacked == True:
            return(0)
        for i, x in reversed(list(enumerated(self.deck))):
            if x.already_attacked == True:
                return(i+1)
        return(0)

    def check_death(self):
        death_list = []
        for i in range(len(self.deck)):
            if i.blood <= 0:
                death_list.append(i)
        return(death_list)

    def apply_deathrattle(self):
        #baran???
        death_list = self.check_death()
        for i in death_list:
            i.skill['deathrattle']()

class battlegrounds():
    def __init__(self, A_deck, B_deck):
        self.A_deck = A_deck
        self.B_deck = B_deck
        self.A_deck_attacker_position = 0
        self.B_deck_attacker_position = 0


    

    def minion_combat(self, attacker_deck, defender_deck, attacker_position):

        if len(defender.taunt_exist) != 0:
            defender_position = random.choice(defender_deck.taunt_exist)
        else:
            defender_position = random.choice(range(len(defender_deck)))
        '''
        when attacking 
        '''
        if attacker_deck[attacker_position].attacking_effect:
            #apply effect

        #coefficient:
        attacker_coef = 1
        defender_coef = 1
        cleave_right_coef = 1
        ##shield
        if attacker_deck[attacker_position].shield:
            attacker_deck[attacker_position].shield = False
            defender_coef *= 0
        if defender_deck[defender_position].shield:
            defender_deck[defender_position].shield = False
            attacker_coef *= 0
        ##poison
        if attacker_deck[attacker_position].poison:
            attacker_coef *= 99999
        if defender_deck[defender_position].poison:
            defender_coef *= 99999


        #final blood coef. calculation
        defender_deck[defender_position].blood -= (attacker_deck[attacker_position].attack*attacker_coef)
        attacker_deck[attacker_position].blood -= (defender_deck[defender_position].attack*defender_coef)

        ##cleave effect
        ###cleave right
        if defender_position+1 < len(defender_deck):
            if defender_deck[defender_position+1].shield:
                defender_deck[defender_position+1].shield = False
            else:
                defender_deck[defender_position+1].blood -= (attacker_deck[attacker_position].attack)

        ###cleave left
        if defender_position-1 >= 0:
            if defender_deck[defender_position-1].shield:
                defender_deck[defender_position-1].shield = False
            else:
                defender_deck[defender_position-1].blood -= (attacker_deck[attacker_position].attack)


    def combat(self):
    
        ##determine first attacker
        ##self.attacker = True -----> A
        if len(self.A_deck) > len(self.B_deck):
            self.attacker = True
        elif len(self.A_deck) < len(self.B_deck):
            self.attacker = False
        else:
            self.attacker = random.choice([True, False])


        '''
        start of combat effect
        '''
        if self.attacker:
            if self.A_deck.round_start_effect_exist:
                #apply effect
                for idx in self.A_deck.round_start_effect_exist:
                    A_deck[idx].skill['round_start_effect'](A_deck, B_deck)
                #check death and deathrattle
                B_deck.apply_deathrattle()
                self.B_deck_attacker_position = B_deck.check_attacker_position()
            
            if self.B_deck.round_start_effect_exist: 
                #apply effect
                for idx in self.B_deck.round_start_effect_exist:
                    B_deck[idx].skill['round_start_effect'](B_deck, A_deck)
                #check death and deathrattle
                A_deck.apply_deathrattle()
                self.A_deck_attacker_position = A_deck.check_attacker_position()



        #physical combat start
        while(len(self.A_deck) > 0 and len(self.B_deck) > 0):
            if self.attacker:
                self.minion_combat(self, self.A_deck, self.B_deck, self.A_deck_attacker_position)

            else:
                self.minion_combat(self, self.B_deck, self.A_deck, self.B_deck_attacker_position)

            '''
            check death and deathrattle
            '''


            '''
            check_attacker_position

            '''




            #change attacker from A to B, or B to A
            self.attacker = (not self.attacker)

        if len(self.A_deck) > 0:
            return('A')
        elif len(self.B_deck) > 0:
            return('B')
        else:
            return('tie')




