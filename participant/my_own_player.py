import random
from . import participant as part
import copy

marble_count = []


class my_own_player(part.Participant):
    def __init__(self):
        super().__init__('name of your team', 'team num')
        global marble_count
        global bet_list
        global dec_list
        global co
        global do
        marble_count = []
        bet_list = [1, 2]
        dec_list = [True, False]
        co = 0
        do = 0
        # you can change everything in this code file!!
        # also, you can define your own variables here or in the overriding method
        # Any modifications are possible if you follows the rules of Squid Game

    # ====================================================================== for initializing your player every round
    def initialize_player(self, string):
        # you can override this method in this sub-class
        # this method must contain 'self.initialize_params()' which is for initializing some essential variables
        # you can initialize what you define
        self.initialize_params()

    # ====================================================================== for initializing your player every round

    # ================================================================================= for marble game
    def bet_marbles_strategy(self, playground_marbles):
        global my_current_marbles
        my_current_marbles = playground_marbles.get_num_of_my_marbles(self)
        marble_count.append(my_current_marbles)
        co = 0
        if len(marble_count) <= 1:
            return 1
        else:
            max_marble = max(marble_count)
            if marble_count[-1] >= max_marble:
                return bet_list[co % 2]
            else:
                co += 1
                return bet_list[(co) % 2]
        # you can override this method in this sub-class
        # you can refer to an object of 'marbles', named as 'playground_marbles'
        # the return should be the number of marbles bet (> 0)!

    def declare_statement_strategy(self, playground_marbles):
        # you can override this method in this sub-class
        # you can refer to an object of 'marbles', named as 'playground_marbles'
        # the return should be True or False!

        # answer = bool(random.randint(0, 1))
        do = 0
        if len(marble_count) <= 1:
            return True
        else:
            max_marble = max(marble_count)
            if marble_count[-1] >= max_marble:
                answer = dec_list[do % 2]
            else:
                do += 1
                answer = dec_list[(do) % 2]

        return self.set_statement(answer)
    # ================================================================================= for marble game


    # ================================================================================= for glass_stepping_stones game
    def step_toward_goal_strategy(self, playground_glasses):
        # you can override this method in this sub-class
        # you can refer to an object of 'glass_stepping_stones', named as 'playground_glasses'
        # the return should be 0 or 1 (int)!
        if self.position == 0:
            self.temp_list = copy.deepcopy(playground_glasses._players_steps)  # 상대방것도 복사
        length = len(self.temp_list)
        if self.previous_player != 'None' and self.temp_list != []:
            if self.position < length - 1:  #우리 player의 위치가 length보다 뒤(결승점에서 먼 지점)에 있을 때
                print(self.temp_list)   #기억해 둔 temp_list를 출력해서
                # print('chk1')
                return self.temp_list[self.position]  # 내가 갔던 경로대로 따라감
            else:
                if self.position == length - 1: #우리 player의 위치가 length와 같을 때
                    # print('chk2')
                    if self.temp_list[self.position] == 0:
                        return 1
                    else:
                        return 0
                else:   #우리 player의 위치가 length보다 앞(결승점에서 가까운 지점)에 있을 때
                    # print('chk3')
                    return random.randint(0, 1)
        return random.randint(0, 1) #랜덤으로 좌/우 중에 선택하여 전진
    # ================================================================================= for glass_stepping_stones game


    # ================================================================================= for tug_of_war game
    def gathering_members(self):
        # you can override this method in this sub-class
        # this method gathers your members for the tug of war game
        # you only can change the configuration of the numbers of person types
        # there are 4 types of persons
        # type1 corresponds a ordinary person who has standard stats for the game
        # type2 corresponds a person with great height
        # type3 corresponds a person with a lot of weight
        # type4 corresponds a person with strong power
        # the return should be a tuple with size of 4, and the sum of the elements should be 10
        # only for computer, it is allowed to set 12 members
        return (0, 0, 5, 5) #이 조합을 default로 다양한 조합 시뮬레이션

    def act_tugging_strategy(self, playground_tug_of_war):
        # you can override this method in this sub-class
        # you can refer to an object of 'tug_of_war', named as 'playground_tug_of_war'
        # the return should be a float value in [0, 100]!
        # note that the float represents a stamina-consuming rate for tugging
        if playground_tug_of_war.player_condition['Computer'] == False:
            if playground_tug_of_war.player_expression[self.name] in ['best', 'well']:
                return 15
            else:
                return 10
        else:
            if playground_tug_of_war.player_expression['Computer'] in ['best', 'well']:
                return 0
            else:
                if playground_tug_of_war.player_expression[self.name] in ['best', 'well']:
                    return 30 + random.randint(0, 3)
                else:
                    return random.randint(0, 3)
    # ================================================================================= for tug_of_war game