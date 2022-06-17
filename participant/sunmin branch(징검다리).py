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