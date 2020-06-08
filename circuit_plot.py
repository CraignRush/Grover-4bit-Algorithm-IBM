#initialization
import matplotlib.pyplot as plt
import numpy as np
#matplotlib inline
#config InlineBackend.figure_format = 'svg' # Makes the images look nice

# importing Qiskit
from qiskit import IBMQ, Aer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.circuit.library.standard_gates import ZGate, HGate

# import basic plot tools
from qiskit.visualization import plot_histogram
n = 4

grover_circuit = QuantumCircuit(n)

for qubit in range(n):
    grover_circuit.h(qubit)
    
grover_circuit.barrier()
grover_circuit.x(1)
grover_circuit.x(3)

c3z_gate = ZGate().control(3)

grover_circuit.append(c3z_gate, [3, 2, 1, 0])

grover_circuit.x(1)
grover_circuit.x(3)
grover_circuit.barrier()
for qubit in range(n):
    grover_circuit.h(qubit)
    
grover_circuit.draw('mpl',1,'C:/Users/Familie/Documents/QuantumComputers/grover_circuit_4qubits_oracle_0101.png')
plt.show(grover_circuit)



for qubit in range(n):
    grover_circuit.x(qubit)
grover_circuit.append(c3z_gate, [3, 2, 1, 0])    

for qubit in range(n):
    grover_circuit.x(qubit)
    grover_circuit.h(qubit) 
grover_circuit.measure_all()
grover_circuit.draw('mpl',1,'C:/Users/Familie/Documents/QuantumComputers/grover_circuit_4qubits_full_0101.png')
plt.show(grover_circuit)