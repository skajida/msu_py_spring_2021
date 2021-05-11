def merge_sort(iterable, batch_size=2):
    iterable = list(iterable)
    if (len(iterable) <= batch_size >> 1):
        return
    for i in range((len(iterable) + batch_size - 1) // batch_size):
        source = iterable[i * batch_size:(i + 1) * batch_size]
        separator, size = batch_size >> 1, len(source)
        if (size < separator):
            break
        idx_left, idx_right = 0, separator
        while idx_left + idx_right < size + separator:
            idx = i * batch_size + idx_left + idx_right - separator
            if idx_right == size or idx_left < separator and source[idx_left] < source[idx_right]:
                iterable[idx] = source[idx_left]
                idx_left += 1
            else:
                iterable[idx] = source[idx_right]
                idx_right += 1
    yield iterable
    yield from merge_sort(iterable, batch_size << 1)
