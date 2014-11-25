__author__ = 'duansy'
def distance(vec1, vec2):
    derVec1=normalize(derivative(vec1))
    derVec2=normalize(derivative(vec2))
    minDist=curDistance(derVec1,derVec2)
    for i in range(0,max(len(derVec1),len(derVec2))-1):
        derVec1=shiftRight(derVec1)
        newMin=curDistance(derVec1,derVec2)
        if newMin<minDist:
            minDist=newMin
    return minDist
def normalize(vec):
    out=[0]*(len(vec))
    dist=0
    for i in range(1,len(vec)):
        dist+=vec[i]**2
    total=dist**.5
    if total==0:
        return vec
    for i in range(1,len(vec)):
        out[i]=vec[i]/total
    return out
def derivative(vec):
    out=[0]*(len(vec)-1)
    for i in range(1,len(vec)):
        out[i-1]=vec[i]-vec[i-1]
    return out
def curDistance(vec1,vec2):
    dist=0
    for i in range(0,min(len(vec1),len(vec2))):
        dist+=(vec1[i]-vec2[i])**2
    return dist
def shiftRight(vec1):
    vec1.insert(0,vec1.pop())
    return vec1

class truthEntry:
    def __init__(self,vec,label):
        self.label=label
        self.vec=vec


vec1=[1]*101
vec2=[1]*101
vec3=[1]*101
vec4=[1]*101
for i in range(-50,51):
    vec1[i+50]=100*(i-40)**2
for i in range(-50,51):
    vec2[i+50]=i
for i in range(-50,51):
    vec3[i+50]=1.1**i
for i in range(-50,51):
    vec4[i+50]=5*(i-6)**2+4


truthEntries=[]

truthEntries.append(truthEntry(vec1,'square'))
truthEntries.append(truthEntry(vec2,'linear'))
truthEntries.append(truthEntry(vec3,'exponential'))

minDist=999999999
label='none'
for entry in truthEntries:
    newDist=distance(vec4,entry.vec)
    print newDist
    if newDist<minDist:
        minDist=newDist
        label=entry.label

print label
