# Simulated Annealing for Clustering Problems
import math
import random

## idea: I'll cluster into used and nonused fields
# parametros para mudar a temperatura: uso e ordem
# maior numero de uso e menor for a ordem mais energia
num_fields=5
num_cost_increases = 100
avg_cost_increase = 200
acc_ratio = 0.75 # acceptance ratio should e between 0 and 1
prob_e = 0.00000000001 # probability factor
beta = 0.125
max_iter = 4 * num_fields # maximum number of iterations
num_temp = 200
nrOfUsers = 10

initial_temperature = avg_cost_increase / math.log( num_cost_increases / ((num_cost_increases * acc_ratio) - (1-acc_ratio) * (max_iter - num_cost_increases)))
final_temperature = -beta * avg_cost_increase / math.log(prob_e)
alpha = math.pow(final_temperature / initial_temperature , 1 / num_temp) # decay rate for temperature

# I'm considering 10 user using the app
field1 = {"times": 10, "avg_order": 4}
field2 = {"times": 1, "avg_order": 5}
field3 = {"times": 7, "avg_order": 3}
field4 = {"times": 0, "avg_order": 2}
field5 = {"times": 8, "avg_order": 1}

initial_state = [field1, field2, field3, field4, field5]
unused_fields = []

def Simulated_Annealing(max_iter, initial_temperature, alpha, final_temperature, initial_state):
    t = initial_temperature
    current_state = initial_state.copy()
    while(t >= final_temperature):
        print("Original State:", current_state)
        for i in range(1, max_iter):
            next_state = action_on(current_state)
            next_value = value(next_state)
            current_value = value(current_state)
            energy_delta = next_value - current_value
            print ("For index "+str(i)+": Calculate " + str(next_value) + " - " + str(current_value) + " = " + str(energy_delta))
            if ((energy_delta < 0) or (math.exp( -energy_delta / t) >= random.randint(0,10))):
                current_state = next_state
        t = alpha * t
    print("Final", current_state)
    print("Energy of final state:", value(current_state))

# the more the energy, the worst
def value(state):
    energy=0
    halfOrMoreUsersUsedField = (nrOfUsers / 2) + 1
    minimalUsers = nrOfUsers * 0.3 #30% of users
    avgOrder = (num_fields / 2) + 1

    ## if the worst case is in the front, then the worst the energy will be
    for i in range(0, len(state)):
        position = state[i]
        times = position['times']
        position = position['avg_order']
        if (position >= avgOrder and times < minimalUsers):  # field is not used and it's almost forgotten on screen -- BAD
            penality = len(state) - i
            energy += penality + 1
        elif (times < minimalUsers):
            penality = len(state) - i
            energy += penality + 1
        elif (times > halfOrMoreUsersUsedField): # more than half of the users used this fields -- GOOD
            energy += 1
        elif (position <= avgOrder and times > minimalUsers): # even it was not really used, let's consider the place where it is -- GOOD
            energy +=1

    return energy

def action_on(current_state):
    curr = current_state.copy()
    shuffled = random.sample(curr, len(curr)) # new state
    return shuffled

if __name__ == "__main__":
    Simulated_Annealing(max_iter, initial_temperature, alpha, final_temperature, initial_state)