import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as a3

def getStarposition(fname):
    data=open(fname).readlines()
    solid,node,end,length=0,0,0,len(data)
    ii=0
    iend=[0,0,0]
    for i,line in enumerate(data):
        line=line.lower()
        if '*keyword' in line:
            start=i
            ii=2
        elif '*element_solid' in line:
            iend[ii]=i
            solid=i
            ii=0
        elif '*node' in line:
            iend[ii]=i
            node=i
            ii=1
        elif '*end' in line:
            iend[ii]=i
            ii=2
        elif line.startswith("*"):
            iend[ii]=i
            ii=2
    print iend
    return (solid,node,end,length)

def getStars(fname):
    data=open(fname).readlines()
    num=[]
    for i,line in enumerate(data):
        if (line.startswith("*")):
            num.append((i,line.strip()))
    return num


def plotNodes(nodes):
    ax=a3.Axes3D(plt.figure())
    ax.scatter(nodes[:,1],nodes[:,2],nodes[:,3])
    plt.show()
    


def getElems(fname,start,end):
    elem=np.genfromtxt(fname,invalid_raise=False,delimiter=[8]*10,comments='$',skip_header=start,skip_footer=end)
    return elem[~np.isnan(elem).any(axis=1)]

def getNodes(fname,start,end):
    nodes=np.genfromtxt(fname,skip_header=start,skip_footer=end,delimiter=[8,16,16,16],usecols=[0,1,2,3],comments='$')
    return nodes

def readKfile(fname):
    solid,node,end,length=getStarposition(fname)
    if solid <node:
        elem=getElems(fname,solid+1,length-node)
        nodes=getNodes(fname,node+1,1)
    else:
        elem=getElems(fname,solid+1,1)
        nodes=getNodes(fname,node+1,length-solid)
    return elem,nodes
    
if __name__ =='__main__':
    fname='target_mesh.k'
    solid,node,end,length=getStarposition(fname)
    elem=getElems(fname,solid+1,length-node)
    nodes=getNodes(fname,node+1,1)
    

#a[~np.isnan(a).any(axis=1)]
