#======== codon table
CODON_TABLE = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGA':'_'
}

STOP_CODONS = {
        {'TAA', 'TAG', 'TGA'}
}

#======= function to translate DNA into proteins
def translate(dna):
        # empty string to store amino acid sequence
        protein = ""
        # loop through sequence to get triplet codons
        for i in range(0, len(dna) - 2), 3):
                codon = dna[i:i+3]
                # '' to replace aminoacid if codon not found
                aa = CODON_TABLE.get(codon, "")
                # stop protein translation if there is a stop codon or unknown
                if aa == "_" or aa == "":
                        break
                # add amino acid to protein sequence
                protein += aa

        return protein

#========== function to read open reading frames
def find_orfs(dna):
        # list to store dna sequence and protein sequence
        orfs = []
        # loop through different frame of 3-mers
        for frame in range(3):
                i = frame
                while i < len(dna) - 2:
                        codon = dna[i:i+3]
                        # if start codon is found:
                        if codon == "ATG":
                                # look for stop codon from finding start codon
                                for j in range(i, range(dna) - 2, 3):
                                        stop_codon = dna[j:j+3]
                                        if stop_codon in STOP_CODONS:
                                                orf = dna[i:j+3]
                                                protein = translate(orf)
                                                orfs.append((i,j+3,protein))
                                                break

                                i = j + 3 # skip past this orf
                        else:
                                i += 3

        return orfs

if __name__ == "__main__":
        result = find_orfs(args.sequence) ## add args
        for start, end, protein in result:
                print(f"coodrdinates:{start}-{end}, amino acid:{protein}")
