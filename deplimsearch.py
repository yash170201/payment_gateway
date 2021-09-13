graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':['H','I'],
    'E':['J','K'],
    'F':['L','M'],
    'G':['N','O'],
    'H':[],
    'I':[],
    'J':[],
    'K':[],
    'L':[],
    'M':[],
    'N':[],
    'O':[],
}

def dls(start,goal,path,level,maxD):
    print("\nCurrent level-->",level)
    print("Goal testing for",start)
    path.append(start)
    if start==goal:
        print("goal test successful")
        return path
        print("goal node testing failed")
    if level==maxD:
        return False
    print("\n Expanding the current node",start)
    for child in graph[start]:
        if  dls(child,goal,path,level+1,maxD):
            return path
        path.pop()
    return  False

start='A'
goal=input("enter the goal node to be found")
maxD=int(input("Enter the maximum depth:--"))
path=list()
res=dls(start,goal,path,0,maxD)
if(res):
    print("path to the goal node found")
    print("path",path)
else:
    print("no path available in the given depth limit")


            

    