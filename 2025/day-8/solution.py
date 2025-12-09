with open(0) as f:
    f = f.readlines()
    f = [[int(y) for y in x.split(",")] for x in f]

class Breaker():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"

    def dist(self, other):
        x_dist = self.x - other.x
        y_dist = self.y - other.y
        z_dist = self.z - other.z
        return x_dist*x_dist+y_dist*y_dist+z_dist*z_dist

    def __hash__(self):
        return hash((self.x,self.y,self.z))

    def __eq__(self,other):
        return hash(self) == hash(other)

class Connection():
    def __init__(self,b1,b2):
        self.breaker1 = b1
        self.breaker2 = b2
        self.breakers = [b1,b2]

    def __repr__(self):
        return f"{self.breaker1}, {self.breaker2}: {len(self)}"

    def __hash__(self):
        return hash(hash(self.breaker1)+hash(self.breaker2))
    
    def __eq__(self, other):
        return hash(self) == hash(other)
        
    def __iter__(self):
        yield self.breaker1
        yield self.breaker2

    def __len__(self):
        return self.breaker1.dist(self.breaker2)

connections = {Connection(Breaker(*line1),Breaker(*line2)) for line1 in f for line2 in f}
connections = sorted(connections, key=lambda c : len(c))
connections = [c for c in connections if len(c) > 0]

circuits = {}
for i, (b1,b2) in enumerate(connections):
    # if i >= 1000: break # UNCOMMENT FOR PART 1

    if b1 not in circuits.keys(): circuits.update({b1:{b1}})
    if b2 not in circuits.keys(): circuits.update({b2:{b2}})

    merged_connections = {*circuits[b1],*circuits[b2]}
    for breaker in circuits[b1]:
        circuits.update({breaker:merged_connections})
    for breaker in circuits[b2]:
        circuits.update({breaker:merged_connections})
    
    # PART 2
    if len(merged_connections) == len(f): 
        print(b1.x*b2.x)
        break

#    for k,v in circuits.items():
#        print(k,v)
#    print("["+str(i)+"] ========================================",b1,b2)

# IGNORE FOR PART 2
sizes = []
checked = []
for k,v in circuits.items():
    if k in checked: continue
    checked.extend(v)
    sizes.append(len(v))

sizes = sorted(sizes, reverse=True)
t=1
for i, size in enumerate(sizes):
    if i >= 3: break
    t*=size
print(t)