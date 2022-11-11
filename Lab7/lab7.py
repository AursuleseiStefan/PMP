import arviz as az
import matplotlib.pyplot as plt

import numpy as np
import pymc3 as pm
import pandas as pd

if __name__ == "__main__":

    data = pd.read_csv("C:/Users/aursu/Downloads/prices.csv")
    #data = open("C:/Users/aursu/Downloads/prices.csv", 'r')

    price = data['Price'].values
    speed = data['Speed'].values
    hardDrive = data['HardDrive'].values
    ram = data['Ram'].values
    premium = data['Premium'].values
    
    
    pc_model = pm.Model()
    
    with pc_model:
        a = pm.Normal('a', mu=0, sd=10)

        bprice = pm.Normal('bprice', mu=0, sd=10)
        
        sigma = pm.HalfNormal('sigma', sd=1)

        mu = pm.Deterministic('mu',a + bprice * speed)
        
        ppvt_like = pm.Normal('ppvt_like', mu=mu, sd=sigma, observed=hardDrive)

        trace = pm.sample(20000, tune=20000, cores=4)
    
    fig, axes = plt.subplots(2, 2, sharex=False, figsize=(10, 8))
    axes[0,0].scatter(speed, price, alpha=0.6)
    axes[0,1].scatter(hardDrive, price, alpha=0.6)
    axes[1,0].scatter(ram, price, alpha=0.6)
    axes[1,1].scatter(premium, price, alpha=0.6)
    axes[0,0].set_ylabel("Price")
    axes[0,0].set_xlabel("Speed")
    axes[0,1].set_xlabel("HardDrive")
    axes[1,0].set_xlabel("Ram")
    axes[1,1].set_xlabel("Premium")
    plt.show()