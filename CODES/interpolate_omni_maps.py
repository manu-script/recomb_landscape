#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 14:53:05 2017

@author: manu

Step 1 : Modify the 1KGP OMNI maps to have same physical positions(bp) by interpolation
"""

import pandas as pd
import os
from scipy.interpolate import interp1d
import numpy as np

omni="../OMNI/"                   #Relative path to the 1KGP OMNI maps
omni_new="../OMNI_INTERPOLATED/"  #Relative path for creating the interpolated maps

positions={}
maps={}

for pop in os.listdir(omni):
    maps[pop]={}
    print("Reading",pop)
    for chrom in os.listdir(omni+pop):
        tmap=pd.read_table(omni+pop+"/"+chrom, header=0,names=["pos","rate","map","filter"])  #Reading maps into dataframes
        tmap=tmap[tmap["filter"]==0]                                                             #Removing filtered positions
        maps[pop][chrom]=tmap
        if not chrom in positions.keys():
            positions[chrom]=[]
        positions[chrom]=list(set(positions[chrom]+list(tmap["pos"])))                          #Creating a union set of positions from all the maps

for chrom in positions.keys():
    positions[chrom]=sorted(positions[chrom])                                                   #Sorting the chromosome-wise markers by genomic locations
#%%
if not os.path.exists(omni_new):
            os.makedirs(omni_new)                                                              #creating directories
#%%
for pop in os.listdir(omni):
    print("Computing interpolated map:",pop)
    if not os.path.exists(omni_new+pop):
            os.makedirs(omni_new+pop)
    for chrom in os.listdir(omni+pop):
        tmap=maps[pop][chrom]
        fmap=interp1d(tmap["pos"],tmap["map"])                                                 #interpolating function
        nmap=pd.DataFrame(columns=["chr","pos"])
        nmap["pos"]=positions[chrom]
        nmap["chr"]=chrom[:-4]
        nmap=pd.merge(nmap,tmap[["pos","map"]],how="left",on="pos")                            #copying map values where positions are equal
        nmap.loc[(nmap["map"].isnull()) & (nmap["pos"]<tmap["pos"].iloc[0]),"map"]=0            #setting map units as 0 for positions preceeding the map
        nmap.loc[(nmap["map"].isnull()) & (nmap["pos"]>tmap["pos"].iloc[-1]),"map"]=tmap["map"].iloc[-1]      #setting map units as the highest map unit for positions exceeding the map
        nmap.loc[(nmap["map"].isnull()),"map"]=fmap(nmap.loc[(nmap["map"].isnull()),"pos"])       #interpolating for the rest
        nmap["rate"]=list(np.diff(nmap["map"])/(np.diff(nmap["pos"])/1e6))+[0]                    #calculating rate for all the intervals
        nmap=nmap.round(6)
        nmap.to_csv(omni_new+pop+"/"+chrom, sep="\t", index=False,columns=["chr","pos","rate","map"])     #writing the interpolated map

print("Done!")
