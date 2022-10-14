import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymc3 as pm
import arviz as az

if __name__=='__main__':
    model = pm.Model()

    with model:
        cutremur=pm.Bernoulli('C',0.0005)
        incendiu=pm.Bernoulli('I',0.01)
        declans=pm.Bernoulli('D',pm.math.switch(incendiu, pm.math.switch(incendiu, 0.95, 0.0005), pm.math.switch(cutremur, 0.98, 00.1)))
        declans_acc=pm.Bernoulli('D_a',pm.math.switch(incendiu, pm.math.switch(incendiu, 0.0001, 0.0005), pm.math.switch(cutremur, 0.02, 00.1)))
        trace = pm.sample(20000)

    dictionary = {
                'cutremur': trace['C'].tolist(),
                'incendiu': trace['I'].tolist(),
                'declansare': trace['D'].tolist(),
                'declansare_accidentala': trace['D_a'].tolist()
                }
    ##Ex2
    df = pd.DataFrame(dictionary)
    decl = df[((df['cutremur'] == 1) & (df['declansare'] == 1))].shape[0] / df[df['declansare'] == 1].shape[0]
    print(decl)
    ##EX3
    decl = df[((df['incendiu'] == 1) & (df['declansare'] == 0))].shape[0] / df[df['declansare'] == 0].shape[0]
    print(decl)