class Quadrado(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.end:
            self.start += 1
            return self.start**2
        else:
            raise StopIteration

n = Quadrado(0, 5)
n.__next__()
print(list(n))
