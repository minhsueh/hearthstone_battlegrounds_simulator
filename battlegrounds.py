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
class minion():
    def __init__(self, 
                name: str,
                attack: int,
                blood: int, 
                star: int, 
                type = None, #beast, demon, dragon, elemental, mech, nurloc, pirate
                **kwargs):

        self.name = None
        self.attack = attack
        self.blood = blood
        self.star = star #1 - 6
        self.type = type
        self.taunt = False
        self.shield = False
        self.poison = False
        self.cleave = False
        self.reborn = False
        self.round_start_effect = False
        self.attacking_effect = False
        self.death_effect = False
        self.friend_die = False
        self.been_attacking = False
        


        self.ability = **kwargs

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



class battlegrounds():
    def __init__(self):


    def check_death(self, minion):
        #input: minion class
        if minion.blood <= 0:
            return(True)
        else:
            return(False)

    def minion_combat(attacker, defender):
        #overkill
        if attacker.ability['instintic']['shield'] == 1:
            defend_coef = 0
        if defender.ability['instintic']['shield'] == 1:
            attack_coef = 0


        #cannot just do this, because if it havve pirate king!!!!!!!!!!!!!!


        attack_coef = 0 if defender.ability['instintic']['shield'] == 1 else 1
        defend_coef = 0 if defender.ability['instintic']['shield'] == 1 else 1
        attacker.blood -= (defender.attack) * attack_coef
        defender.blood -= attacker.attack * defend_coef

    def attack_procedure(self, attacker, defender):
        if len(defender.taunt_exist) != 0:
            self.minion_combat(attacker[0], random.choice(defender.taunt_exist)) 
        else:
            self.minion_combat(attacker[0], random.choice(defender))


    def combat(self, A_deck, B_deck):
        #A_deck, B_deck: list containing minion

        ##determine first attacker
        ##self.attacker = True -----> A
        if len(A_deck) > len(B_deck):
            self.attacker = True
        elif len(A_deck) < len(B_deck):
            self.attacker = False
        else:
            self.attacker = random.choice([True, False])


        while(len(A_deck) > 0 and len(B_deck) > 0):
            if self.attacker:
                self.attack_procedure(self, A_deck, B_deck)
            else:
                self.attack_procedure(self, B_deck, A_deck)







            self.attacker = (not self.attacker)

        if len(A_deck) > 0:
            return('A')
        elif len(B_deck) > 0:
            return('B')
        else:
            return('tie')




