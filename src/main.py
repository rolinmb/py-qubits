import math
import cmath
import os
# Don't ask me about this random function, I found it on Stack Overflow years ago
# Returns a float (or a double?) in the inclusive range [0, 1]
def get_true_pyrand():
    return int.from_bytes(os.urandom(8), byteorder="big") / ((1 << 64) - 1)

class qubit:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1

    def measure(self):
        if self.c0 == 1.0j and self.c1 == 0+0j:
            return 0
        elif self.c0 == 0+0j and self.c1 == 1+0j:
            return 1
        this_obs = get_true_pyrand()
        prob0 = abs(self.c0)**2
        prob1 = abs(self.c1)**2
        largest_prob = max(prob0, prob1)
        if prob0 == prob1: # Coinflip scenario
            return int(round(this_obs, 0))
        else:
            if largest_prob == prob0 and prob1 < this_obs:
                return 0
            elif largest_prob == prob1 and prob0 < this_obs:
                return 1
            
def singleton_qubit(complex0, complex1):
    if int(round(abs(complex0)**2 + abs(complex1)**2, 0)) != 1: # Binary event outcomes must total 1
            raise Exception(f"src/main.py :: Invalid singleton qubit parameters {complex0} & {complex1}")
    return qubit(complex0, complex1)

"""
The qubit is in a superposition of beind measured as 0 or 1 before the measurement
I know it sounds redundand but that is the fundamental assumption of quantum mechanics.
You can simulate binary event outcomes quite well with a single qubit given you know the
Probability of each outcome in such binary event. There are also models of higher order quantum
logits lik Qutrits (think of Qutrits to Qubits as ternary is to binary)
"""
N_ITERS = 10000

if __name__ == "__main__":
    q = singleton_qubit(complex(-1/math.sqrt(2), 0), complex(0, 1/math.sqrt(2))) # coinflip scenario
    nZeros = 0
    nOnes = 0
    for i in range(0, N_ITERS): # Simulate 50/50 events
        measurement = q.measure()
        #print(f"50/50 Measurement Iteration {i} :: {measurement}")
        if measurement == 0:
            nZeros += 1
        else:
            nOnes += 1
    print(f"50/50 Test Result ({N_ITERS} iters) :: {nZeros} 0's  {nOnes} 1's")
    
    # 2/3 (66.66%) chance of measuring Zero vs 1/3 (33.33%) chance of One
    q = singleton_qubit(complex(-2/math.sqrt(6), 0), complex(0, math.sqrt(1)/math.sqrt(3)))
    nZeros = 0
    nOnes = 0
    for i in range(0, N_ITERS): # Simulate 66.66% vs 33.335% events
        measurement = q.measure()
        #print(f"66.66% vs 33.335% Measurement Iteration {i} :: {measurement}")
        if measurement == 0:
            nZeros += 1
        else:
            nOnes += 1
    print(f"66.66% vs 33.335% Test Result ({N_ITERS} iters) :: {nZeros} 0's {nOnes} 1's")