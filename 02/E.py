def chain_loop(args):
    available = list(map(bool, args))
    args = list(map(iter, args))
    while any(available):
        for i in range(len(available)):
            if available[i]:
                try:
                    yield next(args[i])
                except StopIteration:
                    available[i] = False
