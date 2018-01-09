![N|Solid](http://www.ibab.ac.in/wp-content/uploads/2013/11/IBAB-logo.png)

Codes and Datasets used in the manuscript titled "Systematic Analyses of Autosomal Recombination Rates from the 1000 Genomes Project Uncovers the Global Recombination Landscape in Humans."

### Data Sources
The following links point to the original sources from where the datasets have been downloaded.
* [OMNI/](http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/working/20130507_omni_recombination_rates/) - Linkage disequilibrium based recombination rates specific to 20 populations from the 1000 Genomes Project
* [REFINED/](https://github.com/cbherer/Bherer_etal_SexualDimorphismRecombination) - Refined Pedigree based recombination rates from Bherer et al.
* [KNOWN_HOTSPOTS/](https://github.com/auton1/Campbell_et_al) - Hotspots discovered in HapMap phase 2 and lifted over to hg19 by Campbell et al.

### CODES

A pipeline (`reproduce.bash`) is provided to help run the Python3 codes on a linux machine.

Install the following Python3 dependencies:

| Dependencies | Description |
| ------ | ------ |
| [SciPy Ecosystem](https://www.scipy.org/about.html) | Scipy, Pandas, Matplotlib, NumPy|
| [Joblib](https://pypi.python.org/pypi/joblib) | For a  bit of Parallelisation
| [PeakUtils](https://pypi.python.org/pypi/PeakUtils) | Functions for Peak refinement
| [Seaborn](https://seaborn.pydata.org/) | Fancy plots |

>To reproduce the entire analyses, download or clone this repo:
```sh
$ cd recomb_landscape/
$ bash reproduce.bash
```
>The entire analyses will take about 75 minutes on a 3Ghz quad-core machine.
