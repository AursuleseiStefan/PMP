import pymc3 as pm
import numpy as np
import pandas as pd
import theano.tensor as tt
#import seaborn as sns
import scipy.stats as stats
from scipy.special import expit as logistic
import matplotlib.pyplot as plt
import arviz as az
import pandas as pd





if __name__=="__main__":
    df = pd.read_csv('Admission.csv')
    y_1 = pd.Categorical(df['Admission']).codes
    x_n = ['GRE', 'GPA']
    x_1 = df[x_n].values
    
    with pm.Model() as model_1:
        α = pm.Normal('α', mu=0, sd=10)
        β = pm.Normal('β', mu=0, sd=2, shape=len(x_n))
        μ = α + pm.math.dot(x_1, β)
        θ = pm.Deterministic('θ', 1 / (1 + pm.math.exp(-μ)))
        bd = pm.Deterministic('bd', -α/β[1] - β[0]/β[1] * x_1[:,0])
        yl = pm.Bernoulli('yl', p=θ, observed=y_1)
        idata_1 = pm.sample(2000, target_accept=0.9, return_inferencedata=True)

    
    idx = np.argsort(x_1[:,0])
    bd = idata_1.posterior['bd'].mean(("chain", "draw"))[idx]
    plt.scatter(x_1[:,0], x_1[:,1], c=[f'C{x}' for x in y_1])
    plt.plot(x_1[:,0][idx], bd, color='k');
    az.plot_hdi(x_1[:,0], idata_1.posterior['bd'], color='k')
    plt.xlabel(x_n[0])
    plt.ylabel(x_n[1])
    plt.show()

##subpct 2
    idx = np.argsort(x_1[:,0])
    bd = idata_1.posterior['bd'].mean(("chain", "draw"))[idx]
    plt.scatter(x_1[:,0], x_1[:,1], c=[f'C{x}' for x in y_0])
    plt.plot(x_1[:,0][idx], bd, color='k');
    az.plot_hdi(x_1[:,0], idata_1.posterior['bd'],hdi_prob=0.94, color='k')
    plt.xlabel(x_n[0])
    plt.ylabel(x_n[1])
    
## subpct 3
    with pm.Model() as model1:
        alpha = pm.Normal('alpha', mu=0, sd=10)
        beta = pm.Normal('beta', mu=0, sd=2, shape=len(x_n))

        mu = alpha + pm.math.dot([550, 3.5], beta)
        theta = pm.Deterministic('theta', 1 / (1 + pm.math.exp(-mu)))
        bd = pm.Deterministic('bd', -alpha / beta[1] - beta[0] / beta[1] * 550)

        yl1 = pm.Bernoulli('yl1', p=theta, observed=y_1)

        idata1 = pm.sample(2000, target_accept=0.9, return_inferencedata=True)

    idx = np.argsort(x_1[:, 0])
    bd = idata1.posterior['bd'].mean(("chain", "draw"))[idx]
    plt.scatter(x_1[:, 0], x_1[:, 1], c=[f'C{x}' for x in y_1])
    plt.plot(x_1[:, 0], bd, color='k')
    az.plot_hdi(x_1[:, 0], idata1.posterior['bd'], hdi_prob=0.9, color='k')
    plt.xlabel(x_n[0])
    plt.ylabel(x_n[1])
    plt.show()

##subpct 4
    with pm.Model() as model2:
        alpha = pm.Normal('alpha', mu=0, sd=10)
        beta = pm.Normal('beta', mu=0, sd=2, shape=len(x_n))

        mu = alpha + pm.math.dot([500, 3.2], beta)
        theta = pm.Deterministic('theta', 1 / (1 + pm.math.exp(-mu)))
        bd = pm.Deterministic('bd', -alpha / beta[1] - beta[0] / beta[1] * 500)

        yl2 = pm.Bernoulli('yl2', p=theta, observed=y_1)

        idata2 = pm.sample(2000, target_accept=0.9, return_inferencedata=True)

    idx = np.argsort(x_1[:, 0])
    bd = idata2.posterior['bd'].mean(("chain", "draw"))[idx]
    plt.scatter(x_1[:, 0], x_1[:, 1], c=[f'C{x}' for x in y_1])
    plt.plot(x_1[:, 0], bd, color='k')
    az.plot_hdi(x_1[:, 0], idata2.posterior['bd'], hdi_prob=0.9, color='k')
    plt.xlabel(x_n[0])
    plt.ylabel(x_n[1])
    plt.show()
