import numpy as np 
import matplotlib.pyplot as plt
import time

#mapping every combination with it's assigned value
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

#create a new array where it modifies the state
def state_update(current_state, rule):
    new_state = np.zeros_like(current_state)
    for i in range(1, len(current_state) - 1):
        trio = str(current_state[i-1]) + str(current_state[i]) + str(current_state[i+1])
        new_state[i] = rule[trio]
    return new_state

#creating the first state and showing the plot as it evolves
def main():
    initial_array = np.zeros(51, dtype=int)
    initial_array[25] = 1
    rule = rule_to_binary(176)
    num_steps = 50
    
    plt.ion()
    fig, ax = plt.subplots()
    ax.set_axis_off()  
    img = ax.imshow([initial_array], cmap="binary", aspect="auto")

    current_state = initial_array
    for i in range(num_steps):
        img.set_data(np.vstack((img.get_array(), current_state)))
        plt.draw()
        plt.pause(0.3) 
        current_state = state_update(current_state, rule)

    plt.ioff()  
    plt.show()  

if __name__ == "__main__":
    main()