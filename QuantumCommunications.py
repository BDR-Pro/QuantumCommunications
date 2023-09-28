from qiskit import qasm3 
from qiskit import *
import qiskit as q
from qiskit import QuantumRegister
from qiskit.quantum_info import random_statevector
import random

qc=QuantumCircuit(10,10) 
alice_bits = [random.randint(0, 1) for _ in range(10)]
alice_gates = [random.randint(0, 1) for _ in range(10)]
bobrandomZorX = [random.randint(0, 1) for _ in range(10)]

for index,i in enumerate(alice_bits):
    if i == 1:
        qc.x(index)
    else:
        qc.i(index)


qc.barrier()


for index,i in enumerate(alice_gates):
    if i == 1:
        qc.h(index)
    else:
        qc.i(index)

qc.barrier()

for index,i in enumerate(bobrandomZorX):
    if i == 1:
        qc.h(index)
    else:
        qc.i(index)


qc.barrier()

qc.measure(range(10), range(10))

qc.barrier()


sharedKey = []




for index,i in enumerate(alice_gates):
    if i == bobrandomZorX[index]:
        sharedKey.append(index)
        

        
job = q.execute(qc, backend=q.Aer.get_backend('qasm_simulator'), shots=1)
    
counts = job.result().get_counts()

a=list(counts.keys())

rev = a[0][::-1]


print(rev)


print(alice_gates)
print(bobrandomZorX)
print(sharedKey)
sharedkeylist_=[]
for i in (sharedKey):
    sharedkeylist_.append(rev[i])
    
print(sharedkeylist_)
qc.draw(output='mpl')