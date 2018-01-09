#!/bin/bash

#The run time of the scripts are based on a 3 Ghz quad core machine. 

rm -r OMNI_INTERPOLATED/ OMNI_POP_AVG/ HOTSPOTS/ COLDSPOTS/ *.xlsx CODES/*png

cd CODES

python3 interpolate_omni_maps.py        #To interpolate missing coordinates from the 1KGP maps. Approx run time:5m45s
python3 omni_corelation.py              #To find pairwise correaltion between interpolated rates. Approx run time:2m40s
python3 pop_avg_omni_maps.py            #To generate cosmopolitan map. Approx run time:1m20s
python3 spot_hot_n_cold_omni_avg_maps.py #To detect putative hotspots and coldspots. Approx run time:16m22s
python3 omni_avg_refined.py               #To fetch pedigree-based rates and validate putative spots. Approx run time:10s
python3 analyse_1KGP_hotspots.py          #Compute the statistics of putative and validated hotspots. Approx run time: 3m53s
python3 known_vs_current_spots.py         #To compare known hotspot regions to the hotspots identified in our study. run time:37m7s
