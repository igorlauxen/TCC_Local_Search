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

# I'm considering 10 user used the app
field1 = {"times": 10, "avg_order": 4}
field2 = {"times": 1, "avg_order": 5}
field3 = {"times": 7, "avg_order": 3}
field4 = {"times": 0, "avg_order": 2}
field5 = {"times": 8, "avg_order": 1}

initial_state = [field1, field2, field3, field4, field5]
unused_fields = []

def Simulated_Annealing(max_iter, initial_temperature, alpha, final_temperature, initial_state, unused_labels):
    t = initial_temperature
    current_state = initial_state.copy()
    print("Original State:", current_state)
    print("Energy of Original State:", value(current_state))
    while(t >= final_temperature):
        for i in range(1, max_iter):
            next_state = action_on(current_state)
            energy_delta = value(next_state) - value(current_state)
            if ((energy_delta < 0) or (math.exp( -energy_delta / t) >= random.randint(0,10))):
                current_state = next_state
        t = alpha * t
    print("Final", current_state)
    print("Energy of final state:", value(current_state))

# the more the energy, the worst
def value(state):
    goodVibes=0
    halfOrMoreUsersUsedField = (nrOfUsers / 2) + 1
    minimalUsers = nrOfUsers * 0.3 #30% of users
    avgOrder = (num_fields / 2) + 1

    if(state.times > halfOrMoreUsersUsedField): # more than half of the users used this fields -- GOOD
        goodVibes+=1
    elif(state.avg_order <= avgOrder and state.times > minimalUsers): # even it was not really used, let's consider the place where it is -- GOOD
        goodVibes+=1
    elif( state.avg_order >= avgOrder and state.times < minimalUsers): # field is not used and it's almost forgotten on screen -- BAD
        goodVibes-=1

    energy = num_fields - goodVibes
    return energy # energy of the state