import random
from copy import deepcopy
class Matrix:
    def __init__(self, nrowsA, ncolsA,nrowsB,ncolsB):
        """Construct a (nrows X ncols) matrix"""
        A=[]
        B=[]
        self.nrowsA=nrowsA
        self.ncolsA=ncolsA
        self.nrowsB=nrowsB
        self.ncolsB=ncolsB       
        for i in range(0,self.nrowsA):
            A.append([])
            for j in range(0,self.ncolsA):
                A[i].append(random.randint(0,9))
        print("Enter A matrix's rows : "+str(nrowsA),"Enter A matrix's clos : "+str(ncolsA),'Matrix A'+str((nrowsA,ncolsA))+':',sep='\n')
        for i in range(0,self.nrowsA):
            for j in range(0,self.ncolsA):
                print(A[i][j],end=' ')
            print('')
        print('')
        for i in range(0,self.nrowsB):
            B.append([])
            for j in range(0,self.ncolsB):
                B[i].append(random.randint(0,9))
        print("Enter B matrix's rows : "+str(nrowsB),"Enter B matrix's clos : "+str(ncolsB),'Matrix B'+str((nrowsB,ncolsB))+':',sep='\n')
        for i in range(0,self.nrowsB):
            for j in range(0,self.ncolsB):
                print(B[i][j],end=' ')
            print('')
        print('')
        self.A=A
        self.B=B
        pass
    def add(self, m):
        """return a new Matrix object after summation"""
        C=[]
        if self.nrowsA==self.nrowsB and self.ncolsA==self.ncolsB:
            for i in range(0,self.nrowsA):
                C.append([])
                for j in range(0,self.ncolsA):
                    C[i].append(self.A[i][j]+self.B[i][j])
        self.C=C
        pass
    def sub(self, m):
        """return a new Matrix object after substraction"""
        D=[]
        if self.nrowsA==self.nrowsB and self.ncolsA==self.ncolsB:
            for i in range(0,self.nrowsA):
                D.append([])
                for j in range(0,self.ncolsA):
                    D[i].append(self.A[i][j]-self.B[i][j])
            self.D=D
        pass
    def mul(self, m):
        """return a new Matrix object after multiplication"""
        E=[]
        if self.nrowsA==self.ncolsB and self.ncolsA==self.nrowsB:
            for i in range(0,self.nrowsA):
                E.append([])
                for j in range(0,self.ncolsB):
                    E[i].append(0)
                    for k in range(0,self.ncolsA):
                        E[i][j]+=self.A[i][k]*self.B[k][j]
        self.E=E
        pass
    def transpose(self):
        """return a new Matrix object after transpose"""
        F=[]
        if self.nrowsA==self.ncolsB and self.ncolsA==self.nrowsB:
            for i in range(0,self.nrowsA):
                F.append([])
                for j in range(0,self.ncolsB):
                    F[i].append(self.E[j][i])
        self.F=F
        pass
    def display(self):
        """Display the content in the matrix"""
        print('========== A + B ==========')
        if self.nrowsA==self.nrowsB and self.ncolsA==self.ncolsB:
            for i in range(0,self.nrowsA):
                for j in range(0,self.ncolsA):
                    print(self.C[i][j],end=' ')
                print('')
            print('')
        else:
            print("Matrixs' size should be in the same size.")      
        print('========== A - B ==========')
        if self.nrowsA==self.nrowsB and self.ncolsA==self.ncolsB:
            for i in range(0,self.nrowsA):
                for j in range(0,self.ncolsA):
                    print(self.D[i][j],end=' ')
                print('')
            print('')
        else:
            print("Matrixs' size should be in the same size.") 
        print('========== A * B ==========')
        if self.nrowsA==self.ncolsB and self.ncolsA==self.nrowsB:
            for i in range(0,self.nrowsA):
                for j in range(0,self.ncolsB):
                    print(self.E[i][j],end=' ')
                print('')
            print('')
        else:
            print("Matrixs' size should be in the same size.") 
        print('= the transpose of A * B ==')
        if self.nrowsA==self.ncolsB and self.ncolsA==self.nrowsB:
            for i in range(0,self.nrowsA):
                for j in range(0,self.ncolsB):
                    print(self.F[i][j],end=' ')
                print('')
        else:
            print("Matrixs' size should be in the same size.") 
        pass
C=Matrix(6,5,6,5)
C.add(1)
C.sub(1)
C.mul(1)
C.transpose()
C.display()