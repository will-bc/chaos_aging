import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import teneto
import conversion_equation
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
from pyvis.network import Network
import pandas as pd

# Corrigir visualização usando pyvis


#Data loading 
gene= ['BLC2']
rna=['miRNA1']
protein=[]
effect=['Myogenesis','Oxidative Stress','Apoptosis', 'Limit Point']
tissue={
    0:['heart',''],
    1:['penis','']}
local= []   
drug = []

    
#nodes universal defaults456
node_colors = {0: 'red', #gene
               1: 'orange', #rna
               2: 'yellow', #protein
               3: 'green', #effect
               4: 'yellow', #tissue
               5: 'aqua', #local
               6: 'black'} #drug

#edges universal defaults
styles_produc= "-|>, head_length=0.4, head_width=0.2"
styles_coproduc= ["<->"] 
styles_inib= ["|-|, widthA=0, angleA=0, widthB=1.0, angleB=0",'r']
styles_coinib= ["|-|", 'r']


#Control construct ---------------------------------------
tissue[1][1] = nx.DiGraph()


#------------------

#Graph point construct (aging heart) ----------------------------

#data edges

edges_info={gene[0]:[effect[2]],
            rna[0] :[gene[0]],
            effect[1]:[rna[0]],
            effect[2]:[effect[3]]}


tissue[0][1] = nx.DiGraph()



#nodes creation


##src = gene[0]
##dst = rna[0]
##w = 1
##
##tissue[0][1].add_node(src, title=src)
##tissue[0][1].add_node(dst, title=dst)
##tissue[0][1].add_edge(src, dst, value=w)



 #automation nodes creation

for i in range list(edges_info.items()):
    
    tissue[0][1].add_nodes_from(list(edges_info.items())[i])

    

 
#edges settings in aging momentum
##aging_edges_configuration= [(rna[0],gene[0]),(gene[0],effect[0])]
##tissue[0][1].add_edges_from(aging_edges_configuration)


#reactions

##C1, C2 = conversion_equation.c_e(1.0,1.0,0.1,-0.05,2,1)
##print(C1)
##print(C2)
##
##edge_widths = {0:C1[1], 1:C2[1]} #equations results





#Draws construct edges


##pos = nx.spring_layout(tissue[0][1])
##
##
##start_pos = pos[rna[0]]
##end_pos = pos[gene[0]]
##
##arrow = FancyArrowPatch(start_pos, end_pos, arrowstyle='|-|, widthA=0, angleA=0, widthB=1.0, angleB=0', color='red', mutation_scale=20)
##plt.gca().add_patch(arrow)


##nx.draw_networkx_edges(tissue[0][1], pos, edgelist=tissue[0][1].edges([rna[0],gene[0]]),
##                       edge_color=styles_inib[1], arrows=True, width=edge_widths[0],
##                       arrowstyle=(styles_inib[0]))


##start_pos = pos[gene[0]]
##end_pos = pos[effect[0]]
##
##arrow = FancyArrowPatch(start_pos, end_pos, arrowstyle='->', color='blue', mutation_scale=20)
##plt.gca().add_patch(arrow)


##nx.draw_networkx_edges(tissue[0][1], pos, edgelist=tissue[0][1].edges([gene[0],effect[0]]),
##                       edge_color='blue', arrows=True, width=edge_widths[1],
##                       arrowstyle=(styles_produc))


# Draws construct nodes

nt = Network(height="750px", width="100%", directed=True, bgcolor="#222222", font_color="white", notebook=True, cdn_resources='remote')
nt.from_nx(tissue[0][1])
nt.show('nx.html')

##
##
##try:
##    nx.draw_networkx_nodes(tissue[0][1], pos,
##                       nodelist=[gene[i] for i in range(0,len(gene))], node_color=(node_colors[0]))
##except Exception as e:
##        pass
##try:    
##    nx.draw_networkx_nodes(tissue[0][1], pos,
##                       nodelist=[rna[i] for i in range(0,len(rna))], node_color=(node_colors[1]))
##except Exception as e:
##        pass
##
##try:
##    nx.draw_networkx_nodes(tissue[0][1], pos,
##                       nodelist=[protein[i] for i in range(0,len(protein))], node_color=(node_colors[2]))
##except Exception as e:
##        pass
##
##try:    
##    nx.draw_networkx_nodes(tissue[0][1], pos,
##                       nodelist=[effect[i] for i in range(0,len(effect))], node_color=(node_colors[3]))
##except Exception as e:
##        pass
##
##    
##nx.draw_networkx_labels(tissue[0][1], pos, font_size=9, font_family='Arial')
##
##plt.axis('off')
##plt.show() 
