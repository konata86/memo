import random

class Node:
    
    def __init__(self, data):
        self.data  = data # ノード値
        self.left  = None # 左の子
        self.right = None # 右の子
    
class BinarySearchTree:

    def __init__(self):
        self.root = None
    
    def getTree(self):
        return self.root
    
    # 2分木を作る
    def insert(self, data):
        if self.root is None: # ルートがNone
            self.root = Node(data)
        else:
            self._insert(data, self.root)
        
    def _insert(self, data, node):
        if data < node.data:
            if node.left is not None:
                self._insert(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._insert(data, node.right)
            else:
                node.right = Node(data)
        
    # 幅優先探索    
    def search(self, key):
        if self.root == None:
            return 
        else:
            self._search(key, self.root)

    def _search(self, key, node):

        # 探索の失敗
        if node is None:
            print('The key: {} was not existed.'.format(key))
        
        else:
            if key == node.data:
                print('Get the key: {}'.format(node.data))
            elif key > node.data: # keyが対象ノード値より大きい
                self._search(key, node.right) # 右の子要素へ
            else: # keyが対象ノード値より小さい
                self._search(key, node.left) # 左の子要素へ     


def main():

    data = list(range(0, 20))
    random.seed(0)
    random.shuffle(data)
    print("Input: {}".format(data))

    bst = BinarySearchTree()
    
    for n in data:
        bst.insert(n)
    
    key = 9
    bst.search(key)


if __name__ == "__main__":
    main()
