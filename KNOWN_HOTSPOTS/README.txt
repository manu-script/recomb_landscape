README FILE:
In order to run the source code provided in the “Download” page.

1) Install following perl packages
-------------------------------------
DBI
Math::BigInt
Math::BigFloat

2)Download Homologene.sql and Install 'Homologene' database

3)The compressed file PerlScripts.zip includes 3 perl scripts

	a)search.pl : For the identifying genomic repeat elements that are enriched in 
	the neighborhood region of the given gene set.

	b)search1.pl : For listing all genomic repeat elements found in a specific
	chromosomal location.

	c)search2.pl : For identifying genomic repeat elements that are enriched in
	given set of genes not only in main species but also in their orthologous genes

4)Download repeat and gene ANNOTATION TRACK tracks from NCBI using below mentioned links

For Homo sapiens: 
==================
REPEAT ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Homo_sapiens/sequence/BUILD.37.3/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Human-1-Repeat.txt' for chromosome 1"

GENE ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Homo_sapiens/sequence/BUILD.37.3/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to GRCh37.p5-Primary Assembly)

"After unzipping the file, rename it as Human-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Homo_sapiens/objects/BUILD.37.3/initial_release/repeat.q.gz

"After unzipping the file, rename it as Human-repeatAnn.txt"

For Mus musculus:
=================
REPEAT ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Mus_musculus/sequence/BUILD.38.1/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Mouse-1-Repeat.txt' for chromosome 1"

GENE ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Mus_musculus/sequence/BUILD.38.1/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to GRCm38-C57BL/6J)

"After unzipping the file, rename it as Mouse-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Mus_musculus/objects/BUILD.38.1/initial_release/repeat.q.gz

"After unzipping the file, rename it as Mouse-repeatAnn.txt"

For Rattus norvegicus:
=======================
REPEAT ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Rattus_norvegicus/sequence/BUILD.5.1/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Rat-1-Repeat.txt' for chromosome 1"

GENE ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Rattus_norvegicus/sequence/BUILD.5.1/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to Rnor_5.0-Primary Assembly)

"After unzipping the file, rename it as Rat-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Rattus_norvegicus/objects/BUILD.5.1/initial_release/repeat.q.gz

"After unzipping the file, rename it as Rat-repeatAnn.txt"

For Bos taurus:
===============
REPEAT ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Bos_taurus/sequence/BUILD.6.1/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Cow-1-Repeat.txt' for chromosome 1"


GENE ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Bos_taurus/sequence/BUILD.6.1/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to Btau_4.6.1-Primary Assembly)

"After unzipping the file, rename it as Cow-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Bos_taurus/objects/BUILD.6.1/initial_release/repeat.q.gz

"After unzipping the file, rename it as Cow-repeatAnn.txt"

For Canis familiaris:
=====================
REPEAT ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Canis_familiaris/sequence/BUILD.3.1/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Dog-1-Repeat.txt' for chromosome 1"

GENE ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Canis_familiaris/sequence/BUILD.3.1/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to CanFam3.1-Primary Assembly)

"After unzipping the file, rename it as Dog-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Canis_familiaris/objects/BUILD.3.1/initial_release/repeat.q.gz

"After unzipping the file, rename it as Dog-repeatAnn.txt"

For Pan troglodytes:
====================
REPEAT ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Pan_troglodytes/sequence/BUILD.3.1/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Chimp-1-Repeat.txt' for chromosome 1"

GENE ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Pan_troglodytes/sequence/BUILD.3.1/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to Pan_troglodytes-2.1.4-Primary Assembly)

"After unzipping the file, rename it as Chimp-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Pan_troglodytes/objects/BUILD.3.1/initial_release/repeat.q.gz

"After unzipping the file, rename it as Chimp-repeatAnn.txt"

For Loxodonta africana:
=======================
REPEAT ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Loxodonta_africana/sequence/current/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one contig] named as 'Elephant-Un|NW_003575740.1-Repeat.txt' for contig Un|NW_003575740.1"

GENE ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Loxodonta_africana/sequence/current/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to Loxafr3.0-Primary Assembly)

"After unzipping the file, rename it as Elephant-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Loxodonta_africana/objects/current/initial_release/repeat.q.gz

"After unzipping the file, rename it as Elephant-repeatAnn.txt"

For Nomascus leucogenys:
========================
REPEAT ANNOTATION TRACK:
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Nomascus_leucogenys/sequence/ANNOTATION_RELEASE.101/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Gibbon-2-Repeat.txt' for chromosome 2"

GENE ANNOTATION TRACK:
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Nomascus_leucogenys/sequence/ANNOTATION_RELEASE.101/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding toNleu_3.0-Primary Assembly)

"After unzipping the file, rename it as Gibbon-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Nomascus_leucogenys/objects/ANNOTATION_RELEASE.101/initial_release/repeat.q.gz

"After unzipping the file, rename it as Gibbon-repeatAnn.txt"

For Equus caballus:
===================
REPEAT ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Equus_caballus/sequence/BUILD.2.2/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Horse-1-Repeat.txt' for chromosome 1"


GENE ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Equus_caballus/sequence/BUILD.2.2/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to EquCab2.0-Primary Assembly)

"After unzipping the file, rename it as Horse-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE 
FILE:ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Equus_caballus/objects/BUILD.2.2/initial_release/repeat.q.gz

"After unzipping the file, rename it as Horse-repeatAnn.txt"

For Macaca mulatta:
===================
REPEAT ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Macaca_mulatta/sequence/BUILD.1.2/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Monkey-1-Repeat.txt' for chromosome 1"


GENE ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Macaca_mulatta/sequence/BUILD.1.2/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to Mmul_051212-Primary Assembly)

"After unzipping the file, rename it as Monkey-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE: 

ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Macaca_mulatta/objects/BUILD.1.2/initial_release/repeat.q.gz

"After unzipping the file, rename it as Monkey-repeatAnn.txt"

For Gorilla gorilla:
====================
REPEAT ANNOTATION TRACK:
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Gorilla_gorilla/sequence/ANNOTATION_RELEASE.100/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Gorilla-1-Repeat.txt' for chromosome 1"

GENE ANNOTATION TRACK:
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Gorilla_gorilla/sequence/ANNOTATION_RELEASE.100/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to gorGor3.1-Primary Assembly)

"After unzipping the file, rename it as Gorilla-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE:
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Gorilla_gorilla/objects/ANNOTATION_RELEASE.100/initial_release/repeat.q.gz

"After unzipping the file, rename it as Gorilla-repeatAnn.txt"

For Callithrix jacchus:
=======================
REPEAT ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Callithrix_jacchus/sequence/BUILD.1.1/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Marmoset-1-Repeat.txt' for chromosome 1"


GENE ANNOTATION TRACK: 

ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Callithrix_jacchus/sequence/BUILD.1.1/initial_release/seq_repeat.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to Callithrix jacchus-3.2-Primary Assembly)

"After unzipping the file, rename it as Marmoset-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE: 

ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Callithrix_jacchus/objects/BUILD.1.1/initial_release/repeat.q.gz

"After unzipping the file, rename it as Marmoset-repeatAnn.txt"

For Monodelphis domestica:
==========================
REPEAT ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Monodelphis_domestica/sequence/BUILD.2.2/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Opposum-1-Repeat.txt' for chromosome 1"

GENE ANNOTATION TRACK: 

ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Monodelphis_domestica/sequence/BUILD.2.2/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to MonDom5-Primary Assembly)

"After unzipping the file, rename it as Opposum-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE: 

ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Monodelphis_domestica/objects/BUILD.2.2/initial_release/repeat.q.gz

"After unzipping the file, rename it as Opposum-repeatAnn.txt"

For Pongo abelii:
=================
REPEAT ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Pongo_abelii/sequence/BUILD.1.2/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Orangutan-1-Repeat.txt' for chromosome 1"

GENE ANNOTATION TRACK: 

ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Pongo_abelii/sequence/BUILD.1.2/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to P_pygmaeus_2.0.2-Primary Assembly)

"After unzipping the file, rename it as Orangutan-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE: 

ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Pongo_abelii/objects/BUILD.1.2/initial_release/repeat.q.gz

"After unzipping the file, rename it as Orangutan-repeatAnn.txt"

For Sus scrofa:
===============
REPEAT ANNOTATION TRACK: 
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Sus_scrofa/sequence/BUILD.4.1/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Pig-1-Repeat.txt' for chromosome 1"

GENE ANNOTATION TRACK: 

ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Sus_scrofa/sequence/BUILD.4.1/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to Sscrofa10.2-Primary Assembly)

"After unzipping the file, rename it as Pig-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE: 

ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Sus_scrofa/objects/BUILD.4.1/initial_release/repeat.q.gz

"After unzipping the file, rename it as Pig-repeatAnn.txt"

For Ornithorhynchus anatinus:
=============================
REPEAT ANNOTATION TRACK: 

ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Ornithorhynchus_anatinus/sequence/BUILD.1.2/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Platypus-1-Repeat.txt' for chromosome 1"

GENE ANNOTATION TRACK: 

ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Ornithorhynchus_anatinus/sequence/BUILD.1.2/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to Ornithorhynchus_anatinus-5.0.1-Primary Assembly)

"After unzipping the file, rename it as Platypus-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE: 

ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Ornithorhynchus_anatinus/objects/BUILD.1.2/initial_release/repeat.q.gz

"After unzipping the file, rename it as Platypus-repeatAnn.txt"

For Oryctolagus cuniculus:
==========================
REPEAT ANNOTATION TRACK: 

ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Oryctolagus_cuniculus/sequence/BUILD.1.1/initial_release/seq_repeat.md.gz

"After unzipping the file, split it into different files [one file for one chromosome and/or contig] named as 'Rabbit-1-Repeat.txt' for chromosome 1"


GENE ANNOTATION TRACK: 

ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Oryctolagus_cuniculus/sequence/BUILD.1.1/initial_release/seq_gene.md.gz
(from both files, retain only ANNOTATION TRACK corresponding to OryCun2.0-Primary Assembly)

"After unzipping the file, rename it as Rabbit-Gene.txt"

REPEAT CLASSIFICATION AND NOMENCLATURE FILE:
ftp://ftp.ncbi.nlm.nih.gov/genomes/MapView/Oryctolagus_cuniculus/objects/BUILD.1.1/initial_release/repeat.q.gz

"After unzipping the file, rename it as Rabbit-repeatAnn.txt"

5) Download population statistics generated from GREAM download page.


