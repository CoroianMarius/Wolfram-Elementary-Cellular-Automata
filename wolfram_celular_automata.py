import numpy as np 

def rule_to_binary(rule_number):
    rule_list = np.array([], dtype=int)
    while rule_number > 0:
        rule_list= np.append(rule_list, rule_number%2)
        rule_number = rule_number//2
    if len(rule_list) < 8:
        for i in range(8-len(rule_list)):
            rule_list= np.append(rule_list, 0)
    return np.flip(rule_list)



initial_array = np.zeros(101, dtype=int)
initial_array[50] = 1
print(rule_to_binary(30))