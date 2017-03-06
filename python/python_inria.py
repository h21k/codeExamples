from scipy.stats import genextreme

def fitGenExtreme(data, target=0.0):
    best = (float('inf'),)
    for sz in range(10, len(data)//4, 10):
        bm = blockMaxima(data, sz)
        try:
            params = genextreme.fit(bm)
            if best[0] > abs(params[0] - target):
                best = (params[0] - target, params)
        except ZeroDivisionError:
            break
    return best[1]
