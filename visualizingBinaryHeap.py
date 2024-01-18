from binaryHeap import BinaryHeap
import matplotlib.pyplot as plt
import networkx as nx
import math

class MyData:
    """
    サンプルデータクラス
    """
    def __init__(self, i:int, v:float):
        self.i: int = i
        self.v = v
        
    def __str__(self) -> str:
        a: str = f'({self.i}, {self.v})'
        return a
    
    def setValue(self, v:float) -> None:
        self.v: float = v

    def get(self) -> tuple[int,float]:
        a: tuple[int, float] = (self.i, self.v)
        return a
    
    def getValue(self) -> float:
        return self.v

    def getLabel(self) -> int:
        return self.i
 
    def __lt__(self, o:"MyData") -> bool:
        return self.v < o.getValue()
    
    def compareTo(self, o:"MyData") -> float:
        return self.v-o.getValue()

def position2xy(position:dict[str,tuple[float,float]])->tuple[dict[str,float],dict[str,float]]:
    xp = dict()
    yp = dict()
    for v in position.keys():
        x, y = position[v]
        xp[v] = x
        yp[v] = y
    return xp,yp

def constructGraph(bh:BinaryHeap,r=1.)->tuple[nx.DiGraph,dict[str,tuple[float,float]]]:
    """
    Construct a binary tree for the given binary heap

    Parameters
    ---
    bh: Binary Heap
    r: basic separation between node
    """
    n = bh.size()
    nn = math.floor(math.log2(n))# the max depth
    nodeList = list()
    position = dict()
    edgeList = list()

    for i in range(1, n + 1):#Note that the 0th position is empty
        nodeLabel = str(bh.get(i))
        nodeList.append(nodeLabel)
        # Calculate the position of the node
        y = math.floor(math.log2(i))
        x = i % (2**y)
        yy = r * (nn - y)
        rr = r * 2**(nn - y)
        xx=  rr * ((x - 2**y) * 2 + 2**y + 1)
        position[nodeLabel]=(xx, yy)
        # the left daughter
        k = 2 * i
        if k <= n:
            edgeList.append((nodeLabel, str(bh.get(k))))
        # the right daughter
        k += 1
        if k <= n:
            edgeList.append((nodeLabel, str(bh.get(k))))
            
    G = nx.DiGraph()#Directed graph
    G.add_nodes_from(nodeList)
    G.add_edges_from(edgeList)
    xp, yp = position2xy(position)
    nx.set_node_attributes(G, xp, 'x')
    nx.set_node_attributes(G, yp, 'y')
    return G, position

def drawGraph(G,position,font_size=9,node_size=1000,edge_width=1.,
              node_color="c",arrowsize=10):
    """
    Drawing the tree corresponding to the binary heap using matplotlib
    """
    plt.figure(facecolor='white')
    
    nx.draw_networkx_nodes(G, position, node_size=node_size, node_color=node_color)
    nx.draw_networkx_labels(G, position, font_size=font_size)
    nx.draw_networkx_edges(G, position, width=edge_width, arrows=True,
                           arrowsize=arrowsize, node_size=node_size)
    plt.axis('off')
    plt.show()

def toTikz(bh:BinaryHeap[MyData],position:dict[str,tuple],fx=1.,fy=1.) -> str:
    """
    Draw the tree corresponding to the binary heap using tikz
    """
    text = ''
    n = bh.size()
    for k in range(1, n + 1):#Define nodes
        q = bh.get(k)
        if q:
            l = q.getLabel()
            x, y = position[str(q)]
            text += f'\\node[myNode] (N{l}) at ({fx*x},{fy*y}) {{{q}}};\n'

    text += '\n'
    # Connect nodes
    for k in range(1,n + 1):
        p = 0
        q = bh.get(k)
        if q:
            p = q.getLabel()
        # Connect to the left daughter
        j = 2 * k
        if j <= n:
            c = 0
            q = bh.get(j)
            if q:
                c = q.getLabel()
            text += f'\\draw[->] (N{p}) -- (N{c});\n'
        # Connect to the right daughter
        j += 1
        if j <= n:
            c = 0
            q = bh.get(j)
            if q:
                c = q.getLabel()
            text += f'\\draw[->] (N{p}) -- (N{c});\n'
            
    text += '\n'
    # Showing the indexes of nodes
    for k in range(1, n + 1):
        q = bh.get(k)
        if q:
            p = q.getLabel()
            text += f'\\node () at ($(N{p})+(0,0.5)$) {{{k}}};\n'
    return text

if __name__ == '__main__':
    tikz=False
    data0 = [.6,.9,.1,.2,.4,.5,.3,.4,.1,.3,.8,.2]
    data:list[MyData]=list()
    for i in range(len(data0)):
        s = MyData(i + 1, data0[i])
        data.append(s)
        
    bh = BinaryHeap[MyData]()
    for d in data:
        bh.add(d)

    bh.add(MyData(13, .2))
    bh.poll()
    G,position = constructGraph(bh)
    if tikz:
        text = toTikz(bh, position, fx=0.4)
        print(text)
    else:
        drawGraph(G, position)



