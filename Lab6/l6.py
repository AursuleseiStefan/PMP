import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import arviz as az

def exe1():
    #exercitiul 1
    data=pd.read_csv("C:/Users/aursu/Downloads/data.csv")
    momage=data['momage'].tolist()
    ppvt=data['ppvt'].tolist()
    plt.scatter(ppvt,momage)
    plt.show()
    #Exercitiul 2
    a=[]
    a=momage
    a.sort()
    np.random.seed(1)
    N = 40
    for i in momage:
        alpha_real = a[:1]
        beta_real = momage[i]/ppvt[i]
        eps_real = np.random.normal(0, 2, size=N)
        x = np.random.normal(40, 1, N)
        y_real = alpha_real + beta_real * x
        y = y_real + eps_real
    _, ax = plt.subplots(1, 2, figsize=(8, 4))
    ax[0].plot(x, y, 'C0.')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y', rotation=0)
    ax[0].plot(x, y_real, 'k')
    az.plot_kde(y, ax=ax[1])
    ax[1].set_xlabel('y')
    plt.tight_layout()
    plt.show()
    
if __name__=="__main__":
    exe1()
    
