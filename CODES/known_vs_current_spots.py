#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 12:18:40 2017

@author: manu
"""
import pandas as pd

POPS={"COS":["CEU","TSI","FIN","GBR","IBS","YRI","LWK","ASW","ACB","MKK","CHB","JPT","CHS","CDX","KHV","MXL","PUR","CLM","PEL","GIH"]}
#%%

g1k_hot=pd.read_excel('../HOTSPOTS_MAP.xlsx',sheet_name="ALL_HOTSPOTS")
hap_hot=pd.read_table("../KNOWN_HOTSPOTS/hotspots-coldspots-b37-filtered.txt",header=0)

    
#%%
con=0    
val_con=0
for ind,hap in hap_hot.iterrows():
        hits=g1k_hot[(g1k_hot.chr==hap.chr) & (((g1k_hot.start>=hap.hotstart) & (g1k_hot.end<=hap.hotend)) | (((g1k_hot.start<=hap.hotstart) & (g1k_hot.end>=hap.hotstart)) | ((g1k_hot.start<=hap.hotend) & (g1k_hot.end>=hap.hotend))))]  #computing the overlapping putative hotspots
        if not hits.empty:
            con+=1
            if not hits[hits.REFINED_rate>1].empty:                              #checking if the overlapping spots are validated
                val_con+=1
        #print(ind)
        
        
print(con,"out of",len(hap_hot),"hapmap hotspots are present in",len(g1k_hot)," putative hotspots from 1KGP ")        
print(val_con,"out of",len(hap_hot),"hapmap hotspots are present in",len(g1k_hot[g1k_hot.REFINED_rate>1])," validated hotspots from 1KGP ") 
