# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 17:01:49 2018

@author: hanseni

Functions placed here are included in the Pyfs business language 

"""
from math import exp, log
from numpy import transpose , array
from scipy.stats import norm
import inspect 
classfunk = []
try:
    from cvxopt import matrix
    from model_cvx import mv_opt, mv_opt_prop
    classfunk = ['TRANS']    # names a classfunk which can be called 
except:
    print('Pyfs info: CVXopt not installed')
    pass

def sum_excel(*arg):
    ''' a functions which sums the arguments used in models franslated from excel 
    '''
    return sum(arg)
    
def logit(number):
    ''' A function which returns the logit of a number 
    '''
    return(-log(1.0/number-1.0)) 
    
def normcdf(input,mu=0.0,sigma=1.0):
    return norm.cdf(input,mu,sigma)    



