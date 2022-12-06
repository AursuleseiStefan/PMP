import pandas as pd
import numpy as np
import pymc3 as pm
minim_statii=1
minim_case=1
minim_mese=1
for i in range(10):
    model = pm.Model()
    with model:
        nr_clienti = pm.Poisson('N', mu=20)
        t_casa = pm.Normal('T_c', mu=1, sd=0.5, shape=50)
        t_gatit = pm.Exponential('T_g', lam=2, shape=50)
        t_masa=pm.TruncatedNormal('T_m', mu=10, sd=2, lower=0)
        idx = np.arange(50)
        timp = pm.math.switch(nr_clienti>idx, t_casa[idx]+t_gatit[idx], 0)
        succes = pm.Deterministic('S', pm.math.prod(pm.math.switch(timp<15,1,0)))
        succese2 = pm.Deterministic('S', pm.math.prod(pm.math.switch(timp>0,1,0)))
        trace = pm.sample(10000)
    succese = trace['S']
    prob1 = len(succese[(succese == 1)]) / len(succese)
    prob2 = len(succese2[(succese2 == 1)]) / len(succese2)
    if prob1<0.95:                   
        minim_case = minim_case + 1
        minim_statii+=1
    if prob2<0.90:
        minim_mese+=1
