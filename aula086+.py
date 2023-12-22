class Quadrado(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
       for i in range(self.start+1, self.end+1):
           yield i**2

n = Quadrado(0, 5)
print(list(n))
