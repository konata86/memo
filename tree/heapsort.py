
class HeapSort:

    #配列上のidx1とidx2の値を交換
    def swap(self, arr, idx1, idx2):
        temp = arr[idx1]
        arr[idx1] = arr[idx2]
        arr[idx2] = temp
        return arr

    # arr[left]~arr[right]までをヒープ化
    def heap(self, arr, left, right):
        temp = arr[left] # 根

        parent = left
        while(parent < (right + 1) // 2):
            cl = parent * 2 + 1 # 左の子
            cr = cl + 1 # 右の子

            # child: 大きい方の子
            if(cr <= right and arr[cr] > arr[cl]):
                child = cr
            else:
                child = cl
            
            if(temp >= arr[child]):
                break
            arr[parent] = arr[child]
            parent = child
        arr[parent] = temp

        return arr        

    # ヒープソートします
    def heapSort(self, arr):
        length = len(arr)

        i = (length - 1)//2 # 一番最後のノードの親ノード
        while(i >= 0):
            arr = self.heap(arr, i, length - 1)
            i -= 1
        i = length - 1 
        while(i > 0):
            arr = self.swap(arr, 0, i) # 最大要素とソートされていない部分の末尾要素を交換
            arr = self.heap(arr, 0, i - 1) # arr[0]~arr[i-1]をヒープ化 
            i -= 1
        
        return arr


def main():
    
    heap_sort = HeapSort()

    numbers = [32, 2, 8, 11, 25, 140, 62, 10, 90]
    sorted = heap_sort.heapSort(numbers)

    print("Input : {}".format(numbers))
    print("Sorted: {}".format(sorted))

if __name__ == "__main__":
    main()
