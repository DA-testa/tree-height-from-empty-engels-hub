#221RDB031

# python3
"""Compute height of arbitrary tree"""
import sys
import threading

class Node:
    """A Node class"""
    def __init__(self, height) -> None:
        self.height = height
        self.children = []


def compute_height(n, parents):
    """A function that creates tree and finds root"""
    #create node array for tree
    nodes = [Node(i) for i in range(n)]
    root = 0
    #assign nodes and find root
    for i in range(n):
        pid=parents[i]
        if pid==-1:
            root=nodes[i]
        else:
            nodes[pid].children.append(nodes[i])
    print(rec(root)+1)
def rec(node):
    """A function that recursively looks for highest node"""
    hmax = 0
    #check for no children
    if not node.children:
        return hmax
    for child in node.children:
        hchild = rec(child)
        if hchild>hmax:
            hmax=hchild
    return hmax+1



def main():
    """Main"""
    # implement input form keyboard and from files
    inp = input()
    if 'F' in inp:
        file_n = input()
        if 'a' in file_n:
            print('invalid file')
            return
        file=open(f"test/{file_n}","r")
        n = int(file.readline().strip())
        nodes =list(map(int,file.readline().strip('\n').split(" ")))
        compute_height(n, nodes)

    elif 'I' in inp:
        n=int(input().strip())
        nodes=list(map(int, input().split()))
        compute_height(n, nodes)


    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))
