import numpy as np 
import time

def rule_to_binary(rule_number):
    rule_list = np.array([], dtype=int)
    while rule_number > 0:
        rule_list= np.append(rule_list, rule_number%2)
        rule_number = rule_number//2
    if len(rule_list) < 8:
        for i in range(8-len(rule_list)):
            rule_list= np.append(rule_list, 0)
    rule_list = np.flip(rule_list)
    rule = {"111":rule_list[0], "110":rule_list[1], "101":rule_list[2], "100":rule_list[3], "011":rule_list[4], "010":rule_list[5], "001":rule_list[6], "000":rule_list[7]}
    return rule

def state_update(current_state, rule):
    new_state = np.zeros_like(current_state)
    for i in range(1, len(current_state) - 1):
        trio = str(current_state[i-1]) + str(current_state[i]) + str(current_state[i+1])
        new_state[i] = rule[trio]
    return new_state

def main():
    initial_array = np.zeros(101, dtype=int)
    initial_array[50] = 1
    rule = rule_to_binary(30)
    while 1==1:
        print(initial_array)
        print(state_update(initial_array, rule))
        initial_array= state_update(initial_array, rule)
        time.sleep(0.3)



if __name__ == "__main__":
    main()