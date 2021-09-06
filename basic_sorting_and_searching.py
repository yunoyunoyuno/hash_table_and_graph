import time as T;

def timer(fn,params):
    t1 = T.time();
    fn(params)
    print("Compiled finished : ",T.time() - t1,"sec");
'''
# different btwn array and list.
####linear sum.
def linear_sum(l=[]):
    s = l[0];
    for i in range(1,len(l),1): s += l[i];
    return s;

####sum of sub arrays.
a = [1,2,3,4] # 3 + 5 + 7 = 15.
b = [1,2,3,4,5]
big_a = [i for i in range(20000)];
#brute force alg.
def slow_sums(l = []): # [ 1 2 3 4]
    m = len(l)//2;
    s = 0;
    for i in range(len(l)-m + 1): #
        for j in range(m):
           s += l[i+j];
    return s;

#print(slow_sums(a)); # [ [1 2] [2,3] [3,4] ]
#print(slow_sums([1,2,3,4,5])); # m = 5//2 = 2; [ [1 2] [2 3] [3 4] [4 5]]

def fast_sums(l = []): # [ 1 2 3 4] 
    m = len(l)//2; n = len(l);
    s1,s2 = 0,0
    for i in range(m):
        s1 += l[i];
    s2 = s1;
    for j in range(1,len(l)-m+1):
        s1 += l[m-1 + j] - l[j-1];
        s2 += s1;
    return s2;

timer(fast_sums,big_a);
timer(slow_sums,big_a);
'''

### SORTING

a = [6,4,2,5,3,1,8];
b = [32,23,11,55,18,3,14,28,34,17,92,43,61,0,9,1,52];

#Selection Sort.

def selection_sort(l):
    print(l);
    for i in range(0,len(l)):
        #ให้ตัวน้อยมากสุดในฝั่งซ้ายเป็นตัวน้อยสุด
        mI = i; #จะได้เกิดการย้ายน้อย ๆ
        # หาตัวน้อยสุดในฝั่งขวา
        for j in range(i+1,len(l)):
            if(l[j] < l[mI] ): mI = j;
        #ถ้าเจอตัวน้อยสุดก็สลับ
        if( j < len(l)): l[i],l[mI] = l[mI],l[i];
        print(l);

def insertion_sort(l):
    print(l);
    for i in range(1,len(l)):
        j = i - 1; t = a[i];
        while(j >= 0 and t < a[j]): #ถ้าตัวปัจจุบันน้อยกว่าตัวก่อนหน้า จะเลื่่อน
            a[j+1] = a[j]; j -= 1;
            print(l,"moves",a[j+1]);
        a[j+1] = t; #แทรกตำแหน่งที่เลื่อนไปล่าสุด
        print(l,"insert",t);

#selection_sort(a);
#insertion_sort(a);

def bubble_sort(l):
    is_sorted = True;
    for i in range(len(l)):
        for j in range(1,len(l)):
            if(l[j] < l[j-1]):
                l[j-1],l[j] = l[j],l[j-1];
                print(l);
            is_sorted = False
        if(is_sorted): break;
            
#bubble_sort(a);

def shell_sort(l = []): # Sedgewick
    h = 1;c = 0;
    while (h <= len(l)):
        h = 4**(c+1)+ 3*2**(c)+1; c+=1;
    while(h > 0):
        for m in range(h):
            for i in range(m + h,len(l),h): #insertion sort.
                t = l[i]; j = i-h;
                while(j >= 0 and t < l[j]):
                    l[j+h] = l[j]; j -= h;
                l[j+h] = t;
        if(c == 0): break;
        c-= 1;
        h = 1 if c == 0 else 4**(c)+ 3*2**(c-1)+1

def shell_sort2(l = []): # Sedgewick
    h = len(l)//2
    while(h > 0):
        for m in range(h):
            for i in range(m + h,len(l),h): #insertion sort.
                t = l[i]; j = i-h;
                while(j >= 0 and t < l[j]):
                    l[j+h] = l[j]; j -= h;
                l[j+h] = t;
        h //= 2;

#print("1",b);
#shell_sort2(b);
#print("b",b);
#shell_sort(b);
#print(b);

def __merge(res,L,M,R,l):
    p1 = L; p2 = M+1;
    for k in range(L,R+1):
        if(p1 > M): res[k] = l[p2]; p2 += 1; continue; #ตกขอบขวา เอาขวาไปใส่
        elif(p2 >R):  res[k] = l[p1]; p1 += 1; continue; #ตกขอบซ้ายเอาขวาไปใส่
        elif(l[p1] < l[p2]): res[k] = l[p1]; p1 += 1; #เติมปกติ
        else: res[k] = l[p2]; p2 += 1; #เติมปกติ
    for k in range(L,R+1): l[k] = res[k]; #อัพเดธ
    
    
def __ms(res,L,R,l):
    if(L < R):
        M = (L+R)//2
        __ms(res,L,M,l);
        __ms(res,M+1,R,l);
        __merge(res,L,M,R,l);

def merge_sort(l = []):
    res = [None for i in range(len(l))];
    __ms(res,0,len(l)-1,l);

pile = [7,8,4,6]
#merge_sort(pile)
#print(pile);

#DIMITRY
def merge(a,b):
    i=0; j=0; c=[]
    while i<len(a) and j<len(b): 
        if a[i]<=b[j]: 
            c.append(a[i])
            i=i+1
        else: 
            c.append(b[j])
            j=j+1 
    while i<len(a):
        c.append(a[i]); i=i+1 
    while j<len(b): 
        c.append(b[j]); j=j+1
    return c    

def mergesort(a):
    if len(a)>1: 
        m=int(len(a)/2)
        return merge(mergesort(a[0:m]),mergesort(a[m:len(a)]))
    else: 
        return a


# SinglyLinkedList.
class LinkedList:
    class LinkedNode:
        def __init__(self,e,n):
            self.element = e;
            self.next = n;

    size = 0; head = None; pointer = None;
    def __init__(self,l):
        for i in range(len(l)):
            self.add(self.LinkedNode(l[i],None));
    def length(self): return self.size;
    def add(self, new_node):
        if(new_node == None): return;
        if(self.head == None):
            self.head = new_node;
            self.pointer = new_node;
        else:
            self.pointer.next = new_node;
            self.pointer = new_node;
    def remove(self):
        if(self.head != None): self.head = self.head.next;
    def print(self):
        h = self.head;
        s = "";
        while(h != None):
            s += str(h.element) + " "; h = h.next;
        print(s);

#pileL1 = LinkedList(pile[0:2]);
#pileL2 = LinkedList(pile[2:4]);

#pileL1.print();
#pileL2.print();

def mergeList(L1,L2):
    newlist = LinkedList([]);
    while(L1.head != None and L2.head != None):
        if L1.head.element <= L2.head.element:
            newlist.add(L1.head);
            L1.remove();
        else:
            newlist.add(L2.head);
            L2.remove();
    while(L1.head != None): newlist.add(L1.head);L1.remove();
    while(L2.head != None): newlist.add(L2.head);L2.remove();
    return newlist

#a = mergeList(pileL1,pileL2);
#print(mergesort(pile));

def __qs_m3(d,left,right):
    m = left + (right-left)//2
    if(d[m] > d[left]): d[left],d[m] = d[m],d[left];
    if(d[left] > d[right]): d[left],d[right] = d[right],d[left];
    if(d[m] > d[left]): d[left],d[m] = d[m],d[left];
    
def __qs_partition(l,left,right):
    __qs_m3(l,left,right)
    p = l[left];
    i = left+1; j = right
    while(i <= j): 
        while(p < l[j]): j-= 1
        while(i <= j  and p >= l[i]): i+=1;
        if(i < j): l[i],l[j] = l[j],l[i];#swap;
    l[left],l[j] = l[j],l[left]; #swap i or j
    return j;

def __qs(l,left,right):
    if(left < right): #at least 1 element.
        pI = __qs_partition(l,left,right);
        __qs(l,left,pI-1);
        __qs(l,pI+1,right);
    
def quicksort(l = []):
    __qs(l,0,len(l)-1);

c = [10,2,5,7,8,9]
print(c)
quicksort(c);
print(c);

def percolate_down(l,i,size): # Max Heap.
    c = 2*i+1;
    while( c < size): # while remain left child
        if(c+1 < size and l[c+1] > l[c]): c+= 1 #consider right child.
        if(l[i] >= l[c]): break;
        l[i],l[c] = l[c],l[i];
        i = c;c = 2*i+1

def heap_sort(l = []):
    for i in range(len(l)//2-1,-1,-1):
        percolate_down(l,i,len(l)); # build a heap.
    print(l);
    for j in range(len(l)-1,-1,-1):
        l[0],l[j] = l[j],l[0];
        percolate_down(l,0,j);

l = [70,65,50,20,2,91,25,31,15,8];
print(l);
heap_sort(l);
print(l);

##### SELECT
def partition(arrl,L,R):
    if(L < R):
        # Median of three. mid <= L <= right
        mid = L + (R-L)//2;
        if(arrl[L] > arrl[mid]): arrl[mid],arrl[L] = arrl[L],arrl[mid];
        if(arrl[L] > arrl[R]): arrl[L],arrl[R] = arrl[R],arrl[L];
        if(arrl[mid] > arrl[L]): arrl[mid],arrl[L] = arrl[L],arrl[mid];
        # partition.
        i = L + 1; j = R;#pointer
        p = arrl[L]; # select
        while(i <= j):
            while(arrl[j] > p): j-= 1;
            while(arrl[i] < p): i+= 1;
            if(i < j) : arrl[i],arrl[j] = arrl[j],arrl[i];
        arrl[j],arrl[L] = arrl[L],arrl[j];
        return j

def __qR(arrl,L,R,k):
    if(L==R): return arrl[L];
    j = partition(arrl,L,R);
    m = j-L+1; #จำนวนสมาชิกฝั่งซ้ายรวม 
    if(k == m): return arrl[j];
    elif(k < m):
        return __qR(arrl,L,j-1,k);
    else:
        return __qR(arrl,j+1,R,k-m);

def quick_select(arrl,k):
    return __qR(arrl,0,len(arrl)-1,k)

#k = quick_select(l,2);
#print(k);

def sequential_search(al,k):
    for i in range(len(al)):
        if (al[i] == k): return i;
    return -1;

def binR(d,l,r,k):
    if(l <= r):
        m = l + (r - l)//2;
        if(d[m] == k): return m;
        if(k < d[m]): return binR(d,l,m-1,k);
        else: return binR(d,m+1,r,k);
           
def binary_search2(d,k):
    return binR(d,0,len(d)-1,k);
def binary_search1(d,k):
    l = 0; r = len(d)-1; #pointer.
    while(l <= r ):
        m = l + (r - l)//2;
        if(d[m] == k): return m;
        if(k < d[m]): r = m - 1;
        elif(k > d[m]): l = m+1;
        

a = [2,3,5,6];

for i in range(7):
    m1 = sequential_search(a,i);
    m2 = binary_search2(a,i);
    m3 = binary_search1(a,i);
    print(m1,m2,m3);




















    
