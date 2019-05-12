def distance(strand_a :str, strand_b :str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Strand Lenths doesn't match.")
    return len([(s1, s2) for s1, s2 in zip(strand_a, strand_b) if s1 != s2])
