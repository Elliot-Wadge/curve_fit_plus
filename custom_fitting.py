#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# In[94]:



def curve_fit_plus(f, x, y, p0 = None, sigma = None, absolute_sigma = False, save = False):
    #plot the original data with error bars as points
    plt.errorbar(x,y,yerr = sigma, fmt = '.', zorder = 1)
    
    #call the curve fit function
    pOpt, pCov = curve_fit(f,x,y,p0 = p0,sigma = sigma, absolute_sigma = absolute_sigma)
    
    #start a string to store the values
    string = ''
    #iterate through pOpt
    for i in pOpt:
        #concatenate each value
        string += str(i) + ','
        
    #add the finishing touches with the function and the brackets  
    call = 'f(x,' + string + ')'
    #run the string as code
    fit = eval(call)
    
    #get the residuals
    res = y - fit
    
    #get the normalized residuals
    norm_res = res/sigma
    
    #get chi squared
    chisq = sum(norm_res**2)
    
    #plot the fit over the data
    plt.plot(x,fit,zorder = 2)
    
    #if you want to save the data you have to enter the following data and make save = True
    if save:
        filename1 = input("what is the filename you want for your fit plot")
        plt.ylabel(input("ylabel"))
        plt.xlabel(input("xlabel"))
        plt.legend(["data","fit"])
        plt.savefig(filename1)
    plt.show()
    
    plt.plot(x,norm_res,'o')
    if save:
        filename2 = input("what is the filename you want for your normalized residuals")
        plt.ylabel(input("ylabel"))
        plt.xlabel(input("xlabel"))
        plt.legend(["data","fit"])
        plt.savefig(filename2)
    plt.show()
    
    error = np.sqrt(np.diag(pCov))
    for i in range(len(pOpt)):
        print(f'variable {i} = {pOpt[i]} ± {error[i]}')
    print(f"chisq = {chisq} ± {np.sqrt(2*(len(x) - len(pOpt)))}")    
    print(f"reduced chisq = {chisq/(len(x) - len(pOpt))}")
    
    return pOpt, error, chisq
    





