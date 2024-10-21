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
        total_prob = prob0 + prob1
        if round(total_prob, 0) != 1.0:
            raise ValueError(f"src/main.py Qubit outcome probabilities do not sum to 1: {total_prob}")
        largest_prob = max(prob0, prob1)
        if prob0 == prob1: # Coinflip scenario
            return int(round(this_obs, 0))
        else: # Otherwise return the result that matches this observation
            if largest_prob == prob0 and prob1 < this_obs:
                return 0
            elif largest_prob == prob1 and prob0 < this_obs:
                return 1
            
def singleton_qubit(complex0, complex1):
    if int(round(abs(complex0)**2 + abs(complex1)**2, 0)) != 1: # Binary event outcomes must total 1
            raise Exception(f"src/main.py :: Invalid singleton qubit parameters {complex0} & {complex1}")
    return qubit(complex0, complex1)

"""
The qubit is in a superposition of being measured as 0 or 1 before the measurement
occurs and collapses the superposition.

I know it sounds redundant but that is the fundamental assumption of quantum mechanics.

The driving idea behind quantum computers and quantum registers is that
you can simulate a chain of binary event outcomes quite well with a set of superimposed qubits
given you know the probability of each outcome in each encoded binary event. There are also models of higher order quantum
logits like Qutrits (think of Qutrits to Qubits as ternary is to binary); given that not all events in nature are binary events.
"""

class qutrit:
    def __init__(self, c0, c1, c2):
        self.c0 = c0
        self.c1 = c1
        self.c2 = c2

    def measure(self):
        this_obs = get_true_pyrand()
        prob0 = abs(self.c0)**2
        prob1 = abs(self.c1)**2
        prob2 = abs(self.c2)**2
        total_prob = prob0 + prob1 + prob2
        if round(total_prob, 0) != 1.0:
            raise ValueError(f"src/main.py Qutrit outcome probabilities do not sum to 1: {total_prob}")
        # Cumulative probability intervals
        if this_obs < prob0:
            return 0
        elif this_obs < prob0 + prob1:
            return 1
        else:
            return 2

def singleton_qutrit(complex0, complex1, complex2):
    if int(round(abs(complex0)**2 + abs(complex1)**2 + abs(complex2)**2, 0)) != 1:
        raise Exception(f"src/main.py :: Invalid singleton qubtrit parameters {complex0} , {complex1} , {complex2}")
    return qutrit(complex0, complex1, complex2)


N_ITERS = 10000

if __name__ == "__main__":
    # Qubit coinflip example
    qb = singleton_qubit(complex(-1/math.sqrt(2), 0), complex(0, 1/math.sqrt(2))) # coinflip scenario
    nZeros = 0
    nOnes = 0
    for i in range(0, N_ITERS): # Simulate 50/50 events
        measurement = qb.measure()
        #print(f"50/50 Measurement Iteration {i} :: {measurement}")
        if measurement == 0:
            nZeros += 1
        else:
            nOnes += 1
    print(f"50/50 Test Result ({N_ITERS} iters) :: {nZeros} 0's  {nOnes} 1's")

    # Qubit example with 2/3 (66.66%) chance of measuring Zero vs 1/3 (33.33%) chance of One
    qb = singleton_qubit(complex(-2/math.sqrt(6), 0), complex(0, math.sqrt(1)/math.sqrt(3)))
    nZeros = 0
    nOnes = 0
    for i in range(0, N_ITERS): # Simulate 66.66% vs 33.335% events
        measurement = qb.measure()
        #print(f"66.66% vs 33.335% Measurement Iteration {i} :: {measurement}")
        if measurement == 0:
            nZeros += 1
        else:
            nOnes += 1
    print(f"66.66% vs 33.335% Test Result ({N_ITERS} iters) :: {nZeros} 0's {nOnes} 1's")

    # Example qutrit in a "coinflip" scenario (equal chance for 0, 1, and 2)
    qt = singleton_qutrit(complex(1/math.sqrt(3), 0), complex(1/math.sqrt(3), 0), complex(1/math.sqrt(3), 0))
    nZeros = 0
    nOnes = 0
    nTwos = 0
    for i in range(N_ITERS):
        measurement = qt.measure()
        if measurement == 0:
            nZeros += 1
        elif measurement == 1:
            nOnes += 1
        else:
            nTwos += 1
    print(f"Equal Probabilities Test Result ({N_ITERS} iters) :: {nZeros} 0's, {nOnes} 1's, {nTwos} 2's")

    # Qutrit example with non-equal probabilities (60% for 0, 30% for 1, 10% for 2)
    qt = singleton_qutrit(complex(math.sqrt(0.6), 0), complex(math.sqrt(0.3), 0), complex(math.sqrt(0.1), 0))
    nZeros = 0
    nOnes = 0
    nTwos = 0
    for i in range(N_ITERS):
        measurement = qt.measure()
        if measurement == 0:
            nZeros += 1
        elif measurement == 1:
            nOnes += 1
        else:
            nTwos += 1
    print(f"60%/30%/10% Test Result ({N_ITERS} iters) :: {nZeros} 0's, {nOnes} 1's, {nTwos} 2's")