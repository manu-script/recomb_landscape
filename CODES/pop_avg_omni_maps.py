#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 09:53:13 2017

@author: manu
"""

import pandas as pd
import os
from scipy.interpolate import interp1d
import numpy as np

omni_new="../OMNI_INTERPOLATED/"     #Relative path of interpolated maps


POPS={"COS":["CEU","TSI","FIN","GBR","IBS","YRI","LWK","ASW","ACB","MKK","CHB","JPT","CHS","CDX","KHV","MXL","PUR","CLM","PEL","GIH"]}

maps={}

for pop in os.listdir(omni_new):
    maps[pop]={}
    print("Reading",pop)
    for chrom in os.listdir(omni_new+pop):
        maps[pop][chrom]=pd.read_table(omni_new+pop+"/"+chrom, header=0)         #Reading interpolated maps

#%%
omni_pa="../OMNI_POP_AVG/"                                                       #creating new directories for COSmopolitan map
if not os.path.exists(omni_pa):
       os.makedirs(omni_pa)

for sup in POPS.keys():
    if not os.path.exists(omni_pa+sup):
       os.makedirs(omni_pa+sup)
    avg={}
    for pop in POPS[sup]:
        for chrom in os.listdir(omni_new+pop):
            tmap=maps[pop][chrom]
            if not chrom in avg.keys():
                avg[chrom]=tmap.copy()
            else:
                avg[chrom]=pd.merge(avg[chrom],tmap[["pos","rate","map"]],how="left",on="pos")                 #merging population data into a single dataframe

    for chrom in os.listdir(omni_new+pop):
        print("Computing Population averaged map for",sup,chrom)
        achr=avg[chrom]["chr"]
        apos=avg[chrom]["pos"]
        arate=avg[chrom][list(set([col for col in avg[chrom].columns if "rate" in col]))].mean(axis=1)                     #averaging rate
        amap=avg[chrom][list(set([col for col in avg[chrom].columns if "map" in col]))].mean(axis=1)                        #averaging map distance
        pd.DataFrame({"chr":achr,"pos":apos,"rate":arate,"map":amap}).round(6).to_csv(omni_pa+sup+"/"+chrom,sep="\t",columns=["chr","pos","rate","map"],index=False)  #writing population averaged map
