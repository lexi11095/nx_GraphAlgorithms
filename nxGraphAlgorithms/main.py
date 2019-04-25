import networkx as nx
from itertools import combinations
from functions.bool_functions import *
from functions.global_properties import degree_sequence
from functions.Havel_Hakimi import *
from matching import *

G = nx.read_edgelist('sample_graphs/sample_G.txt')
nx.draw_networkx(G)
D = degree_sequence(G)

print(is_matching(G))

