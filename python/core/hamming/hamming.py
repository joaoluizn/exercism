def distance(strand_a :str, strand_b :str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Strand Lenths doesn't match.")
    else:
        return len([k for k in zip(strand_a, strand_b) if k[0] != k[1]])
