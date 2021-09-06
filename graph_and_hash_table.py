class GraphAdjMatrix:
    def __init__(self,n):
        self.order = n;
        self.adj = [[0]*n for i in range(n)];
        
    def display(self):
        print("ADJMatrix","order :",self.order,"\n");
        s = "";
        for v in range(len(self.adj)): s += str(v) + "\t";
        print("\t",s,"\n");
        for i,a in enumerate(self.adj):
            s = "";
            for e in a: s += str(e) + "\t";
            print(i,"\t",s);
        print("\n");
        
    def __validate_input(self,v):
        if(v < 0 or v > len(self.adj)):
            return "Invalid vertex";

    def getOrders(self): return self.order;    

    def addVertices(self,n=1):
        if( n < 0): return self.____validate_input(n);
        order = self.order; n += order;
        mat = [[0]*n for i in range(n)];

        for i in range(order):
            for j in range(order):
                mat[i][j] = self.adj[i][j];
                

        self.order = n; self.adj = mat;

    def removeVertex(self,v):
        e = self.__validate_input(v);
        if(e): return e;
        self.order -= 1;

        for i in range(len(self.adj)):
            self.adj[i][v] = None;
            for j in range(len(self.adj)):
                self.adj[v][j] = None;


    def addArc(self,v1,v2):
        e = self.__validate_input(v1);
        if(not e): e = self.__validate_input(v2);
        if(e): return e;
        
        if(v1 == v2): return "please use different vertex"
        else: self.adj[v1][v2] = 1;

    def removeArc(self,v1,v2):
        e = self.__validate_input(v1);
        if(not e): e = self.__validate_input(v2);
        if(e): return e;
        if(v1 == v2): return "please use different vertex"
        else: self.adj[v1][v2] = 0;

    def addEdge(self,v1,v2):
        e = self.addArc(v1,v2);
        if(e): return e
        self.addArc(v2,v1);

    def removeEdge(self,v1,v2):
       
        e = self.removeArc(v1,v2);
        if(e): return e
        self.removeArc(v2,v1);

    def nbhs(self,v):
        e = self.__validate_input(v);
        if(e): return e;
        a = [];

        for c in range(len(self.adj)):
            if(self.adj[v][c] == 1): a.append(c);
        return None if a == [] else a;
        
                
          

M = GraphAdjMatrix(4);
      
# calling methods
M.addEdge(0, 1);
M.addEdge(0, 2);
M.addEdge(1, 2);
M.addEdge(2, 3);
# the adjacency matrix created
M.display();
  
# adding a vertex to the graph
M.addVertices();
# connecting that verex to other existing vertices
M.addEdge(4, 1);
M.addEdge(4, 3);
# the adjacency matrix with a new vertex
M.display();
      
# removing an existing vertex in the graph
M.removeVertex(1);
# the adjacency matrix after removing a vertex
M.display();


class GraphAdjList:
            
    def __init__(self,n):
        self.order = n;
        self.adj = [None] * n;

    def getOrders(self): return self.order; 

    def __validate_input(self,v): 
        if(v < 0 or v > len(self.adj)): return "Invalid vertex"
    
    def addVertices(self,n = 1):
        if(n < 0): return self.__validate_input(n);
        for i in range(n): self.adj.append(None);
        self.order += n;

    def addArc(self,v1,v2):
        err = self.__validate_input(v1);
        if(not err): err = self.__validate_input(v2);
        if(err): return err;

        if(self.adj[v1] == None): self.adj[v1] = [];
        elif(v2 in self.adj[v1]): return;
        self.adj[v1].append(v2);

        
    def removeArc(self,v1,v2):
        err = self.__validate_input(v1);
        if(not err): err = self.__validate_input(v2);
        if(err): return err;
        
        if(self.adj[v1] != None and v2 in self.adj[v1]):
            self.adj[v1].remove(v2);
        if(self.adj[v1] == []): self.adj[v1] = None;

    def addEdge(self,v1,v2):
        err = self.addArc(v1,v2)
        if(err): return err;
        self.addArc(v2,v1)

    def removeEdge(self,v1,v2):
        err = self.removeArc(v1,v2)
        if(err): return err;
        self.removeArc(v2,v1)
        
    def removeVertex(self,v):
        if(v < 0): return self.__validate_input(v);
        self.adj[v] = None; self.order -= 1;
        for i in range(len(self.adj)):
            if(self.adj[i] != None and v in self.adj[i]):
                self.adj[i].remove(v);

    def nbhs(self,v): 
        err = self.__validate_input(v);
        if(err): return err;
        else : return self.adj[v];
        
    
    def display(self):
        print("ADJ List","order :",self.order);
        for i,e in enumerate(self.adj): print(i,e);
            
        


G = GraphAdjList(4);

G.display();
G.addEdge(0, 1);
G.addEdge(0, 2);
G.addEdge(1, 2);
G.addEdge(2, 3);
# the adjacency matrix created
G.display();
  
# adding a vertex to the graph
G.addVertices();
# connecting that verex to other existing vertices
G.addEdge(4, 1);
G.addEdge(4, 3);
# the adjacency matrix with a new vertex
G.display();
      
# removing an existing vertex in the graph
G.removeVertex(1);
# the adjacency matrix after removing a vertex
G.display();
