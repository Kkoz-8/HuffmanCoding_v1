"""Huffman coding is a lossless data compression algorithm; this algorithm
gets each unique character and the frequency of which they occur. The two characters
with the lowest frequencies are merged and their frequencies combined into a new node;
this is then placed above the previous 2, this is repeated until only one node remains.
This completes the tree of nodes. Huffman coding travels along these node paths applying
0 to left and 1 to right, to represent smaller and larger of the frequencies. These 0 and 1
will represent the binary representation of the character (the huffman codes)"""

"""Time complexity of Huffman Algorithm is O(nlogn)"""

#dictionary for characters and their frequency
data_dict = {}

#list to be used to do...many things
data_list = []

#dummy data
dummy_data = "HUFFMAN ALGORITHM WITH PYTHON"

class HuffmanNode:
    """class to create huffman tree nodes"""

    def __init__(self, left = None, right = None):
        """constructor attributes"""
        self.left = left #used to traverse left lower nodes of two lowest values
        self.right = right #used to traverse right higher value of two lowest values

    def __str__(self):
        """represent the class object as string"""
        return f"{self.left}_{self.right}"


def huff_coding(node_or_char, string = ""):
    """huffman function to traverse the nodes and build the binary representation for traversed path"""
    
    #if statement code block will be run when we hit a string value; nodes data type ignored
    if type(node_or_char) is str:
        #returns the character as key, and concatenated binary huffman code as value
        return {node_or_char: string}

    #variables to access left and right data values of node
    left, right = node_or_char.left, node_or_char.right
    
    #dictionary to store characters with their respective huffman coding
    huff_dict = {}

    huff_dict.update(huff_coding(left, string + "0")) #pass in node/char and concatenate "0" to string for left side of tree
    huff_dict.update(huff_coding(right, string + "1")) #pass in node/char and concatenate "1" to string, for right side of tree
    
    return huff_dict #dictionary of characters with their huffman coding


def huff_tree(sorted_list):
    while len(sorted_list) > 1:
        char, freq = sorted_list[0][0], sorted_list[0][1] #gets char and freq of list at index 0
        char2, freq2 = sorted_list[1][0], sorted_list[1][1] #gets char and freq of list at index 1
  
        sorted_list = sorted_list[2:] #keep excluding first 2 items(lists) in outer list

        #create node from the 2 minimum chars
        node = HuffmanNode(char, char2)
        #insert this node into list
        sorted_list.insert(0, [node, freq + freq2])

        #call function "bubble_sort()"
        bubble_sort(sorted_list)

    return sorted_list #finally return list of the final node combination


def freq(string_data):
    """store and counts characters from string to dictionary"""
    for char in string_data:
        if char not in data_dict: #first encounter with char set value to 1
            data_dict[char] = 1
        else:
            data_dict[char] += 1 #every recurring encounter with char increment value by 1


#function to create a list of lists from dictionary for sorting
def create_list(dict_input):
    """create list of lists from dictionary"""
    for key, value in dict_input.items():
        data_list.append([key, value])


#bubble sort function, complexity of O(n^2)
def bubble_sort(unsorted_list):
    """bubble sort to sort list of lists by second value in ascending order"""
    for index in range(len(unsorted_list)):
        #outer loop to run inner loop as many times as length of list
        for index2 in range(len(unsorted_list) - 1):
            #inner loop bubbles each largest number to end
            if unsorted_list[index2][1] > unsorted_list[index2 + 1][1]:
                unsorted_list[index2][0], unsorted_list[index2 + 1][0] = unsorted_list[index2 + 1][0], unsorted_list[index2][0]
                unsorted_list[index2][1], unsorted_list[index2 + 1][1] = unsorted_list[index2 + 1][1], unsorted_list[index2][1]


#function calls
freq(dummy_data) #prep dictionary with frequency
create_list(data_dict) #prep list of lists
bubble_sort(data_list) #initial sort on list to have it be in ascending order

print("\nThe dummy data used for testing:\n",dummy_data)
print("\nNested list of chars, sorted in ascending via frequency\n",data_list)

#create huffman tree of nodes
hufftree_nodes = huff_tree(data_list)

print("\nFinal HuffmanNode:\n",hufftree_nodes[0][0])

#Apply huffman coding to huffman nodes
huffman_coding = huff_coding(hufftree_nodes[0][0])

print("""\nSee below for char with its corresponding huffman code
------------------------------------------------------""")
for key, value in huffman_coding.items():
    print((key, value))