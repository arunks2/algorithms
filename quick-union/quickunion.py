class QuickUnionUF:

    def __init__(self,n):
        self.N = n
        self.id = [i for i in range(0,self.N)]

    def __repr__(self):
        return self.id

    def root(self, x):
        while(x != self.id[x]):
            x = self.id[x]
        return x

    def isConnected(self, x, y):
        return self.root(x) == self.root(y)

    def union(self,x, y):
        x1 = self.root(x)
        y1 = self.root(y)
        self.id[x1] = y1
        return


if __name__ == "__main__":
    file = open("quickUnion.txt","r+")  
    N = int(file.readline())
    QU = QuickUnionUF(N)
    values = file.readlines()
    count = 0
    for value in values:
        if value.strip() == 'unionendshere':
            break
        n,k = value.strip().split(' ')
        n,k = [int(n),int(k)]
        QU.union(n,k)
        count += 1
    for i in range(count+1,len(values)):
        if values[i].strip() == 'findsendshere':
            break
        n,k = values[i].strip().split(' ')
        n,k = [int(n),int(k)]
        print(QU.isConnected(n,k))