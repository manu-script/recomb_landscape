#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 09:55:00 2017

@author: manu
"""
import os
import numpy as np
import pandas as pd
import peakutils as pu
import warnings
from scipy.optimize import OptimizeWarning
from joblib import Parallel, delayed
from multiprocessing import cpu_count
from scipy.interpolate import UnivariateSpline, interp1d
warnings.simplefilter("error", OptimizeWarning)
warnings.simplefilter("error", RuntimeWarning)

POPS={"COS":["CEU","TSI","FIN","GBR","IBS","YRI","LWK","ASW","ACB","MKK","CHB","JPT","CHS","CDX","KHV","MXL","PUR","CLM","PEL","GIH"]}

fmaps={}
for pop in os.listdir("../OMNI_INTERPOLATED/"):
    print("Reading interpolated map:",pop)
    if pop not in fmaps.keys():
        fmaps[pop]={}
    for chrom in os.listdir("../OMNI_INTERPOLATED/"+pop):
        gen_map=pd.read_table("../OMNI_INTERPOLATED/"+pop+"/"+chrom,header=0)
        fmaps[pop][chrom]=interp1d(gen_map["pos"],gen_map["map"])                        #Generating interpolation functions

def refine_hot(start,end,df):
     data=df.loc[(df.pos >= start) & (df.pos<=end),:].copy()                             #slicing dataframe for block values
     try:
             params=pu.gaussian_fit(np.array(data.pos),np.array(data.rate),center_only=False)   #estimate gaussian parameters
             data["gauss"]=pu.gaussian(data.pos,*params)                                    #fit a gaussian curve
             try:
                 spline = UnivariateSpline(data.pos, data.gauss-(data.gauss.max()/2), s=0)        #Full width half maximum
                 r1, r2 = spline.roots()
                 return (r1,r2)
             except:
                 d=data.iloc[data.gauss>data.gauss.max()/2,:]                                        #if FWHM fails, return datapoints > mean of gaussian curve
                 if not d.empty:
                     if not d.pos.iloc[0]==d.pos.iloc[-1]:
                         return (d.pos.iloc[0],d.pos.iloc[-1])
     except:
             d=data[data.rate>(data.rate.max()/2)]                                                #if gaussian fitting fails, return datapoints > half of max rate
             if not d.empty:
                 if not d.pos.iloc[0]==d.pos.iloc[-1]:
                     return (d.pos.iloc[0],d.pos.iloc[-1])

def spotify(inp):
    fname,h_out,c_out=inp
    items=fname.split("/")
    chrom=items[-1]
    pop=items[-2]
    print("Computing Hot & Cold spots:",fname)
    df=pd.read_table(fname,header=0)                                           #Reading map into dataframe
    fmap=interp1d(df.pos,df.map)
    df["dif"]=[0]+list(np.diff(df.rate))                                      #calculating consecutive differences in rate
    df["shif"]=list(np.diff(df.rate))+[0]
    h_ind=df[(df.dif<0)&(df.shif>0)].index+1
    h_spots=[(h_ind[i],h_ind[i+1]) for i in range(len(h_ind)-1)]               #computing hot blocks based on rise and fall of rates
    hotspots=[]
    for start,end in h_spots:
        hot=refine_hot(df.loc[start].pos,df.loc[end].pos,df)                   #refining the peak
        if hot:
            hotspots.append([int(hot[0]),int(hot[1])])

    hspots=pd.DataFrame(hotspots,columns=["start","end"]).round(6)
    hspots["n_start"]=list(hspots.start[1:])+[0]
    hspots["cont"]=hspots.n_start-hspots.end                                    #finding adjacent continuos peaks
    merged=[]
    tmp=pd.DataFrame(columns=["start","end","n_start","cont"])
    flag=False
    for ind,row in hspots.iterrows():
        if row.cont==0:
            tmp=tmp.append(row)
            flag=False
        elif row.cont!=0 and not tmp.empty and not flag:
            tmp=tmp.append(row)
            merged.append((tmp.start.iloc[0],tmp.end.iloc[-1]))                #Merging the adjacent peaks
            flag=True
            tmp=pd.DataFrame(columns=["start","end","n_start","cont"])

    ind=hspots[hspots.cont==0].index
    hspots=hspots[["start","end"]][~hspots.index.isin(set(list(ind)+list(ind+1)))].append(pd.DataFrame(merged,columns=["start","end"]),ignore_index=True).sort_values(by="start")
    hspots["avg_rate"]=(fmap(hspots["end"]) - fmap(hspots["start"])) / ((hspots["end"]-hspots["start"]) / 1e6)          #Computing average recombination rate
    hspots["chr"]=chrom[:-4]
    hspots["flag"]=hspots.avg_rate>1
    for p in POPS[pop]:
        f=fmaps[p][chrom]
        hspots[p+"_rate"]=(f(hspots["end"]) - f(hspots["start"])) / ((hspots["end"]-hspots["start"]) / 1e6)
        hspots.loc[(hspots["flag"]==False) & (hspots[p+"_rate"]>1),"flag"]=True                                          #Interpolating and computing rate in each population
    hspots=hspots[hspots.flag==True]
    hspots.round(6).to_csv(h_out,sep="\t",columns=["chr","start","end"]+[i for i in hspots.columns if i.endswith("_rate")],index=False)    #Writing hotspots
    hspots["n_start"]=list(hspots.start[1:])+[0]
    c_spots=hspots[["end","n_start"]][:-1]                                     #Computing the locations of coldspots between hotspots
    coldspots=[]
    for start,end in zip(c_spots.end,c_spots.n_start):
        rate=(fmap(end)-fmap(start))/((end-start)/1e6)                         #Calculating the average recombination rate in coldspots
        coldspots.append([df.chr.iloc[0],int(start),int(end),rate])
    
    cspots=pd.DataFrame(coldspots,columns=["chr","start","end","avg_rate"])
    cspots["chr"]=chrom[:-4]
    
    cspots["flag"]=cspots.avg_rate<=1
    for p in POPS[pop]:
        f=fmaps[p][chrom]
        cspots[p+"_rate"]=(f(cspots["end"]) - f(cspots["start"])) / ((cspots["end"]-cspots["start"]) / 1e6)    #computing the recombination rate in each population
        cspots.loc[(cspots["flag"]==False) & (cspots[p+"_rate"]<=1),"flag"]=True
    cspots=cspots[cspots.flag==True]
    
    cspots.round(6).to_csv(c_out,sep="\t",columns=["chr","start","end"]+[i for i in cspots.columns if i.endswith("_rate")],index=False)       #Writing coldspots

if not os.path.exists("../HOTSPOTS"):
       os.makedirs("../HOTSPOTS")

if not os.path.exists("../COLDSPOTS"):
       os.makedirs("../COLDSPOTS")

for sup in POPS.keys():
    if not os.path.exists("../HOTSPOTS/"+sup):
       os.makedirs("../HOTSPOTS/"+sup)

for sup in POPS.keys():
    if not os.path.exists("../COLDSPOTS/"+sup):
       os.makedirs("../COLDSPOTS/"+sup)

inp=[("../OMNI_POP_AVG/"+pop+"/"+chrom,"../HOTSPOTS/"+pop+"/"+chrom,"../COLDSPOTS/"+pop+"/"+chrom) for pop in os.listdir("../OMNI_POP_AVG/") for chrom in os.listdir("../OMNI_POP_AVG/"+pop)]
Parallel(n_jobs=cpu_count(), verbose=25)(delayed(spotify)(i)for i in inp)
