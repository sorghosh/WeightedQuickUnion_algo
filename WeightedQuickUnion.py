class WeightedQuickUnion:

    def __init__(self,n):
        self.id  = [i for i in range(0,n)]
        self.sz  = [1] * n
    def union(self,i,y):
        x = self.root(i)
        y = self.root(y)
        if self.sz[x] < self.sz[y]:
            self.id[x] = y
            self.sz[x] = self.sz[x] + self.sz[y]
        else:
            self.id[x] = y
            self.sz[x] = self.sz[x] + self.sz[y]
            
    def connected(self,i,j):
        return self.root(self.id[i]) == self.root(self.id[j])
    
    def root(self,i):
        while(i != self.id[i]):
            i = self.id[i]
        return i
        
    def print_result(self):
        print self.id


obj = WeightedQuickUnion(10)
obj.print_result()
obj.union(4,3)
obj.print_result()

obj.union(3,8)
obj.print_result()


obj.union(6,5)
obj.print_result()

obj.union(9,4)
obj.print_result()

obj.union(2,1)
obj.print_result()

obj.union(5,0)
obj.print_result()

obj.union(7,2)
obj.print_result()

obj.union(6,1)
obj.print_result()

obj.union(7,3)
obj.print_result()    
    
print obj.connected(3,0)
