import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import teneto
import conversion_equation
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
from pyvis.network import Network
import pandas as pd



gene= ['BLC2']
rna=['miRNA1']
protein=[]
effect=['Myogenesis','Oxidative Stress','Apoptosis', 'Limit Point']
tissue={
    0:['heart',''],
    1:['penis','']}
local= []   
drug = []

edges_info={gene[0]:[effect[2]],
            rna[0] :[gene[0]],
            effect[1]:[rna[0]],
            effect[2]:[effect[3]]}

x= []


for key, value in edges_info.items():
    x.append((key, value))

    

print(x)
