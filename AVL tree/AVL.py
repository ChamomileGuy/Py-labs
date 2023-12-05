class TreeNode:
    def __init__(self,key,left=None,right=None,parent=None):
        self.key = key
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

    def replaceNodeData(self,key,lc,rc):
        self.key = key
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class AVLTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def view(self):
        count=0
        try:
            self._view(self.root,count)
        except AttributeError:
            print(" ")
        
    def _view(self,currentNode,count):
        print("**"*count+str(currentNode.key),end="")
        if not currentNode.isRoot():
            if currentNode.isLeftChild():
                print(" (left)")
            else:
                print(" (right)")
        else:
            print(" (root)")
        if not currentNode.hasLeftChild() is None:
            count+=1
            self._view(currentNode.hasLeftChild(),count)
            count-=1
        if not currentNode.hasRightChild() is None:
            count+=1
            self._view(currentNode.hasRightChild(),count)
            count-=1


    def put(self,key):
        if self.root:
            self._put(key,self.root)
        else:
            self.root = TreeNode(key)
        self.size = self.size + 1

    def _put(self,key,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self,node):
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

    def rotateLeft(self,rotRoot):
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
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self,rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rebalance(self,node):
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

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res
            else:
                return None
        else:
            return None


def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False



print("Это программа, реализующая AVL-дерево с добавлением и отображением элементов")
print("Для создания элемента введите 'put число'")
print("Для просмотра структуры дерева введите 'view'")
print("Для выхода из программы введите 'exit'")
inp=input()
mytree = AVLTree()
while inp!="exit":
    arr=inp.split()
    if inp=="view":
        mytree.view()
    elif arr[0]=="put" and is_digit(arr[1]) and len(arr)==2:
        mytree.put(float(arr[1]))
    else:
        print("Некорректный ввод, операция не была выполнена")
    inp=input()

