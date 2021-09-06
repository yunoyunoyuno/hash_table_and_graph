#Made by Yuno

import matplotlib.pyplot as plt


class SeperateChaining:
    class LinkedNode:
        def __init__(self,k,v,n):
            self.key = k; self.value = v; self.next_node= n;
    
    table,size = [],0
    load_factor = 2;
    def __init__(self,m=1):
        if(m <= 0): m =1;
        self.table = [None]*m;
    
    def __h(self,key):
        key = str(key);
        return abs(hash(key))%len(self.table);

    def __getNode(self,key):
        n = self.table[self.__h(key)];
        while(n != None and not n.key == key ): n = n.next_node;
        return n;

    def length(self): return self.size;

    def get(self,key):
        node = self.__getNode(key);
        return node if node == None else node.value
        
    def put(self,key,value):
        node = self.__getNode(key);
        oldvalue = None;
        if(node != None):
            oldvalue = node.value;
            node.value = value;
        else:
            i = self.__h(key);
            self.table[i] = self.LinkedNode(key,value,self.table[i]);
            self.size += 1;
        if(self.size/len(self.table) > self.load_factor): self.rehash();
        return oldvalue;
    
    def delete(self,key):
        i = self.__h(key);
        if(self.table[i] == None): return;
        if(self.table[i].key == key):
            self.table[i] = self.table[i].next_node; self.size -= 1;
        else:
            prev = self.table[i];
            while(prev.next_node != None and  prev.next_node.key != key):
                prev = prev.next_node;
                
            if(prev.next_node != None):
                prev.next_node = prev.next_node.next_node;
                self.size -= 1;

    def display(self):
        x,y = [],[];
        for i in range(len(self.table)):
            x.append(i);
            firstnode = self.table[i];
            item_list = [];
            while(firstnode != None):
                item_list.append((firstnode.key,firstnode.value));
                firstnode = firstnode.next_node
            y.append(len(item_list));
        print("table length : ",len(self.table));
        plt.bar(x,y);
        plt.show();

    def rehash(self):
        oldtable = self.table[:];
        newChain = SeperateChaining(2*len(self.table));
        for i in range(len(oldtable)):
            firstnode = oldtable[i];
            item_list = [];
            while(firstnode != None):
                item_list.append(firstnode)
                firstnode = firstnode.next_node
            for j in range(len(item_list)):
                k,v = item_list[j].key,item_list[j].value;
                newChain.put(k,v);
        self.size = newChain.length();
        self.table = newChain.table;

n = 1000; # try n about 100000
h = SeperateChaining();
for i in range(n):
    h.put(i,i);
for i in range(n):
    if(type(h.get(i))!= int): print(i,"RIP");
print("Seperate Chaining Hashing HashTable OK");

print("PASS");

arr = []

for i in range(n):
    arr.append(i);
for i in range(n):
    if(not i in arr): print(i,"RIP");
print("ArrayList is OK");

h.display(); #if you try n about 100000 plese comment this line.
