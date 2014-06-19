
"""
Dynamic programming algorithm for typesetting. Minimizes "squared slack norm"
and stores the result which can be printed or written to a file.
author: Jon Hagg

"""

import sys

class typeset(object):
    
    """
    Initialization: splits input into array of words delimited
    by whitespace, runs the DP algorithm, and creates formatted 
    text.
    """

    def __init__(self, input, MAX_LEN=50):

        self.words=input.split()
        self.MAX_LEN=MAX_LEN
        self.OPT=[0]*(len(self.words)+1)
        self.linebreaks=[]
        self._compute_OPT()    
        self.formatted=''
        self._partition()
        self._format()

    def _slack(self,i,j):
        word_lengths=map(len, self.words[i:j+1])
        s=self.MAX_LEN-sum(word_lengths)-(j-i)
        if s < 0:
            return float('inf') 
        else:
            return s


    def _compute_OPT(self):
        for j in range(1,len(self.OPT)):
            self.OPT[j]=min(self._slack(i,j-1)**2+self.OPT[i] for i in range(0,j))
	
	
    def _aux_part(self, j, linebreaks):
        r=range(0,j)
        r.reverse()
        for i in r:
            if self.OPT[j]==self.OPT[i]+self._slack(i,j-1)**2:
                if i==0:
                    return linebreaks
                linebreaks.insert(0,i-1)
                return self._aux_part(i,linebreaks)
	

    def _partition(self):
        self.linebreaks=self._aux_part(len(self.words), [])


    def _format(self):
        for i in range(len(self.words)):
            self.formatted += self.words[i]+' '
            if i in self.linebreaks:
                self.formatted += '\n'
    

    def display(self):
	print(self.formatted)  


    def write(self, file):
        with open(file, 'w') as f:
            f.write(self.formatted)
            f.close()        


if __name__=='__main__':

    FILE=sys.argv[1]
    f=open(FILE)
    TEXT=f.read()
    t=typeset(TEXT)
    t.display()
    t.write('output.txt')





