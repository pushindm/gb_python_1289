class Iterator:
    start = 0
    def __init__(self, md_list):
        self.md_list = md_list
        self.end = len(md_list)
        self.i = Iterator.start - 1
    
    def __next__(self):
        self.i += 1
        if self.i < self.end: 
            return self.md_list[self.i]
        else: 
            raise StopIteration

class Matrix:
    def __init__(self, md_list):
        self.md_list = md_list
    
    def __str__(self):
        return '\n'.join([''.join(['{:4}'.format(el) for el in row]) for row in self.md_list]) # row with breaklines

    def __add__(self, other):
        return Matrix([[i+j for i,j in zip(r1,r2)] for r1,r2 in zip(self.md_list, other)])
    
    def __iter__(self):
        return Iterator(self.md_list)

b = Matrix([[1,2,3], [3,4,5],[6,7,8]])
c = Matrix([[1,2,3], [3,4,5],[6,7,8]])
print(b+c)
