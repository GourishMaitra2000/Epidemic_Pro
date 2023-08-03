import EoN
 import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt
import random
N = 5000
G = nx.fast_gnp_random_graph(N, 6./(N-1))
#We have defined our network ( which is a random graph) with N number o
f nodes
#5 is the number that decides how densely the nodes are connected
#We show how node and edge attributes in the contact network 'G' can be
 used
#to scale the transmission rates.
#Let us define H for the spotaneous transitions
H = nx.DiGraph()
H.add_node('S')
#
H.add_edge('I', 'R', rate = 0.5)
H.add_edge('I', 'C', rate = 0.5)
H.add_edge('C', 'R', rate = 0.25)
H.add_edge('E', 'I', rate = 0.65)
#  The line above states that the I to 'R' transition occurs with rate
0.5
#
#Let us define J for the induced transitions
#
J = nx.DiGraph()
J.add_edge(('I', 'S'), ('I', 'I'), rate = 0.6)
J.add_edge(('E', 'S'), ('E', 'E'), rate = 0.35)
#  The line above states that an 'I' individual will cause an 'S' indiv
idual
#  to transition to 'I' with rate equal to 0.6
#Defining initial conditions
IC = defaultdict(lambda: 'S')
for node in range(10):
 IC[node] = 'I'
for node in range(40):
 IC[node] = 'E'
return_statuses = ('S','E','I','C','R')
t, S,E, I,C, R = EoN.Gillespie_simple_contagion(G, H, J, IC, return_sta
tuses,tmax = float('Inf'))
plt.plot(t, S, label = 'Susceptible')
plt.plot(t, E, label = 'Exposed')
plt.plot(t, I, label = 'Infected')
plt.plot(t, C, label = 'Chronical')
plt.plot(t, R, label = 'Recovered')
plt.legend()
 
plt.savefig('SEICR.png')