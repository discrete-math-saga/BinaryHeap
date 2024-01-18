import sys
from binaryHeap import BinaryHeap

class MyData:
    """
    例題用のクラス
    """
    def __init__(self, i:int, v:float):
        self.i = i
        self.v = v
        
    def __lt__(self, o:'MyData') -> bool:
        return self.v < o.getValue()

    def __str__(self) -> str:
        return f'({self.i}, {self.v})'
    
    def setValue(self, v:float) -> None:
        self.v = v

    def get(self) -> tuple[int,float]:
        return (self.i, self.v)
    
    def getValue(self) -> float:
        return self.v

if __name__ == '__main__':
    data0 = [
        .6, .9, .1, .2, .4, .5, .3, .4, .1, .3, .8, .2
        ]
    data:list[MyData] = list()
    for i in range(len(data0)):
        s = MyData(i + 1,data0[i])
        data.append(s)
        
    bh = BinaryHeap[MyData]()
    for d in data:
        bh.add(d)
        
    #要素の追加
    bh.add(MyData(13, .2))
    print(bh)

    #最小要素の取り出し
    bh.poll()
    print(bh)

    #4番目に入れたデータを探す
    x = None
    for d in data:
        (i, v)=d.get()
        if i == 4:
            x = d

    #4番目に入れたデータの値を0.2に変更する
    if x:
        x.setValue(0.2)
        bh.raiseValue(x)
        print(bh)
