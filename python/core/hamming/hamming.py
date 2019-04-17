def distance(strand_a :str, strand_b :str) -> int:
    a_len = len(strand_a)
    b_len = len(strand_b)

    if a_len != b_len:
        raise ValueError("Strand Lenths doesn't match.")
    else:
        distance = 0
        for k in range(a_len):
            if strand_a[k] != strand_b[k]:
                distance += 1
        return distance

