from huffman import HuffmanTree
from graph import print_tree

if __name__ == '__main__':
    text = "Huffman coding is a lossless data compression algorithm"
    t = HuffmanTree(text)
    print_tree(t.root)

    encodedText = t.encode(text)
    print(encodedText)
    print(t.decode(encodedText))
