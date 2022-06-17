import random
from . import participant as part
import copy


class my_own_player(part.Participant):
    def __init__(self):
        super().__init__('name of your team', 'team num')
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
        # you can override this method in this sub-class
        # you can refer to an object of 'marbles', named as 'playground_marbles'
        # the return should be the number of marbles bet (> 0)!
        my_current_marbles = playground_marbles.get_num_of_my_marbles(self)
        com_dec_list=[] #컴퓨터 추측 결과(홀(True)짝(False))를 모은 데이터
        if not com_dec_list:  # list가 비어있을 때(처음 상태)
             return 1
        ratio = com_dec_list.count(True) / len(com_dec_list) #list 중 컴퓨터가 홀수라 예측한 비율
        if ratio > 0.5 and my_current_marbles >=2: #홀수 예측 비율이 더 높고 현재 구슬이 2개 이상이면
            return 2 #2 반환
        else: return 1

    def declare_statement_strategy(self, playground_marbles):
        # you can override this method in this sub-class
        # you can refer to an object of 'marbles', named as 'playground_marbles'
        # the return should be True or False!
        com_bet_list = []  # 컴퓨터 베팅결과를 모은 데이터(홀수는 True, 짝수는 False로 변환해서 저장)
        if not com_bet_list:  # list가 비어있을 때(처음 상태)
             return bool(random.randint(0, 1)) #무작위로 선택
        ratio = com_bet_list.count(True) / len(com_bet_list) #컴퓨터가 홀수개를 베팅한 비율
        if ratio > 0.5: return True #모비율이 0.5보다 클 때 무조건 홀수라 답하는 게 유리(표본비율X)
        elif ratio == 0.5: return bool(random.randint(0, 1))
        else: return False
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
            if self.position < length - 1:  # 카피 한 것보다 앞에 있으면
                print(self.temp_list)
                # print('chk1')
                return self.temp_list[self.position]  # 내가 갔던 곳으로
            else:
                if self.position == length - 1:
                    # print('chk2')
                    if self.temp_list[self.position] == 0:
                        return 1
                    else:
                        return 0
                else:
                    # print('chk3')
                    return random.randint(0, 1)
        return random.randint(0, 1)
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
        return (0, 0, 5, 5)

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