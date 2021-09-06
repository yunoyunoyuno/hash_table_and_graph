#Made by Yuno 

#Require these libraries.
import matplotlib.pyplot as plt 
import sympy; 

#Linear Probing.
class OAHashTable:
    class Entry:
       def __init__(self,k,v):
            self.key = k; self.value = v;

    def __init__(self,m=1):
        if(m <= 0): m = 1;
        self.table = [None]*m;
        self.size = 0;
        self.DELETE = self.Entry(object(),None);
        self.numExistCells = 0;

    def __indexOf(self,key):
        hI = self.__h(key);
        for j in range(len(self.table)):
            e = self.table[hI];
            if(e == None or e.key == key): return hI;
            hI = (hI + 1) % len(self.table);
            
    def __h(self,key):
        key = str(key);
        return (abs(hash(key)))% len(self.table)

    def length(self): return self.size;

    def display(self):
        x,y = [],[];
        for i in range(len(self.table)):
            x.append(i);
            e = self.table[i]
            if(e != None and e != self.DELETE): y.append(1);
            else: y.append(0);
        print("n = ",self.size,"m=",len(self.table),"lambda",self.size/len(self.table));
        plt.bar(x,y,align='edge', width=1);
        plt.show();
    

    def get(self,key):
        hI = self.__indexOf(key);
        e = self.table[hI];
        return None if (e == None or e == self.DELETE) else e.value;

    def put(self,k,v):
        empty = -1;
        oldValue = None;
        hI = self.__h(k);
        
        for j in range(len(self.table)):
            e = self.table[hI]
            if(e == self.DELETE and empty == -1): empty = hI;
            if(e == None or e.key == k): break;
            hI = (hI + 1) % len(self.table);
        
        if(self.table[hI] == None):
            if(empty != -1): hI = empty;
            self.table[hI] = self.Entry(k,v);
            self.size += 1;
            if(empty == -1): self.numExistCells += 1;
            if(self.numExistCells > len(self.table)/2): self.rehash();
            
        elif(self.table[hI].key == k):
            oldValue = self.table[hI].value;
            self.table[hI].value = v;

        return oldValue;

    def remove(self,key):
        hI = self.__indexOf(key);
        if(self.table[hI] != None):
            self.table[hI] = self.DELETE;
            self.size -= 1;

    def rehash(self):
        oldTable = self.table
        self.table = [None] * self.size * 4
        self.size = self.numExistCells = 0;
        for i in range(len(oldTable)):
            entry = oldTable[i]
            if(entry != None and entry != self.DELETE):
                self.put(entry.key,entry.value)
    
#Quardratic Probing.
class OAQDHashTable:
    class Entry:
       def __init__(self,k,v):
            self.key = k; self.value = v;

    def __init__(self,m=1):
        if(m <= 0): m = 1;
        self.size = 0;
        self.DELETE = self.Entry(object(),None);
        self.numExistCells = 0;
        self.table = [None] * self.__nextPrime(m);

    def __indexOf(self,key):
        hI = self.__h(key);
        for j in range(len(self.table)):
            e = self.table[hI];
            if(e == None or e.key == key): return hI;
            hI = (hI + 2*j - 1) % len(self.table);
            
    def __nextPrime(self,n): return sympy.nextprime(n); # include sympy library

    def __h(self,key):
        key = str(key);
        return (abs(hash(key)))% len(self.table)

    def length(self): return self.size;

    def display(self):
        x,y = [],[];
        for i in range(len(self.table)):
            x.append(i);
            e = self.table[i]
            if(e != None and e != self.DELETE): y.append(1);
            else: y.append(0);
        print("n = ",self.size,"m=",len(self.table),"lambda",self.size/len(self.table));
        plt.bar(x,y,align='edge', width=1);
        plt.show();
    

    def get(self,key):
        hI = self.__indexOf(key);
        e = self.table[hI];
        return None if (e == None or e == self.DELETE) else e.value;

    def put(self,k,v):
        empty = -1;
        oldValue = None;
        hI = self.__h(k);
        
        for j in range(len(self.table)):
            e = self.table[hI]
            if(e == self.DELETE and empty == -1): empty = hI;
            if(e == None or e.key == k): break;
            hI = (hI + 2*j-1) % len(self.table);
        
        if(self.table[hI] == None):
            if(empty != -1): hI = empty;
            self.table[hI] = self.Entry(k,v);
            self.size += 1;
            if(empty == -1): self.numExistCells += 1;
            if(self.numExistCells > len(self.table)/2): self.rehash();
            
        elif(self.table[hI].key == k):
            oldValue = self.table[hI].value;
            self.table[hI].value = v;

        return oldValue;

    def remove(self,key):
        hI = self.__indexOf(key);
        if(self.table[hI] != None):
            self.table[hI] = self.DELETE;
            self.size -= 1;

    def rehash(self):
        oldTable = self.table
        self.table = [None] * self.__nextPrime(self.size)* 4
        self.size = self.numExistCells = 0;
        for i in range(len(oldTable)):
            entry = oldTable[i]
            if(entry != None and entry != self.DELETE):
                self.put(entry.key,entry.value)

#Double Hashing
class OADBHashTable:
    class Entry:
       def __init__(self,k,v):
            self.key = k; self.value = v;

    def __init__(self,m=20):
        if(m < 20): m = 20;
        self.size = 0;
        self.DELETE = self.Entry(object(),None);
        self.numExistCells = 0;
        self.table = [None] * self.__nextPrime(m);

    def __nextPrime(self,n): return sympy.nextprime(n); #please include sympy library
    
    def __indexOf(self,key):
        hI = self.__h(key);
        g = self.__g(key);
        for j in range(len(self.table)):
            e = self.table[hI];
            if(e == None or e.key == key): return hI;
            hI = (hI + g) % len(self.table);
    def __g(self,key):
        key = str(key);
        return 11 - (abs(hash(key)))% 11
    
    def __h(self,key):
        key = str(key);
        return (abs(hash(key)))% len(self.table)

    def length(self): return self.size;

    def display(self):
        x,y = [],[];
        for i in range(len(self.table)):
            x.append(i);
            e = self.table[i]
            if(e != None and e != self.DELETE): y.append(1);
            else: y.append(0);
        print("n = ",self.size,"m=",len(self.table),"lambda",self.size/len(self.table));
        plt.bar(x,y,align='edge', width=1);
        plt.show();
    

    def get(self,key):
        hI = self.__indexOf(key);
        e = self.table[hI];
        return None if (e == None or e == self.DELETE) else e.value;

    def put(self,k,v):
        empty = -1;
        oldValue = None;
        hI = self.__h(k);
        g = self.__g(k);
        
        for j in range(len(self.table)):
            e = self.table[hI]
            if(e == self.DELETE and empty == -1): empty = hI;
            if(e == None or e.key == k): break;
            hI = (hI + g) % len(self.table);
        
        if(self.table[hI] == None):
            if(empty != -1): hI = empty;
            self.table[hI] = self.Entry(k,v);
            self.size += 1;
            if(empty == -1): self.numExistCells += 1;
            if(self.numExistCells > len(self.table)/2): self.rehash();
            
        elif(self.table[hI].key == k):
            oldValue = self.table[hI].value;
            self.table[hI].value = v;

        return oldValue;

    def remove(self,key):
        hI = self.__indexOf(key);
        if(self.table[hI] != None):
            self.table[hI] = self.DELETE;
            self.size -= 1;

    def rehash(self):
        oldTable = self.table
        self.table = [None] * self.size * 4
        self.size = self.numExistCells = 0;
        for i in range(len(oldTable)):
            entry = oldTable[i]
            if(entry != None and entry != self.DELETE):
                self.put(entry.key,entry.value)

#Testing
                
h2 = OAHashTable();
h3 = OAQDHashTable();
h4 = OADBHashTable()
n = 1000; #if n = 1000000 the performance between hash table and array will be shown.


for i in range(n):
    h2.put(i,i);
for i in range(n):
    if(type(h2.get(i))!= int): print(i,"RIP");
print("Open Adreessing Linear probing HashTable OK");

for i in range(n):
    h3.put(i,i);
for i in range(n):
    if(type(h3.get(i))!= int): print(i,"RIP");
print("Open Adreessing Quardratic probing HashTable OK");

for i in range(n):
    h4.put(i,i);
for i in range(n):
    if(type(h4.get(i))!= int): print(i,"RIP");
print("Open Adreessing Double Hashing HashTable OK");

print("PASS");

arr = []

for i in range(n):
    arr.append(i);
for i in range(n):
    if(not i in arr): print(i,"RIP");
print("ArrayList is OK");

# If use n > 1000 please comment this code.
h2.display();
h3.display();
h4.display();
