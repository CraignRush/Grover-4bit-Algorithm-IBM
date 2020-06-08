#initialization
import matplotlib.pyplot as plt
import numpy as np
from dsutil.plotting import add_value_labels
# Import math Library
import math 
#matplotlib inline
#config InlineBackend.figure_format = 'svg' # Makes the images look nice
# importing Qiskit
from qiskit import IBMQ, Aer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
# import basic plot tools
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor

provider = IBMQ.load_account()

SIM_REAL = True
SIM_COMP = True
PLOT = True
ELAB = False
SHOW_PLOT = False
DRAW_CIRCUIT = True
RANGE = 1

n = 4
shots = 8192

for i in range(5,6,RANGE):
    print('Iteration: ' + str(i))
    gc = QuantumCircuit(n)
    gc.h(0)
    gc.h(1)
    gc.h(2)
    gc.h(3)   
    for qubit in range(i+1):   
        if ELAB:
            gc.x(1)
            gc.x(3)
            gc.barrier()

            gc.h(1)
            gc.cx(2,1)
            gc.tdg(1)
            gc.cx(3,1)

            gc.t(1)
            gc.cx(2,1)
            gc.tdg(1)
            gc.cx(3,1)
            gc.barrier()
            gc.t(1)
            gc.tdg(2)
            gc.h(3)
            gc.h(1)
            gc.h(2)
            gc.cx(1,0)
            gc.barrier()
            gc.cx(2,3)
            gc.barrier()
            gc.t(0)
            gc.h(2)
            gc.h(3)
            gc.cx(1,0)
            gc.barrier()
            gc.tdg(2)
            gc.h(3)
            gc.tdg(0)
            gc.tdg(1)
            gc.barrier()
            gc.h(2)
            gc.h(1)
            gc.cx(2,3)
            gc.h(2)
            gc.h(3)
            gc.s(2)
            gc.t(3)
            gc.cx(2,1)
            gc.barrier()
            gc.tdg(1)
            gc.cx(3,1)
            gc.barrier()
            gc.t(1)
            gc.cx(2,1)
            gc.barrier()
            gc.tdg(1)
            gc.cx(3,1)
            gc.barrier()
            gc.t(1)
            gc.tdg(2)
            gc.h(3)
            gc.h(1)
            gc.h(2)
            gc.cx(1,0)
            gc.barrier()
            gc.cx(2,3)
            gc.barrier()
            gc.tdg(0)
            gc.h(2)
            gc.h(3)
            gc.cx(1,0)
            gc.tdg(2)
            gc.h(3)
            gc.t(0)
            gc.t(1)
            gc.h(2)
            gc.cx(1,0)
            gc.cx(2,3)
            gc.h(0)
            gc.h(1)
            gc.h(2)
            gc.h(3)
            gc.cx(1,0)
            gc.s(2)
            gc.t(3)
            gc.h(0)
            gc.h(1)
            gc.h(2)
            gc.h(3)
            gc.cx(1,0)
            gc.cx(2,3)
            gc.h(2)
            gc.h(3)
            gc.cx(2,1)
            gc.h(3)
            gc.u1(math.pi/8,1)
            gc.cx(2,1)
            gc.u1(-math.pi/8,1)
            gc.u1(-math.pi/8,2)
            gc.h(2)
            gc.cx(2,3)
            gc.h(2)
            gc.h(3)
            gc.cx(2,1)
            gc.u1(-math.pi/8,1)
            gc.cx(2,1)
            gc.u1(math.pi/8,1)
            gc.u1(math.pi/8,2)
            gc.cx(3,1)
            gc.u1(-math.pi/8,1)
            gc.cx(3,1)
            gc.u1(math.pi/8,1)
            gc.u1(math.pi/8,3)
            gc.cx(1,0)
            gc.h(0)
            gc.h(1)
            gc.cx(1,0)
            gc.h(0)
            gc.h(1)
            gc.cx(1,0)
            gc.barrier()
            gc.x(1)
            gc.x(3)
            gc.barrier()
            gc.h(0)
            gc.h(1)
            gc.h(2)
            gc.h(3)
            gc.x(0)
            gc.x(1)
            gc.x(2)
            gc.x(3)
            gc.barrier()
            gc.h(1)
            gc.cx(2,1)
            gc.tdg(1)
            gc.cx(3,1)
            gc.t(1)
            gc.cx(2,1)
            gc.tdg(1)
            gc.cx(3,1)
            gc.t(1)
            gc.tdg(2)
            gc.h(3)
            gc.h(1)
            gc.h(2)
            gc.cx(1,0)
            gc.cx(2,3)
            gc.t(0)
            gc.h(2)
            gc.h(3)
            gc.cx(1,0)
            gc.tdg(2)
            gc.h(3)
            gc.tdg(0)
            gc.tdg(1)
            gc.h(2)
            gc.h(1)
            gc.cx(2,3)
            gc.h(2)
            gc.h(3)
            gc.s(2)
            gc.t(3)
            gc.cx(2,1)
            gc.tdg(1)
            gc.cx(3,1)
            gc.t(1)
            gc.cx(2,1)
            gc.tdg(1)
            gc.cx(3,1)
            gc.t(1)
            gc.tdg(2)
            gc.h(3)
            gc.h(1)
            gc.h(2)
            gc.cx(1,0)
            gc.cx(2,3)
            gc.tdg(0)
            gc.h(2)
            gc.h(3)
            gc.cx(1,0)
            gc.tdg(2)
            gc.h(3)
            gc.t(0)
            gc.t(1)
            gc.h(2)
            gc.cx(1,0)
            gc.cx(2,3)
            gc.h(0)
            gc.h(1)
            gc.h(2)
            gc.h(3)
            gc.cx(1,0)
            gc.s(2)
            gc.t(3)
            gc.h(0)
            gc.h(1)
            gc.h(2)
            gc.h(3)
            gc.cx(1,0)
            gc.cx(2,3)
            gc.h(2)
            gc.h(3)
            gc.cx(2,1)
            gc.h(3)
            gc.u1(math.pi/8,1)
            gc.cx(2,1)
            gc.u1(-math.pi/8,1)
            gc.u1(-math.pi/8,2)
            gc.h(2)
            gc.cx(2,3)
            gc.h(2)
            gc.h(3)
            gc.cx(2,1)
            gc.u1(-math.pi/8,1)
            gc.cx(2,1)
            gc.u1(math.pi/8,1)
            gc.u1(math.pi/8,2)
            gc.cx(3,1)
            gc.u1(-math.pi/8,1)
            gc.cx(3,1)
            gc.u1(math.pi/8,1)
            gc.u1(math.pi/8,3)
            gc.cx(1,0)
            gc.h(0)
            gc.h(1)
            gc.cx(1,0)
            gc.h(0)
            gc.h(1)
            gc.cx(1,0)
            gc.barrier()
            gc.x(0)
            gc.x(1)
            gc.x(2)
            gc.x(3)
            gc.h(0)
            gc.h(1)
            gc.h(2)
            gc.h(3)
        else:
            # Select 0101            
            gc.x(1)
            gc.x(3)

            gc.barrier()

            gc.ccx(3,2,1)
            
            #CZ -1/2
            gc.cu1(-math.pi/2,1,0)   

            gc.ccx(3,2,1)

            #CZ 1/2
            gc.cu1(math.pi/2,1,0)   

            gc.cx(3,2)

            #CZ -1/4 
            gc.cu1(-math.pi/4,2,0)   

            gc.cx(3,2)

            #CZ 1/4            
            gc.cu1(math.pi/4,2,0) 
            
            #CZ 1/4            
            gc.cu1(math.pi/4,3,0) 

            # Select 0101 
            gc.barrier()           
            gc.x(1)
            gc.x(3)
            gc.barrier()  

            # Initalize
            gc.h(0)
            gc.h(1)
            gc.h(2)
            gc.h(3)
            
            gc.x(0)
            gc.x(1)
            gc.x(2)
            gc.x(3)

            # Rotation
            gc.ccx(3,2,1)
            
            #CZ -1/2
            gc.cu1(-math.pi/2,1,0)   

            gc.ccx(3,2,1)

            #CZ 1/2
            gc.cu1(math.pi/2,1,0)   

            gc.cx(3,2)

            #CZ -1/4 
            gc.cu1(-math.pi/4,2,0)   

            gc.cx(3,2)

            #CZ 1/4            
            gc.cu1(math.pi/4,2,0) 
            
            #CZ 1/4            
            gc.cu1(math.pi/4,3,0) 

            # Finalize   
            gc.barrier()    
            gc.x(0)
            gc.x(1)
            gc.x(2)
            gc.x(3)

            gc.h(0)
            gc.h(1)
            gc.h(2)
            gc.h(3)

    gc.measure_all()

    styledict = {
        'fontsize': 13,
        'subfontsize': 9,
        'dpi': 1000,
        'margin': [0,0,0,0]
    }

    if DRAW_CIRCUIT:
        gc.draw('mpl',0.7,'C:/Users/Familie/Documents/QuantumComputers/Grover4_0101/grover_circuit_4qubits_'+ str(i) +'it_paper_0101.png',styledict)


    if SIM_REAL:
        # Load IBM Q account and get the least busy backend device
        real_device = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= 3 and 
                                           not x.configuration().simulator and x.status().operational==True))
        print("Running on current least busy device: ", real_device)
        job = execute(gc, backend=real_device, shots=shots, optimization_level=3)
        job_monitor(job, interval = 2)
        # Get the results from the real computation
        results = job.result()
        answer_real = results.get_counts(gc)

    if SIM_COMP:
        # Get the results from the simulation
        sim_device = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= 3 and 
                                          x.configuration().simulator and x.status().operational==True))
        print("Running on current least busy device: ", sim_device)
        job = execute(gc, backend=sim_device, shots=shots, optimization_level=3)
        job_monitor(job, interval = 2)
        results = job.result()
        answer_sim = results.get_counts()


    if (SIM_COMP and SIM_REAL) or PLOT: 
        fig, ax = plt.subplots(1, 2, False, True, figsize=(12,6.75))
        plot_histogram(answer_real,(6,3),None,None,'asc',None,None,None,None,ax[0])
        plot_histogram(answer_sim,(6,3),None,None,'asc',None,None,None,None,ax[1])
        ax[0].set_title('Real Execution \n on ' + real_device.name())
        ax[1].set_title('Simulated Execution \n on ' + sim_device.name())
        add_value_labels(ax=ax[0],format='{:.2f}',rotation=60)
        add_value_labels(ax=ax[1],format='{:.2f}',rotation=60)
        for tick in ax[0].get_xticklabels():
            tick.set_fontsize(13)
        for tick in ax[1].get_xticklabels():
            tick.set_fontsize(13)
        plt.tight_layout()
        plt.gcf().savefig('C:/Users/Familie/Documents/QuantumComputers/Grover4_0101/grover_circuit_4qubits_'+ str(i) + 'it_' + str(shots) + 'shots_0101.pdf')        
        plt.gcf().savefig('C:/Users/Familie/Documents/QuantumComputers/Grover4_0101/grover_circuit_4qubits_'+ str(i) + 'it_' + str(shots) + 'shots_0101.eps')      
        if SHOW_PLOT:
            plt.show()
