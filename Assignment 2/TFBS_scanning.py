# Belle Pan
# 260839939

import math

# This function encodes a DNA nucleotide as an integer between 0 and 3
# It returns the encoded value, or -1 if the input is not a valid nucleotide.
def encode(nucleotide):
    """
    Args:
        nucleotide: A string of one character
    Returns:
        An integer encoding the nucleotide, or -1 if not a valid nucleotide
    """
    # WRITE YOUR QUESTION 1 CODE HERE
    nucleotide_dict = {"A":0 , "C":1 , "G":2 , "T":3}
    if nucleotide in nucleotide_dict:
        return nucleotide_dict[nucleotide]
    else:
        return -1

# This function builds and returns a Position Frequency Matrix from the 
# list of sequences provided as input. The PFM is stored in the form of a
# list of lists.
def build_PFM(sequences):
    """
    Args:
        sequences: A list of sequences of equal lengths
    Returns:
        The position Frequency Matrix build from the sequences, stored
        as a two-dimensional list
    """

    # You may find this useful: To create a list of lists of 4 rows and L columns:
    # PFM = [[0 for i in range(L)] for j in range(4)]
    
    # WRITE YOUR QUESTION 2 CODE HERE
    PFM = [[0 for x in range(len(sequences[0]))] for y in range(4)]
    for sequence in sequences:
        for nucIndex in range(len(sequence)):
            PFM [encode(sequence[nucIndex])][nucIndex] += 1
    return PFM


# This function builds and returns a PWM from a PFM and a pseudocount value. 
# The PWM is stored as a list of lists.
def get_PWM_from_PFM(PFM, pseudocount):
    """
    Args:
        PFM: A position frequency matrix, stored as a two-dimensional list
        pseudocount: A non-negative floating point number
    Returns:
        A position weight matrix, stored as a two-dimensional list
    """
    # You may find this useful: To create a list of lists of 4 rows and L columns:
    # PWM = [[0 for i in range(L)] for j in range(4)]

    # WRITE YOUR QUESTION 3 CODE HERE
    PWM = [[0 for x in range(len(PFM[0]))] for y in range(4)]
    for y in range(4):
        for x in range(len(PFM[0])):
            PWM[y][x] = math.log10((PFM[y][x] + pseudocount)/(PFM[0][x]+PFM[1][x]+PFM[2][x]+PFM[3][x]+4*pseudocount))-math.log10(0.25)
    return PWM


# This function calculates and returns the score of a given sequence with a given PWM
def score(sequence, PWM):
    """
    Args:
        sequence: A DNA sequence
        PWM: A position weight matrix, of the same length as the sequence
    Returns:
        A floating point number corresponding to the score of the sequence 
        for the given PWM
    """
    # WRITE YOUR QUESTION 4 CODE HERE
    s = 0
    for nucIndex in range(len(sequence)):
        s += PWM[encode(sequence[nucIndex])][nucIndex]
    return s


# This function identifies and returns the list of positions in the given sequence 
# where the PWM score is larger or equal to the threshold
def predict_sites(sequence, PWM, threshold = 0):
    """
    Args:
        sequence: A DNA sequence
        PWM: A position weight matrix
        threshold (optional): Minimum score needed to be predicted as a binding site
    Returns:
        A list of positions with match scores greater or equal to threshold
    """
    # WRITE YOUR QUESTION 5 CODE HERE
    sites = []
    for i in range(len(sequence)-len(PWM[0])):
        s = score(sequence[i:i+len(PWM[0])], PWM)
        if s > threshold:
            sites.append(i)
    return sites


# This function takes as input a dictionary of gene positions, a list of 
# PWM hits, and a maxDist value, and builds and returns a new dictionary with the same genes
# as keys, and the count of the number of hits within distance at most max_dist as values.
def count_hits_per_gene(gene_pos, hits, max_dist = 10):
    """
    Args:
        genePos: A dictionary of gene positions
        hits: A list of positions of hits
        maxDist (optional): The maximum distance to be associated to a gene
    Returns:
        A dictionary that associates to each gene the number of hits with
        distance maxDist
    """   
    # You may find this useful: it creates a new dictionary with
    # the same keys as the gene_pos dictionary, and values 0
    # hit_count=dict.fromkeys(gene_pos.keys(),0)
  
    # WRITE YOUR QUESTION 6 CODE HERE
    hit_count=dict.fromkeys(gene_pos.keys(),0)
    for key, val in gene_pos.items():
        for elem in hits:
            if  val <= (elem + max_dist) and val >= (elem - max_dist):
                hit_count [key] += 1
    return hit_count


if __name__ == "__main__":  # do not remove this line   
    
    # Write your testing code here. This portion will not be marked.
    sites = ["ACGATG","ACAATG","ACGATC","ACGATC","TCGATC",
             "TCGAGC","TAGATC","TAAATC","AAAATC","ACGATA"]
    sequence = "GCAGACTCAGCAGCGACTACAGCGCTACTACAGCGGAGACGATGCGACAAT"
    genes = {"BRCA1":3, "MYC":23, "RUNX": 45}
#sites=["ACGATG","ACAATG","ACGATC","ACGATC","TCGATC",
#"TCGAGC","TAGATC","TAAATC","AAAATC","ACGATA"]
#PFM= build_PFM(sites)
#print(PFM) 

#PFM=[[6,3,3,10,0,1],[0,7,0,0,0,7],[0,0,7,0,1,2],[4,0,0,0,9,0]]
#PWM=get_PWM_from_PFM(PFM,0.1)
#sequence="GCATCGATGGCAGCGACTACAGCGCTACTACAGCGGAGACGATGCGATCGATACAAT"
#print(len(sequence))
#hits=predict_sites(sequence,PWM)
#print(hits)
    
#gene_pos={"BRCA1":3,"MYC":23,"RUNX":45}
#hits=[3,38,43,47]
#gene_hits=count_hits_per_gene(genes,hits,max_dist=10)
#print(gene_hits)
        