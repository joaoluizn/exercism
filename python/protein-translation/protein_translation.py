from textwrap import wrap

def proteins(strand):
    """
    :param str strand: Given strand to classify proteins
    :rtype: list
    """
    # first implementation
    # codons = [strand[i*3:3*(i+1)] for i in range(int(len(strand)/3))]    
    
    # clever approach
    codons = wrap(strand, 3)
    
    proteins = {
        'Methionine':['AUG'],
        'Phenylalanine': ['UUU', 'UUC'], 
        'Leucine': ['UUA', 'UUG'], 
        'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
        'Tyrosine': ['UAU', 'UAC'],
        'Cysteine': ['UGU', 'UGC'], 
        'Tryptophan': ['UGG'],
        'STOP': ['UAA', 'UAG', 'UGA']}

    response = []
    for k in codons:
        for group in proteins.items():
            if k in group[1]:
                if group[0] != 'STOP':
                    response.append(group[0])
                else:
                    return response
    return response
