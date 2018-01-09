#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:38:55 2017

@author: manu
"""
import itertools
import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import scipy.stats as stats
import seaborn as sns
from matplotlib.collections import BrokenBarHCollection
from matplotlib import rcParams, rc
sns.set_style("whitegrid")
from matplotlib import rcParams, rc
sns.set()



POPS={"COS":["CEU","TSI","FIN","GBR","IBS","YRI","LWK","ASW","ACB","MKK","CHB","JPT","CHS","CDX","KHV","MXL","PUR","CLM","PEL","GIH"]}
#%%

hot=pd.DataFrame(columns=pd.read_table("../HOTSPOTS/COS_REFINED/chr22.txt",header=0).columns)   #Fetching headers
cold=pd.DataFrame(columns=pd.read_table("../COLDSPOTS/COS_REFINED/chr22.txt",header=0).columns)
gaps=pd.read_table("hg19_gap.txt",header=0,sep="\t")
cos=pd.DataFrame(columns=["chr","start","rate","map","end","dist"])

for chrom in ["chr"+str(i)+".txt" for i in range(1,23)]:
    print("Reading:",chrom)
    hot=hot.append(pd.read_table("../HOTSPOTS/COS_REFINED/"+chrom,header=0),ignore_index=True)
    cold=cold.append(pd.read_table("../COLDSPOTS/COS_REFINED/"+chrom,header=0),ignore_index=True)  #reading hotspots and coldspots
    tmp_df=pd.read_table("../OMNI_POP_AVG/COS/"+chrom,header=0,names=["chr","start","rate","map"])
    tmp_df["end"]=list(tmp_df.start[1:].values)+[None]
    tmp_df["dist"]=tmp_df.end-tmp_df.start
    cos=cos.append(tmp_df[tmp_df.dist>50000])
    
#%% Dropping hotspots and coldspots in hg19 assembly gaps and SNP sparse regions
    
for ind,gap in gaps.iterrows():
   hot.drop(hot.loc[(hot.chr==gap.chr)&(((hot.start>=gap.start)&(hot.end<=gap.end)) | ((hot.start<=gap.end)&(hot.end>=gap.end)) | ((hot.start<=gap.start)&(hot.end>=gap.start)) )].index,inplace=True)
   cold.drop(cold.loc[(cold.chr==gap.chr)&(((cold.start>=gap.start)&(cold.end<=gap.end)) | ((cold.start<=gap.end)&(cold.end>=gap.end)) | ((cold.start<=gap.start)&(cold.end>=gap.start)) )].index,inplace=True)

for ind,gap in cos.iterrows():
   hot.drop(hot.loc[(hot.chr==gap.chr)&(((hot.start>=gap.start)&(hot.end<=gap.end)) | ((hot.start<=gap.end)&(hot.end>=gap.end)) | ((hot.start<=gap.start)&(hot.end>=gap.start)) )].index,inplace=True)
   cold.drop(cold.loc[(cold.chr==gap.chr)&(((cold.start>=gap.start)&(cold.end<=gap.end)) | ((cold.start<=gap.end)&(cold.end>=gap.end)) | ((cold.start<=gap.start)&(cold.end>=gap.start)) )].index,inplace=True)
    
#%%    

hot["width"]=hot.end-hot.start               #calculating hotspot and coldspot widths
cold["width"]=cold.end-cold.start
hot.loc[hot.REFINED_rate>1,"Validated"]=True
hot.loc[hot.REFINED_rate<=1,"Validated"]=False
cold.loc[(cold.REFINED_rate<=1)&(cold.REFINED_rate>=0),"Validated"]=True
cold.loc[(cold.REFINED_rate>1)|(cold.REFINED_rate<0),"Validated"]=False

hot["Conserved"]=True
for col in hot.columns:
    if col.endswith("rate") and col!="COS_rate" and col!="REFINED_rate":             
        hot.loc[hot[col]<=1,"Conserved"]=False                                      

cold["Conserved"]=True
for col in cold.columns:
    if col.endswith("rate") and col!="COS_rate" and col!="REFINED_rate":
        cold.loc[(cold[col]>1),"Conserved"]=False                                   
        
all_hot=hot[(hot.Conserved) & (hot.Validated)]                                 #computing the hotspots and coldspots conserved in all populations
all_cold=cold[(cold.Conserved) & (cold.Validated)]

print("Putative hotspots:",len(hot))
print("Validated hotspots:",len(hot[hot.Validated]))
print("Putative coldspots:",len(cold))
print("Validated coldspots:",len(cold[cold.Validated]))
print("Conserved Hotspots in all 20 populations {} (validated)".format(len(all_hot)))
print("Conserved Coldspots in all 20 populations {} (validated)".format(len(all_cold)))
cols=['chr', 'start', 'end', 'width', 'Validated', 'Conserved']+[i for i in hot.columns if i.endswith("_rate")]

cold_sorted=cold.sort_values(by="COS_rate")
cold_sorted.to_excel("../COLDSPOTS_MAP.xlsx",sheet_name="ALL_COLDSPOTS",columns=cols,index=False)
hot_sorted=hot.sort_values(by="COS_rate",ascending=False)
hot_sorted.to_excel('../HOTSPOTS_MAP.xlsx',sheet_name="ALL_HOTSPOTS",index=False,columns=cols)

#%%   
print("Number of Hotspots per chromosome")        
dist=[]
for chrom in ["chr"+str(i) for i in range(1,23)]:
    tmp=hot[(hot.chr==chrom)&(hot.Validated)].copy()
    print(chrom,len(tmp))
    tmp.sort_values(by="start",inplace=True)
    dist_df=pd.DataFrame({"d_end":tmp.start[1:].values,"d_start":tmp.end[:-1].values})
    dist_df["dist"]=dist_df.d_end-dist_df.d_start
    for ind,gap in gaps[gaps.chr==chrom].iterrows():
        dist_df.drop(dist_df.loc[(((dist_df.d_start>=gap.start)&(dist_df.d_end<=gap.end)) | ((dist_df.d_start<=gap.end)&(dist_df.d_end>=gap.end)) | ((dist_df.d_start<=gap.start)&(dist_df.d_end>=gap.start)))].index,inplace=True)
    for ind,gap in cos[cos.chr==chrom].iterrows():
        dist_df.drop(dist_df.loc[(((dist_df.d_start>=gap.start)&(dist_df.d_end<=gap.end)) | ((dist_df.d_start<=gap.end)&(dist_df.d_end>=gap.end)) | ((dist_df.d_start<=gap.start)&(dist_df.d_end>=gap.start)))].index,inplace=True)
    d=dist_df.d_end-dist_df.d_start
    dist=dist+list(d.values)

dist=pd.Series(dist)              
dist.dropna(inplace=True)

def remove_outlier(x):
    minm=x.mean()-(3*x.std())
    maxm=x.mean()+(3*x.std())
    return x[(x>minm)&(x<maxm)]
                                     
dist=remove_outlier(dist)
hot_width=remove_outlier(hot.width[hot.Validated])
cold_width=remove_outlier(cold.width[cold.Validated])
                                          #Calculating distances between adjacent hotspots
print("Average distance between Validated Hotspots:",dist.mean(),"Std:",dist.std())
print("\n\nValidated Hotspot width: Mean=",hot_width.mean(),"Median=",hot_width.median(),"Std=",hot_width.std())
print("\n\nValidated Coldspot width: Mean=",cold_width.mean(),"Median=",cold_width.median(),"Std=",cold_width.std())

print("\n\nAverage LD rate of Validated Hotspots:",hot.COS_rate[hot.Validated].mean(),"Median:",hot.COS_rate[hot.Validated].median(),"Std:",hot.COS_rate[hot.Validated].std())
print("\n\nAverage LD rate of Validated Coldspots:",cold.COS_rate[cold.Validated].mean(),"Median:",cold.COS_rate[cold.Validated].median(),"Std:",cold.COS_rate[cold.Validated].std())

print("\n\nAverage PED rate of Validated Hotspots:",hot.REFINED_rate[hot.Validated].mean(),"Median:",hot.REFINED_rate[hot.Validated].median(),"Std:",hot.REFINED_rate[hot.Validated].std())
print("\n\nAverage PED rate of Validated Coldspots:",cold.REFINED_rate[cold.Validated].mean(),"Median:",cold.REFINED_rate[cold.Validated].median(),"Std:",cold.REFINED_rate[cold.Validated].std())

print("\n\nAverage LD rate of Unvalidated Hotspots:",hot.COS_rate[hot.Validated==False].mean(),"Median:",hot.COS_rate[hot.Validated==False].median(),"Std:",hot.COS_rate[hot.Validated==False].std())
print("\n\nAverage LD rate of Unvalidated Coldspots:",cold.COS_rate[cold.Validated==False].mean(),"Median:",cold.COS_rate[cold.Validated==False].median(),"Std:",cold.COS_rate[cold.Validated==False].std())

print("\n\nAverage PED rate of Unvalidated Hotspots:",hot.REFINED_rate[hot.Validated==False].mean(),"Median:",hot.REFINED_rate[hot.Validated==False].median(),"Std:",hot.REFINED_rate[hot.Validated==False].std())
print("\n\nAverage PED rate of Unvalidated Coldspots:",cold.REFINED_rate[cold.Validated==False].mean(),"Median:",cold.REFINED_rate[cold.Validated==False].median(),"Std:",cold.REFINED_rate[cold.Validated==False].std())

#%% Plotting the distribution of strength of hotspots

fig = plt.figure(figsize=(9, 5))
ax = fig.add_subplot(111)

ax.hist(hot.COS_rate[hot.Validated],bins=500,color="red",alpha=0.75,label="Validated Hotspots")
ax.hist(hot.COS_rate[hot.Validated==False],bins=500,color="orange",alpha=0.75,label="Unvalidated Hotspots")

plt.xlabel("LD-based Cosmopolitan Recombination Rate in cM/Mb units",fontsize=14, fontweight='bold')
plt.ylabel("Frequency",fontsize=14, fontweight='bold')
plt.xticks(fontsize=14, fontweight='bold')
plt.yticks(fontsize=14, fontweight='bold')
#plt.title("Distribution of the Average Strength of Validated Hotspots and Coldspots")
ax.legend(loc="lower right")
plt.xlim(-1,100)
plt.savefig("hist_LD_hotspots.png",format='png',dpi=1200)  

#%%

plt.figure(figsize=(9, 5))

plt.hist(cold.COS_rate[cold.Validated],bins=500,color="blue",alpha=0.75,label="Validated Coldspots")
plt.hist(cold.COS_rate[cold.Validated==False],bins=500,color="aqua",alpha=0.75,label="Unvalidated Coldspots")
plt.legend()
plt.xticks(fontsize=14, fontweight='bold')
plt.yticks(fontsize=14, fontweight='bold')
#plt.xlabel("LD-based Cosmopolitan Recombination Rate in cM/Mb units")
#plt.ylabel("Frequency")
plt.xlim(-0.1,20)
plt.savefig("hist_LD_coldspots.png",format='png',dpi=1200) 
#%%
fig = plt.figure(figsize=(9, 5))
ax = fig.add_subplot(111)

ax.hist(hot.REFINED_rate[hot.Validated],bins=500,color="red",alpha=0.75,label="Validated Hotspots")
ax.hist(cold.REFINED_rate[cold.Validated==False],bins=500,color="aqua",alpha=0.75,label="Unvalidated Coldspots")

plt.xlabel("Pedigree-based Cosmopolitan Recombination Rate in cM/Mb units",fontsize=14, fontweight='bold')
plt.ylabel("Frequency",fontsize=14, fontweight='bold')
plt.xticks(fontsize=14, fontweight='bold')
plt.yticks(fontsize=14, fontweight='bold')
#plt.title("Distribution of the Average Strength of Validated Hotspots and Coldspots")
ax.legend(loc="lower right")
plt.xlim(-1,100)
plt.savefig("hist_PED_validated.png",format='png',dpi=1200)  

#%%

plt.figure(figsize=(9, 5))
plt.hist(hot.REFINED_rate[hot.Validated==False],bins=500,color="orange",alpha=0.75,label="Unvalidated Hotspots")
plt.hist(cold.REFINED_rate[cold.Validated],bins=500,color="blue",alpha=0.75,label="Validated Coldspots")
plt.legend()
plt.xticks(fontsize=14, fontweight='bold')
plt.yticks(fontsize=14, fontweight='bold')
#plt.xlabel("Pedigree-based Cosmopolitan Recombination Rate in cM/Mb units")
#plt.ylabel("Frequency")
plt.xlim(-0.01,1.01)
plt.savefig("hist_PED_unvalidated.png",format='png',dpi=1200) 





#%%        

df_put=pd.DataFrame(index=POPS["COS"],columns=POPS["COS"])
df_val=pd.DataFrame(index=POPS["COS"],columns=POPS["COS"])

for pop in POPS["COS"]:
    tmp_hot=hot.loc[:,pop+"_rate"]
    df_put.loc[pop,pop]=len(tmp_hot[tmp_hot>1])                         #calculating total number of putative hotspots in a population
    
    ref_hot=hot.loc[tmp_hot.index[tmp_hot>1],"REFINED_rate"]
    df_val.loc[pop,pop]=len(ref_hot[ref_hot>1])                          #calculating number of validated hotspots in a population
    
for a,b in itertools.combinations(POPS["COS"],2):                       #pairwise computation of shared hotspots
    tmp_a=hot.loc[:,a+"_rate"]
    a_hot_put=tmp_a[tmp_a>1]
    
    tmp_b=hot.loc[:,b+"_rate"]
    b_hot_put=tmp_b[tmp_b>1]
    
    put_ind=list(set(a_hot_put.index).intersection(set(b_hot_put.index)))
    ref_df=hot.loc[put_ind,"REFINED_rate"]
    val=ref_df[ref_df>1]
    
    df_put.loc[a,b]=len(put_ind)
    df_put.loc[b,a]=len(put_ind)
    
    df_val.loc[a,b]=len(val)
    df_val.loc[b,a]=len(val)
    
df_val.to_excel("../SHARED_VALIDATED_HOTSPOTS.xlsx")    
#%%

fig = plt.figure(figsize=(9, 5))
ax = fig.add_subplot(111)

order=["YRI","LWK","ASW","ACB","MKK","CEU","TSI","FIN","GBR","IBS","MXL","PUR","CLM","PEL","GIH","CHB","JPT","CHS","CDX","KHV"]
df = df_val.loc[order,order].astype(float)    
ax=sns.heatmap(df,cmap="jet_r",vmin=37000,vmax=49000,cbar_kws={'ticks' : [37000,40000,43000,46000,49000]})
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.savefig("heatmap.png",format='png', dpi=1200)  
#%%  Computing hotspots unique to a super-population


afr_uniq=hot[((hot.YRI_rate>1) | (hot.LWK_rate>1) | (hot.ASW_rate>1) | (hot.ACB_rate>1) | (hot.MKK_rate>1)) &
             ((hot.CEU_rate<=1) & (hot.TSI_rate<=1) & (hot.FIN_rate<=1) & (hot.GBR_rate<=1) & (hot.IBS_rate<=1) &
             (hot.CHB_rate<=1) & (hot.JPT_rate<=1) & (hot.CHS_rate<=1) & (hot.CDX_rate<=1) & (hot.KHV_rate<=1) &
             (hot.MXL_rate<=1) & (hot.PUR_rate<=1) & (hot.CLM_rate<=1) & (hot.PEL_rate<=1) & (hot.GIH_rate<=1))]   

print("\n\nHotspots present in one or more African populations and absent in all Non-African populations: Put-",len(afr_uniq), "Val-", len(afr_uniq[afr_uniq.Validated]))

eur_uniq=hot[((hot.CEU_rate>1) | (hot.TSI_rate>1) | (hot.FIN_rate>1) | (hot.GBR_rate>1) | (hot.IBS_rate>1)) &
             ((hot.YRI_rate<=1) & (hot.LWK_rate<=1) & (hot.ASW_rate<=1) & (hot.ACB_rate<=1) & (hot.MKK_rate<=1) &
             (hot.CHB_rate<=1) & (hot.JPT_rate<=1) & (hot.CHS_rate<=1) & (hot.CDX_rate<=1) & (hot.KHV_rate<=1) &
             (hot.MXL_rate<=1) & (hot.PUR_rate<=1) & (hot.CLM_rate<=1) & (hot.PEL_rate<=1) & (hot.GIH_rate<=1))]   

print("\n\nHotspots present in one or more European populations and absent in all Non-European populations: Put-",len(eur_uniq),"Val-", len(eur_uniq[eur_uniq.Validated]))

eas_uniq=hot[((hot.CHB_rate>1) | (hot.JPT_rate>1) | (hot.CHS_rate>1) | (hot.CDX_rate>1) | (hot.KHV_rate>1)) &
             ((hot.CEU_rate<=1) & (hot.TSI_rate<=1) & (hot.FIN_rate<=1) & (hot.GBR_rate<=1) & (hot.IBS_rate<=1) &
             (hot.YRI_rate<=1) & (hot.LWK_rate<=1) & (hot.ASW_rate<=1) & (hot.ACB_rate<=1) & (hot.MKK_rate<=1) &
             (hot.MXL_rate<=1) & (hot.PUR_rate<=1) & (hot.CLM_rate<=1) & (hot.PEL_rate<=1) & (hot.GIH_rate<=1))]   

print("\n\nHotspots present in one or more East Asian populations and absent in all Non-East Asian populations: Put-",len(eas_uniq),"Val-", len(eas_uniq[eas_uniq.Validated]))

amr_uniq=hot[((hot.MXL_rate>1) | (hot.PUR_rate>1) | (hot.CLM_rate>1) | (hot.PEL_rate>1)) &
             ((hot.CEU_rate<=1) & (hot.TSI_rate<=1) & (hot.FIN_rate<=1) & (hot.GBR_rate<=1) & (hot.IBS_rate<=1) &
             (hot.YRI_rate<=1) & (hot.LWK_rate<=1) & (hot.ASW_rate<=1) & (hot.ACB_rate<=1) & (hot.MKK_rate<=1) &
             (hot.CHB_rate<=1) & (hot.JPT_rate<=1) & (hot.CHS_rate<=1) & (hot.CDX_rate<=1) & (hot.KHV_rate<=1) & (hot.GIH_rate<=1))]   


print("\n\nHotspots present in one or more American populations and absent in all Non-American populations: Put-",len(amr_uniq),"Val-", len(amr_uniq[amr_uniq.Validated]))

sas_uniq=hot[(hot.GIH_rate>1) & ((hot.MXL_rate<=1) & (hot.PUR_rate<=1) & (hot.CLM_rate<=1) & (hot.PEL_rate<=1) &
             (hot.CEU_rate<=1) & (hot.TSI_rate<=1) & (hot.FIN_rate<=1) & (hot.GBR_rate<=1) & (hot.IBS_rate<=1) &
             (hot.YRI_rate<=1) & (hot.LWK_rate<=1) & (hot.ASW_rate<=1) & (hot.ACB_rate<=1) & (hot.MKK_rate<=1) &
             (hot.CHB_rate<=1) & (hot.JPT_rate<=1) & (hot.CHS_rate<=1) & (hot.CDX_rate<=1) & (hot.KHV_rate<=1))]   

print("\n\nHotspots present in GIH and absent in all other populations: Put-",len(sas_uniq),"Val-", len(sas_uniq[sas_uniq.Validated]))
