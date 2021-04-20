#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np
from scipy.optimize import curve_fit


# In[94]:



def curve_fit_plus(f, x, y, p0 = None, sigma = None, absolute_sigma = False, save = False):
    
    #call the curve fit function
    pOpt, pCov = curve_fit(f,x,y,p0 = p0,sigma = sigma, absolute_sigma = absolute_sigma)
    
    
    fit = f(x,*pOpt)
    
    #get the residuals
    res = y - fit
    
    try:
        #get the normalized residuals
        norm_res = res/sigma
    
        #get chi squared
        chisq = sum(norm_res**2)
        
    
    except:
        print('chisq set to zero error in res/sigma')
        chisq = 0
    
    
    
    
    error = np.sqrt(np.diag(pCov))
    for i in range(len(pOpt)):
        print(f'variable {i} = {pOpt[i]} ± {error[i]}')
    print(f"chisq = {chisq} ± {np.sqrt(2*(len(x) - len(pOpt)))}")    
    print(f"reduced chisq = {chisq/(len(x) - len(pOpt))}")
    
    return pOpt, error, chisq
    





