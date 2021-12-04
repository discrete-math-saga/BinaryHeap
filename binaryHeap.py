class BinaryHeap:
    """
    Binary Heap
    """
    def __init__(self):
        """
        コンストラクタ
        """
        self._members = [None]
        self._n = 0
    
    def __str__(self):
        """
        文字列化
        """
        text = ""
        for i in range(1, self._n + 1):
            a = self._members[i]
            text += f'{i}:{a}\n'
        return text

    def add(self, o):
        """
        要素の追加

        Parameters
        ---
        o 追加する要素
        """
        self._members.append(o)
        self._n += 1
        self._shiftUp(self._n)
        
    def _shiftUp(self, k:int):
        """
        指定した位置の要素をシフトアップ

        Parameters
        ---
        k 要素の位置
        """
        kk = int(k/2)
        if (k > 1) and self._isLess(k, kk):
            self._swap(k, kk)
            k = kk
            self._shiftUp(k)
        
    def poll(self):
        """
        最小要素を取り出す。取り出した要素は削除される

        Returns
        ---
        取り出した最小要素

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
    
    def _shiftDown(self, k:int):
        """
        指定した位置の要素をシフトダウン

        Parameters
        ---
        k 要素の位置
        """
        if 2*k <= self._n:
            j = 2 * k
            if j < self._n and self._isLess(j + 1,j):
                j += 1
            if self._isLess(k, j):
                return
            self._swap(k, j)
            self._shiftDown(j)
    
    def reduceValue(self, o):
        """
        値が減少した要素を指定する

        Parameters
        ---
        o 指定する要素
        """
        k = self._members.index(o)
        self._shiftUp(k)
        
    def raiseValue(self, o):
        """
        値が増加した要素を指定する

        Parameters
        ---
        o 指定する要素
        """
        k = self._members.index(o)
        self._shiftDown(k)
        

    def size(self) ->int:
        """
        要素数を返す

        Returns
        ---
        要素数
        """
        return self._n

    def get(self, k:int):
        """
        指定された位置の要素を返す

        Parameters
        ---
        k 位置の指定
        """
        if k < 1 or k > self._n:
            return None
        return self._members[k]

    def _isLess(self, i:int, j:int):
        io=self._members[i]
        jo=self._members[j]
        return (io < jo)
    
    def _swap(self, i:int, j:int):
        t = self._members[i]
        self._members[i]=self._members[j]
        self._members[j]=t
        
