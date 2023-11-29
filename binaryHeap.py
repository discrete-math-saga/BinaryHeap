from typing import Any

class BinaryHeap:
    """
    Binary Heap
    """
    def __init__(self):
        """
        Constructor
        """
        self._members = [None]#Zeroth position
        self._n = 0
    
    def __str__(self) -> str:
        """
        Converting this object into a string
        """
        text = ""
        for i in range(1, self._n + 1):
            a = self._members[i]
            text += f'{i}:{a}\n'
        return text

    def add(self, o:Any) -> None:
        """
        Add an element to this binary heap

        Parameters
        ---
        o: an element to be added
        """
        self._members.append(o)
        self._n += 1
        self._shiftUp(self._n)
        
    def _shiftUp(self, k:int) -> None:
        """
        Shift up the element specified by the position

        Parameters
        ---
        k: the position of the element to be shifted up
        """
        kk = k // 2
        if (k > 1) and self._isLess(k, kk):
            self._swap(k, kk)
            k = kk
            self._shiftUp(k)
        
    def poll(self) -> Any:
        """
        Extract the minimum element. The extracted element will be removed from this binary heap.

        Returns
        ---
        The minimum element of this binary heap

        """
        t = self._members[1]
        x = self._members.pop()
        if len(self._members) > 1:
            self._members[1] = x
        else:
            self._members.append(x)
        self._n -= 1
        self._shiftDown(1)
        return t
    
    def _shiftDown(self, k:int) -> None:
        """
        Shift down the element specified by the position

        Parameters
        ---
        k: the position of the element to be shifted down
        """
        if 2*k <= self._n:
            j = 2 * k
            if j < self._n and self._isLess(j + 1,j):
                j += 1
            if self._isLess(k, j):
                return
            self._swap(k, j)
            self._shiftDown(j)
    
    def reduceValue(self, o:Any) -> None:
        """
        Specify the element whose value is decreased, and is shifted up

        Parameters
        ---
        o: the element to be specified
        """
        k = self._members.index(o)
        self._shiftUp(k)
        
    def raiseValue(self, o:Any) -> None:
        """
        Specify the element whose value is increased, and is shifted down
        Parameters
        ---
        o: the element to be specified
        """
        k = self._members.index(o)
        self._shiftDown(k)
        

    def size(self) ->int:
        """
        Return the number of elements included in this binary heap

        """
        return self._n

    def get(self, k:int) -> Any:
        """
        Return the element at the specified position

        """
        if k < 1 or k > self._n:
            return None
        return self._members[k]

    def _isLess(self, i:int, j:int) -> bool:
        io=self._members[i]
        jo=self._members[j]
        return (io < jo)# type: ignore
    
    def _swap(self, i:int, j:int) -> None:
        t = self._members[i]
        self._members[i]=self._members[j]
        self._members[j]=t
        
