from justins_ds_and_algos.graph import BinaryNode
from justins_ds_and_algos.queue import PriorityQueue

class HuffmanCode:
    def __init__(self, freq, symbol=None):
        self.freq = freq
        self.symbol = symbol

    def __repr__(self):
        return "({}, {})".format(self.symbol, self.freq)

def getHuffmanCodes(text):
    freqs = dict()
    for c in text:
        if c in freqs:
            freqs[c] += 1
        else:
            freqs[c] = 1
    huffmanCodes = [BinaryNode(HuffmanCode(f, s)) for s, f in freqs.iteritems()]
    return PriorityQueue(huffmanCodes, key=lambda x: x.value.freq)

class HuffmanTree:
    def __init__(self, text):
        self.__text = text
        pQueue = getHuffmanCodes(text)
        self.root = HuffmanTree.buildTree(pQueue)

        self.encodings = dict()

    @staticmethod
    def buildTree(pQueue):
        if len(pQueue) == 0:
            raise Exception("Cannot build huffman tree from zero length string")
        root = None

        while len(pQueue) > 1:
            l = pQueue.dequeue()
            r = pQueue.dequeue()
            p = HuffmanCode(l.value.freq + r.value.freq)
            root = BinaryNode(p, l, r)
            pQueue.enqueue(root)

        return root

    def encodeSymbol(self, symbol):
        if symbol in self.encodings:
            return self.encodings[symbol]

        stack = [(self.root, "")]
        while len(stack) > 0:
            stack, (n, encoding) = stack[:-1], stack[-1]
            if n.value.symbol:
                self.encodings[n.value.symbol] = encoding

            if n.value.symbol == symbol:
                return encoding

            if n.getLeft():
                stack.append((n.getLeft(), encoding + "0"))
            
            if n.getRight():
                stack.append((n.getRight(), encoding + "1"))

        raise Exception("Symbol not found in encoding")

    def encode(self, text):
        return "".join([self.encodeSymbol(s) for s in text])

    def decode(self, text):
        decoded = []

        n = self.root
        for s in text:
            if s == '1':
                n = n.getRight()
            else:
                n = n.getLeft()

            if n.isLeaf():
                decoded.append(n.value.symbol)
                n = self.root

        return "".join(decoded)
