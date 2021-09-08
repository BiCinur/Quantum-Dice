import matplotlib.pyplot as plt

from pyquil import Program, get_qc
from pyquil.api import WavefunctionSimulator
from pyquil.gates import *

import numpy as np
import itertools

def quantum_dice(n):
    '''
    :param n: number of qubits
    :return: Program preparing quantum dice
    '''
    p = Program()
    for q in range(n):
        p += Program(H(q))
    return p

n = 3  # since 2^3 = 8
p = quantum_dice(n)

wfn_sim = WavefunctionSimulator()
wfn = wfn_sim.wavefunction(p)
outcome_probs = wfn.get_outcome_probs()

# testing for correctness of program
np.testing.assert_allclose(list(outcome_probs.values()), np.tile(1/(2**n), 2**n))
print("Quantum Dice implementation correct!")

# Plotting probabilities according to the resultant wavefunction
plt.figure(figsize=(8, 6))
plt.bar(outcome_probs.keys(), outcome_probs.values())
plt.show()



# specify the number of trials/shots
n_shots = 1000


# plot frequency bars
d_counts = {''.join(q): np.sum(np.all(results_stack == np.array([int(s) for s in q]), axis=-1))
            for q in itertools.product(['0', '1'], repeat=n)}

plt.figure(figsize=(8, 6))
plt.bar(d_counts.keys(), d_counts.values())
plt.show()
