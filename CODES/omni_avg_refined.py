#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 10:20:42 2017

@author: manu
"""

import pandas as pd
import os
from scipy.interpolate import interp1d

if not os.path.exists("../HOTSPOTS/COS_REFINED"):
       os.makedirs("../HOTSPOTS/COS_REFINED")

if not os.path.exists("../COLDSPOTS/COS_REFINED"):
       os.makedirs("../COLDSPOTS/COS_REFINED")

for chrom in ["chr"+str(i)+".txt" for i in range(1,23)]:
    print("Processing:",chrom)
    COS_hot=pd.read_table("../HOTSPOTS/COS/"+chrom,header=0)              #reading putative hotspots
    COS_cold=pd.read_table("../COLDSPOTS/COS/"+chrom,header=0)            #reading putative coldspots
    REFINED=pd.read_table("../REFINED/"+chrom,header=0)                     #reading refined pedigree-based rates
    fmap=interp1d(REFINED.pos,REFINED.map)                                   #interpolating function
    COS_hot=COS_hot.rename(columns={"avg_rate":"COS_rate"})
    COS_cold=COS_cold.rename(columns={"avg_rate":"COS_rate"})
    
    COS_hot.loc[((COS_hot.start<=REFINED.pos.iloc[0]))|(COS_hot.end<=REFINED.pos.iloc[0]),"REFINED_rate"]=-1          #out of the range values set to -1
    COS_hot.loc[(COS_hot.start>=REFINED.pos.iloc[-1]) | (COS_hot.end>=REFINED.pos.iloc[-1]) ,"REFINED_rate"]=-1
    
    COS_cold.loc[((COS_cold.start<=REFINED.pos.iloc[0]))|(COS_cold.end<=REFINED.pos.iloc[0]),"REFINED_rate"]=-1
    COS_cold.loc[(COS_cold.start>=REFINED.pos.iloc[-1])|(COS_cold.end>=REFINED.pos.iloc[-1]),"REFINED_rate"]=-1
    
    hot=COS_hot[(COS_hot.start>=REFINED.pos.iloc[0]) & (COS_hot.end<=REFINED.pos.iloc[-1])]
    cold=COS_cold[(COS_cold.start>=REFINED.pos.iloc[0]) & (COS_cold.end<=REFINED.pos.iloc[-1])]
    
    COS_hot.loc[(COS_hot.start>=REFINED.pos.iloc[0]) & (COS_hot.end<=REFINED.pos.iloc[-1]),"REFINED_rate"]=(fmap(hot["end"]) - fmap(hot["start"])) / ((hot["end"]-hot["start"]) / 1e6)  #interpolation and calculationof pedigree rates
    COS_hot["start"]=COS_hot["start"].astype(int)
    COS_hot["end"]=COS_hot["end"].astype(int)
    COS_hot.round(6).to_csv("../HOTSPOTS/COS_REFINED/"+chrom,columns=["chr","start","end"]+[i for i in COS_hot.columns if i.endswith("_rate")],index=False,sep="\t")
    
    COS_cold.loc[(COS_cold.start>=REFINED.pos.iloc[0]) & (COS_cold.end<=REFINED.pos.iloc[-1]),"REFINED_rate"]=(fmap(cold["end"]) - fmap(cold["start"])) / ((cold["end"]-cold["start"]) / 1e6)  #interpolation and calculationof pedigree rates
    COS_cold["start"]=COS_cold["start"].astype(int)
    COS_cold["end"]=COS_cold["end"].astype(int)
    COS_cold.round(6).to_csv("../COLDSPOTS/COS_REFINED/"+chrom,columns=["chr","start","end"]+[i for i in COS_hot.columns if i.endswith("_rate")],index=False,sep="\t")