﻿# HuffmanCoding_v1
Huffman coding is a lossless data compression algorithm; this algorithm
gets each unique character and the frequency of which they occur. The two characters
with the lowest frequencies are merged and their frequencies combined into a new node;
this is then placed above the previous 2, this is repeated until only one node remains.
This completes the tree of nodes. Huffman coding travels along these node paths applying
0 to left and 1 to right, to represent smaller and larger of the frequencies. These 0 and 1
will represent the binary representation of the character (the huffman codes)
