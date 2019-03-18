def slices(series, length):
    if length == 0:
        raise ValueError("Length can't be 0.")
    elif len(series) < length:
        raise ValueError("Serie is too short.")
    elif length < 0:
        raise ValueError("Length can't be negative.")

    step = 0
    slices_ = []
    while True:
        wrapped = series[step:][:length]
        if len(wrapped) == length:
            slices_.append(wrapped)
            step += 1
        else:
            break

    return slices_
