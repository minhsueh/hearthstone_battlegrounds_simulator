# HearthStone battlegrounds winning simularor

'''
To do list:

minion:
when summon mech, having sheild?
lose shield, add attack
baron, khadgar     V


card_pool:


'''
from cardpool import *
import random
import copy
import sys
from copy import deepcopy



class deck():
    def __init__(self):
        self.deck = []
        self.max_deck_length = 7

    def add(self, minion):
        self.deck.append(deepcopy(minion))

    def death(self,minion_position):
        self.deck.pop(minion_position)

    def check_length(self):
        return(len(self.deck))
    
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
            if self.deck[i].skill.get('round_start_effect', False):
                effect_list.append(i)
        return(effect_list)

    def update_position(self):
        for i in range(len(self.deck)):
            self.deck[i].position = i 

    def check_attacker_position(self):
        if not self.deck:
            return(0)
        if self.deck[-1].already_attacked == True:
            return(0)
        for i, x in reversed(list(enumerate(self.deck))):
            if x.already_attacked == True:
                return(i+1)
        return(0)

    def check_full_deck(self):
        if len(self.deck) == self.max_deck_length:
            return(True)
        else:
            return(False)

    ###summon
    def check_multiple_summon(self):
        base = 1
        for i in self.deck:
            if i.skill.get('multiple_summon', False):
                base *= i.skill['multiple_summon']
        return(base)

    def summon(self, summoner_position, minion):
        N_summon = self.check_multiple_summon()
        counter = 1
        while(counter <= N_summon):
            if not self.check_full_deck():
                self.deck.insert(summoner_position, deepcopy(minion))
            else:
                return
            counter += 1

    ##charge
    def check_charge(self):
        for i in range(len(self.deck)):
            if self.deck[i].charge:
                return([i])
        return(False)


    #deathrattle
    def check_deathrattle_exist(self, query):
        if not query:
            return
        deathrattle_list = []
        for i in range(len(query)):
            if query[i].skill.get('deathrattle', False):
                deathrattle_list.append(i)
        return(deathrattle_list)


    def check_multiple_deathrattle(self):
        base = 1
        for i in self.deck:
            if i.skill.get('multiple_deathrattle', False):
                base = max(base, i.skill['multiple_deathrattle'])
        return(base)

    def check_death(self):
        death_list = []
        N = len(self.deck)
        while(N > 0):
            if self.deck[N-1].blood <= 0:
                if self.deck[N-1].reborn:
                    self.deck[N-1].blood = 1
                    self.deck[N-1].reborn = False
                    self.deck[N-1].already_attacked = False
                else:
                    death_list.append(self.deck.pop(N-1))
            N -= 1
        death_list.reverse()
        return(death_list)

    def check_single_minion_death(self, position):
        if self.deck[position].blood <= 0:
            self.deck.pop(position)
            return(True)
        else:
            return(False)


class battlegrounds():
    def __init__(self, A_deck, B_deck, verbose = False):
        self.A_deck = A_deck
        self.B_deck = B_deck
        self.A_deck_attacker_position = 0
        self.B_deck_attacker_position = 0

        self.verbose = verbose

        self.poison_attack = 99999


    def update_all_deck_position(self):
        self.A_deck.update_position()
        self.B_deck.update_position()

    def apply_round_start_effect(self, attacker, defender):
        #apply effect
        for idx in attacker.round_start_effect_exist():
            attacker.deck[idx].skill['round_start_effect'](attacker.deck[idx], attacker, defender)
        #check death and deathrattle
        self.apply_all_deathrattle(defender, attacker)
        if self.verbose:
            self.visulization()
        self.update_all_deck_position()
            

    def apply_all_deathrattle(self, deathrattle_deck, be_affected_deck):
        death_list = deathrattle_deck.check_death()
        if deathrattle_deck.check_deathrattle_exist(death_list):
            N_deathrattle = deathrattle_deck.check_multiple_deathrattle()
            for i in death_list:
                counter = 1
                while(counter <= N_deathrattle):
                    i.skill['deathrattle'](i, deathrattle_deck, be_affected_deck) 
                    
                    #if having charge
                    self.update_all_deck_position()
                    while(deathrattle_deck.check_charge()):
                        
                        self.check_win()
                        self.apply_all_deathrattle(be_affected_deck, deathrattle_deck)
                        self.update_all_deck_position()
                        charge_idx = deathrattle_deck.check_charge()[0]
                        if self.verbose:
                            self.visulization()
                        self.minion_combat(deathrattle_deck, be_affected_deck, charge_idx)
                        if not deathrattle_deck.check_single_minion_death(charge_idx):
                            deathrattle_deck[charge_idx].charge = False
                        

                        self.update_all_deck_position()
                        #self.apply_all_deathrattle(deathrattle_deck, be_affected_deck)
                        self.apply_all_deathrattle(be_affected_deck, deathrattle_deck) 
                    self.B_deck_attacker_position = self.B_deck.check_attacker_position()
                    self.A_deck_attacker_position = self.A_deck.check_attacker_position()
                    

                    counter += 1

    

    def minion_combat(self, attacker_deck, defender_deck, attacker_position):

        if len(defender_deck.taunt_exist()) != 0:
            defender_position = random.choice(defender_deck.taunt_exist())
        else:
            defender_position = random.choice(range(defender_deck.check_length()))
        '''
        when attacking 
        
        if attacker_deck[attacker_position].attacking_effect:
            #apply effect
            attacker_deck[attacker_position].attacking_effect()
        '''

        #coefficient:
        attacker_coef = 1
        defender_coef = 1
        cleave_right_coef = 1
        ##shield
        if attacker_deck.deck[attacker_position].shield:
            attacker_deck.deck[attacker_position].shield = False
            defender_coef *= 0
        if defender_deck.deck[defender_position].shield:
            defender_deck.deck[defender_position].shield = False
            attacker_coef *= 0
        ##poison
        if attacker_deck.deck[attacker_position].poison:
            attacker_coef *= self.poison_attack
        if defender_deck.deck[defender_position].poison:
            defender_coef *= self.poison_attack


        #final blood coef. calculation
        defender_deck.deck[defender_position].blood -= (attacker_deck.deck[attacker_position].attack*attacker_coef)
        attacker_deck.deck[attacker_position].blood -= (defender_deck.deck[defender_position].attack*defender_coef)

        ##cleave effect
        if attacker_deck.deck[attacker_position].cleave:
            ###cleave right
            if defender_position+1 < defender_deck.check_length():
                if defender_deck.deck[defender_position+1].shield:
                    defender_deck.deck[defender_position+1].shield = False
                else:
                    defender_deck.deck[defender_position+1].blood -= (attacker_deck.deck[attacker_position].attack)

            ###cleave left
            if defender_position-1 >= 0:
                if defender_deck.deck[defender_position-1].shield:
                    defender_deck.deck[defender_position-1].shield = False
                else:
                    defender_deck.deck[defender_position-1].blood -= (attacker_deck.deck[attacker_position].attack)

        ####
        attacker_deck.deck[attacker_position].already_attacked = True

        
    def check_win(self):
        if len(self.A_deck.deck) == 0 and len(self.B_deck.deck) == 0:
            print('tie')
            sys.exit()
        elif len(self.A_deck.deck) == 0:
            print('B')
            sys.exit()
        elif len(self.B_deck.deck) == 0:
            print('A')
            sys.exit()


    def combat(self):
    
        ##determine first attacker
        ##self.attacker = True -----> A
        if self.A_deck.check_length() > self.B_deck.check_length():
            self.attacker = True
        elif self.B_deck.check_length() > self.A_deck.check_length():
            self.attacker = False
        else:
            self.attacker = random.choice([True, False])

        if self.verbose:
            self.visulization()

        '''
        start of combat effect
        '''
        self.update_all_deck_position()
        if self.attacker:
            if self.A_deck.round_start_effect_exist():
                self.apply_round_start_effect(self.A_deck, self.B_deck)
                self.B_deck_attacker_position = self.B_deck.check_attacker_position()
            
            if self.B_deck.round_start_effect_exist(): 
                self.apply_round_start_effect(self.B_deck, self.A_deck)
                self.A_deck_attacker_position = self.A_deck.check_attacker_position()
        else:
            if self.B_deck.round_start_effect_exist(): 
                self.apply_round_start_effect(self.B_deck, self.A_deck)
                self.A_deck_attacker_position = self.A_deck.check_attacker_position()
            if self.A_deck.round_start_effect_exist():
                self.apply_round_start_effect(self.A_deck, self.B_deck)
                self.B_deck_attacker_position = self.B_deck.check_attacker_position()


        self.check_win()
        #physical combat start
        while(self.A_deck.check_length() > 0 and self.B_deck.check_length() > 0):
            if self.verbose:
                self.visulization()

            if self.attacker:
                self.minion_combat(self.A_deck, self.B_deck, self.A_deck_attacker_position)
                #check death and deathrattle
                self.apply_all_deathrattle(self.A_deck, self.B_deck)
                #self.update_all_deck_position()
                self.apply_all_deathrattle(self.B_deck, self.A_deck) 
                #self.update_all_deck_position()
                #check_attacker_position
                self.B_deck_attacker_position = self.B_deck.check_attacker_position()
                self.A_deck_attacker_position = self.A_deck.check_attacker_position()
            else:
                self.minion_combat(self.B_deck, self.A_deck, self.B_deck_attacker_position)
                #check death and deathrattle
                self.apply_all_deathrattle(self.B_deck, self.A_deck) 
                #self.update_all_deck_position()
                self.apply_all_deathrattle(self.A_deck, self.B_deck)
                #self.update_all_deck_position()
                #check_attacker_position
                self.A_deck_attacker_position = self.A_deck.check_attacker_position()
                self.B_deck_attacker_position = self.B_deck.check_attacker_position()

            #change attacker from A to B, or B to A
            self.attacker = (not self.attacker)

        if self.verbose:
            self.visulization()

        if self.A_deck.check_length() > 0:
            return('A')
        elif self.B_deck.check_length() > 0:
            return('B')
        else:
            return('tie')

    def visulization_single(self, deck):
        vis_list = []
        for i in deck.deck:
            status = ''
            if i.shield:
                status += 'S'
            if i.taunt:
                status +='T'
            if i.reborn:
                status += 'R'
            if i.skill.get('deathrattle', False):
                status += 'D'
            vis_list.append((status, i.attack, i.blood))
        return(vis_list)

    def visulization(self):
        B_vis = self.visulization_single(self.B_deck)
        A_vis = self.visulization_single(self.A_deck)
        print('==================================')
        print(B_vis)
        print('----------------------------------')
        print(A_vis)
        print('==================================')





class combat_calculator():
    def __init__(self, N = 1000):
        #player represent A_deck
        self.N = N
    def calculate(self, A_deck, B_deck):
        A_win = 0
        B_win = 0
        tie = 0
        for i in range(self.N):
            A_cp = copy.deepcopy(A_deck)
            B_cp = copy.deepcopy(B_deck)
            bg = battlegrounds(A_cp, B_cp)
            result = bg.combat(verbose = False)
            if result == 'A':
                A_win += 1
            elif result == 'B':
                B_win += 1
            else:
                tie += 1
        print('=======================================')
        print('| win: '+ str(round(A_win/self.N*100, 2))+'%, tie: '+ str(round(tie/self.N*100, 2))+'%, lose: '+ str(round(B_win/self.N*100, 2)) + '%  |')
        print('=======================================')

def main():
    A_deck = deck()
    B_deck = deck()

    
    
    A_deck.add(Scallywag)
    #A_deck.add(Scallywag)
    #A_deck.add(RockpoolHunter)
    #A_deck.add(AcolyteOfCThun)
    
    #B_deck.add(ValgarHomunculus)
    #B_deck.add(ValgarHomunculus)
    #B_deck.add(AcolyteOfCThun)
    B_deck.add(RedWhelp)
    


    bg = battlegrounds(A_deck, B_deck, verbose = True)
    print(bg.combat())
    #cc = combat_calculator()
    #cc.calculate(A_deck, B_deck)



if __name__ == '__main__':
    main()



