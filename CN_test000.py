#Tentar replicar:
#
#https://www.youtube.com/watch?v=V5MU658qOPM&list=PL2VXyKi-KpYu7djT-8bDxtylvxznz3WLR&index=1
# https://networkx.org/documentation/stable/auto_examples/drawing/plot_directed.html#sphx-glr-auto-examples-drawing-plot-directed-py
#

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import teneto
import conversion_equation
import matplotlib as mpl
from pyvis.network import Network
import json
import pandas as pd



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

    
#nodes universal defaults
node_colors = {0: '#722f37', #gene
               1: 'orange', #rna
               2: 'yellow', #protein
               3: '#008080', #effect
               4: 'yellow', #tissue
               5: 'aqua', #local
               6: 'Purple', #drug
               7: 'black'} #limit_point


#edges universal defaults
styles_produc= "-|>, head_length=0.4, head_width=0.2"
styles_coproduc= ["<->"] 
styles_inib= ["|-|, widthA=0, angleA=0, widthB=1.0, angleB=0",'r']
styles_coinib= ["|-|", 'r']


#Control construct ---------------------------------------
tissue[0][1] = nx.DiGraph()
tissue[1][1] = nx.DiGraph()


#------------------

#GRAPH POINT CONSTRUCT aging heart) ----------------------------


tissue[0].append(nx.DiGraph())

##Automation nodes creation

tissue[0][1].add_nodes_from(gene+rna+effect)


##Data edges


edges_info_p={effect[1]:[rna[0]],   #production
            effect[2]:[effect[3]]}

edges_info_i= {gene[0]:[effect[2]],  #inhibition
            rna[0] :[gene[0]]}


 
##Edges settings in aging momentum


               #Promoters agents (production)
k_p=[]    
v_p=[]


for key in edges_info_p.keys():
    k_p.append(key)
    value = edges_info_p[key][0]
    v_p.append(value)
    


for i in range(len(k_p)):
    aging_edges_configuration= [(k_p[i],v_p[i])]
    tissue[0][2].add_edges_from(aging_edges_configuration)


               #Inhibitors agents (inhibition)
k_i=[]    
v_i=[]


for key in edges_info_i.keys():
    k_i.append(key)
    value = edges_info_i[key][0]
    v_i.append(value)
    


for i in range(len(k_p)):
    aging_edges_configuration= [(k_i[i],v_i[i])]
    tissue[0][2].add_edges_from(aging_edges_configuration)





    




#reactions

##C1, C2= conversion_equation.c_e(1.0,1.0,0.1,0.5)
##print(C1)
##print(C2)
##
##edge_widths = {0:C1[1], 1:C2[1]} #equations results
##conversion_equation.plot_concentrations(C1,C2,'X','Y')


#Draw

##pos = nx.spring_layout(tissue[0][2])

##Nodes




#Production



##try:
##    nx.draw_networkx_nodes(tissue[0][2], pos,
##                       nodelist=[gene[i] for i in range(0,len(gene))], node_color=(node_colors[0]))
##except Exception as e:
##        pass
##try:    
##    nx.draw_networkx_nodes(tissue[0][2], pos,
##                       nodelist=[rna[i] for i in range(0,len(rna))], node_color=(node_colors[1]))
##except Exception as e:
##        pass
##
##try:
##    nx.draw_networkx_nodes(tissue[0][2], pos,
##                       nodelist=[protein[i] for i in range(0,len(protein))], node_color=(node_colors[2]))
##except Exception as e:
##        pass
##
##try:    
##    nx.draw_networkx_nodes(tissue[0][2], pos,
##                       nodelist=[effect[i] for i in range(0,len(effect))], node_color=(node_colors[3]))
##except Exception as e:
##        pass





#Draws construct edges





##for p in range(len(k_p)):
##
##    if k_p[p] in gene:
##
##        edges= nx.draw_networkx_edges(
##            tissue[0][2],
##            pos,
##            edgelist=tissue[0][2].edges([k_p[p],v_p[p]]),
##            edge_color='g',
##            arrowstyle="->")
##
##
##
##for i in range(len(k_i)):
##
##    if k_i[i] in gene:
##
##        edges= nx.draw_networkx_edges(
##            tissue[0][2],
##            pos,
##            edgelist=tissue[0][2].edges([k_i[i],v_i[i]]),
##            edge_color='r',
##            arrowstyle=(styles_inib[0]))







#Nodes Draws 

all_nodes=list(set((k_p+k_i+v_p+v_i))) #concatenating and removing repeated elements


for i in range(0,len(all_nodes)):
    
    
    if all_nodes[i] in gene:
        
        tissue[0][2].add_node(all_nodes[i],title=all_nodes[i], color=node_colors[0])
        
    elif all_nodes[i] in rna:
        
        tissue[0][2].add_node(all_nodes[i],title=all_nodes[i], color=node_colors[1])
    
    elif all_nodes[i] in protein:
    
        tissue[0][2].add_node(all_nodes[i],title=all_nodes[i], color=node_colors[2])
        
    elif all_nodes[i] in effect:
    
        tissue[0][2].add_node(all_nodes[i],title=all_nodes[i], color=node_colors[3])

#Edge Draws

#Inhibitors

for i in range(0,len(k_i)):

    tissue[0][2].add_edge(k_i[i], v_i[i], color= 'red')

#Promoters

for p in range(0,len(k_p)):

    tissue[0][2].add_edge(k_p[p], v_p[p], color= 'green')


# create a legend object



    

nt = Network(height="750px", width="100%", directed=True, bgcolor="#222222", font_color="white", notebook=True, cdn_resources='remote')
##nt.barnes_hut() physics



nt.from_nx(tissue[0][2])
nt.show('nx.html')



