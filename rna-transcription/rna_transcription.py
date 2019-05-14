def to_rna(dna_strand):
    result = ""
    if dna_strand == result:
        return(result)
    else:
        for i in dna_strand:
            if i == "A":
                result += "U"
            if i == "T":
                result += "A"
            if i == "C":
                result += "G"
            if i == "G":
                result += "C"
        return(result)
