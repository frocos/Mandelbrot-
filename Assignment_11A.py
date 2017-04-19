
#Filename: dictionaries.py
#Title: 3 Mandelbrot III


import numpy as np
import matplotlib.pyplot as plt 

res = 300

x = np.arange(-2.5,1.0,1/res)
y = np.arange(-1.5,1.5,1/res)
xx, yy = np.meshgrid(x, y, sparse=False)
c = xx + yy*1j

nn = np.zeros((len(y),len(x)))

def f(c,z=0): 
    for n in range(100):
        z = z**2 + c
        if (abs(z) > 2): 
            return n
    
for i in range(len(y)):
        for j in range(len(x)):
            nn[i,j] = f(c[i,j])
            
plt.imshow(nn)
plt.savefig('mandelbrot_lowres.pdf')




# Optized Code

res = 500
x = np.arange(-2.5,1.0,1./res)
y = np.arange(-1.5,1.5,1/res)
xx, yy = np.meshgrid(x, y, sparse=False)
c = xx + yy*1j


def mandelbrot_set(c, i_max=100):
    opt = np.zeros((len(y),len(x)), dtype=complex)
    l = np.ones((len(y),len(x)) , dtype=int)
    
    for n in range(i_max):
        opt = np.add(np.square(opt),c)
        l[np.abs(opt)>2] = n
    return l
    

plt.imshow(mandelbrot_set(c))
plt.savefig('mandelbrot_highres_1.pdf')


res = 100
x = np.arange(-0.5,0.5,1./res)
y = np.arange(-0.5,0.5,1/res)
xx, yy = np.meshgrid(x, y, sparse=False)
c = xx + yy*1j

plt.imshow(mandelbrot_set(c))
plt.savefig('mandelbrot_highres_2.pdf')
   
        
