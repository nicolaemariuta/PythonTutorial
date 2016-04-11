from numpy import *

## An example
print("An example")
a = arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)

print(type(a))
b = array([6,7,8])
print(type(b))


## Array creation
print("\nArray creation")
a = array([2,3,4])
print(a)
print(a.dtype)
b = array([1.2,3.5,5.1])
print(b)
print(b.dtype)

# wrong: a = array(1,2,3,4)
# right: a = array([1,2,3,4])

b = array([(1.5,2,3) , (4,5,6) ])
print(b)

#specify type of array at creation time
c = array([ [1,2], [3,4] ], dtype = complex)
print(c)

#create array that are originally unknown, but its size is known
print(zeros((3,4)))
print (ones((2,3,4), dtype = int16))
print (empty( (2,3) ))

#create sequences of numbers
print(arange(10,30,5))
print(arange(0,2,0.3))

#linspace also takes as argument the number of elements we want
print(linspace(0,2,9))   # 9 numbers from 0 to 2
x = linspace(0,2*pi,100)  # useful to evaluate function at lots of points
f = sin(x)
print(x)
print(f)


## Printing arrays
print("Printing arrays")
a = arange(6)  # 1d array
print(a)
b = arange(12).reshape(4,3)   # 2d array
print(b)
c = arange(24).reshape(2,3,4)
print(c)
print ( arange(10000) )
print ( arange(10000).reshape(100,100) )


## Basic Operations
print("Basic Operations")
a = array([20,30,40,50])
b = arange(4)
c = a-b
disp(c)
disp(b**2)
disp(10*sin(a))
disp(a<35)
#dot multiplication
A = array([[1,1],[0,1]])
B = array([[2,0],[3,4]])
print(A*B)
print(dot(A,B))
#operators += and *=
a = ones((2,3), dtype=float)
b = random.random((2,3))
a *= 3
print(a)
b += a
print(b)
a += b
print(a)
#upcasting behavior
a = ones(3, dtype=int32)
b = linspace(0,pi,3)
print (b.dtype.name)
c = a+b
print(c)
print (c.dtype.name)
d = exp(c*1j)
print(d)
print (d.dtype.name)
#unary operations of ndarray class
a = random.random((2,3))
print(a)
print(a.sum())
print(a.min())
print(a.max())
# apply unary operations by specifying axis parameter
b = arange(12).reshape(3,4)
print(b)
print(b.sum(axis=0))
print(b.min(axis=1))
print(b.cumsum(axis=1))

## Universal functions
print("Universal functions")
B = arange(3)
print(B)
print(exp(B))
print(sqrt(B))
C = array([2. , -1 , 4.])
print(add(B,C))

## Indexing, Slicing and Iterating
print("Indexing, Slicing and Iterating")
#One-dimensional arrays are much like lists
a = arange(10)**3
print(a)
print(a[2])
print(a[2:5])
a[:6:-2] = -1000
print(a)
print (a[ : :-1])
a = arange(10)**3
for i in a:
    print (i **(1/3.))

#Multidimensional arrays can have one index per axis. These indices are given in a tuple separated by commas:
def f(x,y):
    return 10*x+y

b = fromfunction(f,(5,4),dtype = int)
print(b)
print(b[2,3])
print(b[0:5, 1])
print(b[ :, 1])
print(b[1:3, : ])
print(b[-1])

# the dots represent as many colons as needed to produce a complete indexing tuple
c = array( [ [[ 0, 1, 2], [ 10, 12, 13]], [[ 100, 101, 102], [ 110, 112, 113]] ] )
print (c.shape)
print (c[1,...])
print (c[...,2])

# iterating over multidimensional arrays done with respect to the first axis
for row in b:
    print(row)
for element in b.flat:
    print(element)


## Shape manipulation
print('Shape manipulation')
a = floor(10*random.random((3,4)))
print(a)
print(a.shape)
print(a.ravel())
a.shape = (6,2)
print(a.transpose())
print(a)
a.resize(2,6)
print(a)
a = a.reshape(3,-1)
print(a)

## Stacking together different arrays
print('Stacking together different arrays')
a = floor(10*random.random((2,2)))
print(a)
b = floor(10*random.random((2,2)))
print(b)

print(vstack((a,b)))
print(hstack((a,b)))
print(column_stack((a,b)))

a = array([4.,2.])
b = array([2.,8.])

print(a[:,newaxis])

print(column_stack((a[:,newaxis],b[:,newaxis])))
print(vstack((a[:,newaxis],b[:,newaxis])))
print(r_[1:4,0,4])

a = floor(10*random.random((2,12)))
print(hsplit(a,3))
print(hsplit(a,(3,4)))

## Copies and Views
print('Copies and Views')
a = arange(12)
b = a
print(b is a)
b.shape = 3,4
print(a.shape)

def f(x):
    print(id(x))


print (id(a))
f(a)
#view or shallow copy
c = a.view()
print(c is a)
print(c.base is a)
print(c.flags.owndata)
c.shape = 2,6
print(a.shape)
c[0,4] = 1234
print(a)
# slicing and array
s = a[:,1:3]
a[:]= 10
print(a)
#copy method
d = a.copy()
print(d is a)
print(d.base is a)
d[0,0] = 9999
print(a)

## Fancy indexing and indexing tricks
print('Fancy indexing and indexing tricks')
a = arange(12)**2
i = array([1,1,3,8,5])
print(a[i])
j = array([[3,4], [9,7]])
print(a[j])

palette = array( [ [0,0,0],
                   [255, 0, 0],
                   [0, 255, 0],
                   [0, 0, 255],
                   [255, 255, 255] ])


image = array([ [0,1,2,0],
                [0,3,4,0] ])

print(palette[image])


a = arange(12).reshape(3,4)
print(a)
i = array([ [0,1],
            [1,2] ])
j = array([ [2,1],
            [3,3] ])

print(a[i,j])
print(a[i,2])
print(a[:,j])

l = [i,j]
print(a[l])

s = array([i,j])
#print(a[s])
print(a[tuple(s)])


# serch of the maxium value of time-dependent series
time = linspace(20,145,5)    # time scale
data = sin(arange(20)).reshape(5,4) # 4 time-dependent series
print(time)
print(data)
ind = data.argmax(axis = 0)  # index of the macxima for each series
print(ind)
time_max = time[ind]
data_max = data[ind, range(data.shape[1])] # => data[ind[0],0], data[ind[1],1]...
print(time_max)
print(data_max)
print(all(data_max == data.max(axis=0)))

# indexing with boolean arrays
a = arange(12).reshape(3,4)
b = a > 4
print(b)
print(a[b])
a[b] = 0
print(a)

a = arange(12).reshape(3,4)
b1 = array([False, True, True])
b2 = array([True, False, True, False])
print(a[b1,:])
print(a[b1])
print(a[:, b2])
print(a[b1,b2])

# the ix_() function
a = array([2,3,4,5])
b = array([8,5,4])
c = array([5,4,6,8,3])
ax,bx,cx = ix_(a,b,c)
print(ax)
print(bx)
print(cx)

print(ax.shape)
print(bx.shape)
print(cx.shape)

result = ax+bx*cx
print(result)
print(result[3,2,4])
print(a[3]+b[2]*c[4])

#implement reduce
def ufunc_reduce(ufct, *vectors):
    vs = ix_(*vectors)
    r = ufct.identity
    for v in vs:
        r = ufct(r,v)
    return r

print(ufunc_reduce(add,a,b,c))



























