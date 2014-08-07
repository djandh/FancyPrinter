
import sys


def slack(i,j):
    word_lengths=map(len, words[i:j+1])
    s=max_len-sum(word_lengths)-(j-i)
    if s < 0:
        return float('inf') 
    else:
        return s



def compute_OPT(OPT):
    for j in range(1,len(OPT)):
        OPT[j]=min(slack(i,j-1)**2+OPT[i] for i in range(0,j))
    return OPT



def aux_part(j, linebreaks):
    r=range(j-1,-1,-1)
    for i in r:
        if OPT[j]==OPT[i]+slack(i,j-1)**2:
            if i==0:
                return linebreaks
            linebreaks.insert(0,i-1)
            return aux_part(i,linebreaks)


def partition():
    return aux_part(len(words), [])


def format():
    formatted = ""
    for i in range(len(words)):
        formatted += words[i]+' '
        if i in linebreaks:
            formatted += '\n'
    return formatted


filename = sys.argv[1]
f = open(filename)
text = f.read()
words = text.split()

max_len=50
OPT = compute_OPT([0]*(len(words)+1))
linebreaks = partition()
formatted = format()
print(formatted)




