def to_rna(dna_strand):
    """
    :param str dna_strand: Strand DNA to be converted to RNA
    :rtype: str
    """
    response = []
    for e in list(dna_strand):
        if e == 'C':
            response.append('G') 
        elif e == 'G':
            response.append('C')
        elif e == 'T':
            response.append('A')
        elif e == 'A':
            response.append('U')
    return ''.join(response)
