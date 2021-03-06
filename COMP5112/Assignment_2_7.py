heap=[22,18,20,17,3,16,14,7,12,19,9]

def minheap(heap,i):
    left=2*i+1
    right=2*i+2
    if left<len(heap) and heap[left]<heap[i]:
        small=left
    else:
        small=i
    if right<len(heap) and heap[right]<heap[small]:
        small=right
    if small!=i:
        heap[small],heap[i] = heap[i],heap[small]
        minheap(heap,small)

n = int(len(heap)//2-1)
for i in range(n,-1,-1):
    minheap(heap,i)
    
print(heap)
