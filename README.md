# BOP27 genome Genbank file built from the NC_000913 version 3 genome.
Difference between the BOP27 and NC_000913 version are:  
1. Deletion of 2 basepairs at 2173363 (gatC) 
2. Insertion of 'G' at 3560456 (glpR)  
3. Insertion of 'CG' at 4296381 (gltP/yjcO)  

These differences are detailed at the following:
http://systemsbiology.ucsd.edu/BOP27_sequence

# Running the script
1. Install `bioconda`: a straight-forward and very successful way of doing this is by installing the Anaconda Python computational tools distribution (https://www.anaconda.com/download).
2. Install the `co` package (`pip install co`) using the Ananconda based `pip` installed in step 1 (`~/anaconda3/bin/pip`).
3. Use the `make_new_ref.py` script as a template for creating your custom reference.
