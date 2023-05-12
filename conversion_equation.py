import numpy as np
import matplotlib.pyplot as plt

#corrigir var_time

def c_e(C1_0,C2_0,k1,k2): 
    """

    Definitions:

    C = Concetrations of agents in reactiion
    
    k = rate of converion (its needed to calculate for your own [yet]) 

    if production the value is POSITIVE (+) if its inhibition the value is
    NEGATIVE (-)

    n_analyzes = How many times was data collection about agent behaviour

    var_time= what was the time periods of data collection
    IMPORTANT: var_time = delta_t 

    """

    ##Future improvements
    #
    # k calculation is necessary to automate
    #
    #-----------------------------------------

    

    ## Time setting

    n_analyzes=1
    delta_t= 0.1
    t = np.arange(0, n_analyzes, delta_t) # Time Array



    # Arrays for C1 and C2
    C1 = np.zeros_like(t)
    C2 = np.zeros_like(t)


    # Inicial condition
    C1[0] = C1_0
    C2[0] = C2_0

    #-----------------------------------------------



    # Functions of concentrations derivatives
    def dC1dt(C1, C2, k1):
        return k1 * C1 * C2

    def dC2dt(C1, C2, k2):
        return k2 * C1 * C2





    # calculating for each time (the magic of derivative)
    for i in range(1, len(t)):
        dC1 = dC1dt(C1[i-1], C2[i-1], k1) * delta_t
        dC2 = dC2dt(C1[i-1], C2[i-1], k2) * delta_t
        C1[i] = C1[i-1] + dC1
        C2[i] = C2[i-1] + dC2


    return C1, C2

    

### For Plot information about concentration behavior

def plot_concentrations(C1,C2,name1,name2):

    """

    name1= string, agent name 1
    name2= string, agent name 2
    

    """
    n_analyzes=1
    delta_t= 0.1
    t = np.arange(0, n_analyzes, delta_t)
 
    plt.plot(t, C1, label=name1)
    plt.plot(t, C2, label=name2)
    plt.xlabel('Time')
    plt.ylabel('concentration')
    plt.legend()
    plt.show()
