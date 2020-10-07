# Jordy Mukania
# ECE 241 Project #1 Main Class
# Oct 3, 2020

# Need to import random number generator and Time to keep time
import random
import time


# TASK 1A City Class
class City:  # City Class

    def __init__(self, cityData):  # Initiates city object
        # Variables needed to set up attributes
        city = cityData.split(',')  # Delimiter (,) to split each cell in CSV file into array
        city_and_state = city[1]  # Array for city & and state in case to split more
        csSplit = city_and_state.split()  # Splits city and state into array
        state_Index = len(csSplit) - 1  # Index for state

        # Variables for City
        self.cid = city[0]  # City ID
        self.cname = ' '.join(csSplit[0:state_Index])  # City Name... Joins Name if more than one in array
        self.cstate = csSplit[state_Index]  # State name of city
        self.pop = city[2]  # Population of city
        self.cities = city[4:]  # Array w COVID data of confirmed cases for city

    def __str__(self):  # String that prints cid, cname, cstate and most recent confirmed cases for city object print
        return "cid: " + self.cid + "; cname: " + str(self.cname) + "; cstate: " + self.cstate + "; cases:" \
               + self.cities[len(self.cities) - 1]


# TASK 1B COV19 Library Class
class COV19Library:  # COVID 19 library class

    def __init__(self):  # Initiates library object for COV19 city data
        self.size = 0  # Makes size auto zero
        self.isSorted = False  # Not sorted upon initiation
        self.cityArray = list()  # City array to store cities in library
        self.root = None  # Root of BST
        self.cityBST = None  # BST list of Cities

    def length(self):  # Returns how many cities added in library
        return self.size

    # TASK 2 Load Data
    def LoadData(self, filename):  # Function that loads CSV data
        csvFile = open(filename, 'r')  # File name to read
        for line in csvFile:  # Reads rows into City Array
            current_city = City(line)
            self.cityArray.append(current_city)  # Appends CSV file into CityList
            self.size += 1  # Increases size the more we add
        self.cityArray.pop(0)  # Removes first row of header titles
        self.size -= 1

    # TASK 3 Linear Search
    def linearSearch(self, city_name, attribute):  # Linearly searches to find city attributes of chosen city

        i = 0  # Starting position checking for cities
        found = False  # Boolean to check if city found

        while i < len(self.cityArray) and not found:  # While loop going through city List checking if city exists
            city = self.cityArray[i]
            i += 1
            if city.cname == city_name or city.cid == city_name:  # If city found, found = true and continue
                found = True

        if found is not True:  # If not found then return city not found
            return "City not found"
        else:
            return str(city)  # If found then return attributes

    # TASK 4 Quicksort
    def quickSort(self):  # Quick sort function to sort cities in alphabetical/ID order

        self.quickSortHelper(self.cityArray, 0, len(self.cityArray) - 1)  # Quick sort helper function
        self.isSorted = True  # After sorting, change variable so user knows it's sorted

    def quickSortHelper(self, alist, first, last):  # Helps sort by using recursion

        if first < last:  # Checks if we need to keep splitting

            splitpoint = self.partition(alist, first, last)  # Recursively partition list to find new split-point
            self.quickSortHelper(alist, first, splitpoint - 1)  # Recursively splits left side of split-point
            self.quickSortHelper(alist, splitpoint + 1, last)  # Recursively splits right side of split-point

    def partition(self, alist, first, last):  # Finds where to split list

        pivotvalue = alist[first]  # Make pivot value first index of  array we have

        # Marks used to find pivot values
        leftmark = first + 1
        rightmark = last

        done = False  # Checks to see if pivot value found
        while not done:

            # Loop going through checking if left mark needs to be moved
            while leftmark <= rightmark and alist[leftmark].cid <= pivotvalue.cid:
                leftmark = leftmark + 1

            # Loop going through checking if right mark needs to be moved
            while alist[rightmark].cid >= pivotvalue.cid and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:  # Means pivot value found so we're done
                done = True
            else:  # If not true... Flip L and R elements and continue. Means no pivot value found yet
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        temp = alist[first]  # Flip pivot value w split-point then exit and continue
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark  # Returns split point

    # TASK 5 Balanced BST Tree
    def buildBST(self):  # Builds balanced BST of cities by CityID

        self.cityBST = AvlTree()  # Make cityBST = AVL Tree
        # Loop adding cities into AVL tree
        i = 0
        while i < len(self.cityArray):     # Goes whole length of city array
            city = self.cityArray[i]
            self.cityBST[city.cid] = city  # Key = cid, value = City Objects
            i += 1                         # Increment iterator and continue

        self.root = self.cityBST.root  # Makes root of COV19Library root same as BST root

    # TASK 6 BST Search
    def searchBST(self, cid):
        city = self.cityBST[cid]  # Gives city object based on cid
        if city is None:  # If no city found then return not found
            return 'City not found'
        else:  # Else return string of city
            return str(city)


class TreeNode:  # Used to store information and keep track of tree information
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:  # Used to make Binary Search Tree

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self, currentNode):
        if currentNode.isLeaf():  # leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


class AvlTree(BinarySearchTree):  # Used to make balanced binary search tree
    '''An extension t the BinarySearchTree data structure which
    strives to keep itself balanced '''

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(
            newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(
            rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot):
        newRoot = rotRoot.leftChild

        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
            else:
                rotRoot.parent.leftChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(rotRoot.balanceFactor, 0)

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)


# Main program for tests

if __name__ == '__main__':
    lib = COV19Library()
    lib.LoadData("cov19_city.csv")
    lib.buildBST()
    print(lib.cityArray)