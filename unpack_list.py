

list = (1,24,("hi", 43),6,7,"Hello")
a, b, c, d, e, f = list;

print(b)

#Error not enough values to unpack (expected 3, got 2)
#g = (1, 2) 
#x, y, z = g 


data = [1,24,("hi", 43),6,7,"Hello"]

_, m,_,n,_,_ = data

print(n) #6
