import time,functools
@functools.lru_cache(maxsize=3)
def fibbo(n):
    time.sleep(n)
    return n

print(fibbo(3))
print(fibbo(3))
print(fibbo(3))
