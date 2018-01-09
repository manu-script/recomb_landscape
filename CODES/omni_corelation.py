#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 14:12:36 2017

@author: manu
"""

import pandas as pd
import itertools
import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib import rcParams, rc
import seaborn as sns
sns.set()

#%%

POPS=["CEU","TSI","FIN","GBR","IBS","YRI","LWK","ASW","ACB","MKK","CHB","JPT","CHS","CDX","KHV","MXL","PUR","CLM","PEL","GIH"]
rates={}
for pop in POPS:
        print("Reading rates:",pop)
        if pop not in rates.keys():
            rates[pop]=[]
        for chrom in ["chr"+str(i)+".txt" for i in range(1,23)]:
            rates[pop]=rates[pop]+list(pd.read_table("../OMNI_INTERPOLATED/"+pop+"/"+chrom,header=0)["rate"])           #Reading interpolated rates from the 1KGP maps

#%%
df=pd.DataFrame(index=POPS,columns=POPS)               #Empty Correlation matrix

for p in POPS:
    df.loc[p,p]=1                                         #Diagonal elements of the matrix are 1
    
#%%       
def func(inp):
    a,b=inp
    print("Computing pair-wise correlation:",a,b)
    r=round(stats.pearsonr(rates[a],rates[b])[0],2)       #Computing the pearson correlation coefficient 
    df.loc[a,b]=r                                           #Filling the matrix
    df.loc[b,a]=r
    
for i in itertools.combinations(POPS,2):
    func(i)                                                 #Making pairwise combinations of populations

df.to_excel("../OMNI_CORRELATIONS.xlsx")                    #writing the correlation matrix to an excel sheet

#%%
rcParams.update({'font.size': 10,'font.weight':"bold"})
rc('xtick', labelsize=14)
rc('ytick',labelsize=14)
fig = plt.figure(figsize=(9, 5))
#ax = fig.add_subplot(111)

df=pd.read_excel("../OMNI_CORRELATIONS.xlsx")
df = df[df.columns].astype(float)    
                                                              #Plotting a cluster map of the matrix

#ax=sns.clustermap(df,vmin=0.6,vmax=1, annot=True,cmap="hot",robust=True,annot_kws={"size": 10},linewidths=.5,cbar_kws={'ticks' : [0.6,0.7,0.8,0.9,1]})
ax=sns.clustermap(df,vmin=0.6,vmax=1,cmap="jet_r",cbar_kws={'ticks' : [0.6,0.7,0.8,0.9,1]})
plt.setp(ax.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
plt.setp(ax.ax_heatmap.xaxis.get_majorticklabels(), rotation=90)

plt.savefig("clustermap.png",format='png', dpi=300)  