def to_rna(dna_strand):
    result = ""
    if dna_strand == result:
        return(result)
    else:
        in_table = "GCTA"
        out_table = "CGAU"
        return(dna_strand.translate(str.maketrans(in_table, out_table)))
