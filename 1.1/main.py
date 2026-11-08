import numpy as np



# a = np.array([ [1, 2, 3], [2, 3, 4], [3, 4, 5]], dtype=np.float32)

# b = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# a = a.astype(np.int32)

# mask = np.array([True, False, True])
# binary = mask.astype(int)
# c = np.full((2, 4), np.random.randint(0, 10), dtype=np.int8)
# print(c)


# #np.arange([start,] stop[, step], dtype=None)
# # С дробным шагом
# np.arange(0, 1, 0.2)
# np.linspace(0, 1, 5)
# # array([0.  , 0.25, 0.5 , 0.75, 1.  ])
# #arange — «я знаю, с каким шагом идти» (шаг = 0.5, сколько точек выйдет — как получится).

# #linspace — «я знаю, сколько точек мне нужно получить на отрезке» (нужно ровно 50 точек, шаг NumPy посчитает сам).

# print(c.ndim)#

#3
np.zeros(10)    
#6google 
a = np.zeros((10))
a[4] = 1
#7google
np.arange(10,50)
#9 google
matrix = np.arange(9).reshape(3,3)
#11
np.eye  
#12 ai 50/50
np.full((3,3), np.random.randint(0, 100))
np.random.randint(0, 100, size=(3,3))
#own
massive = np.arange(20).reshape(4, 5)
print(massive)
print(massive.shape)
print(massive.ndim)
print(massive.dtype)
print(massive.size)
print(massive.nbytes)
massive = massive.astype(np.float32)
print(massive.nbytes)

#done :DD first lesson was nice