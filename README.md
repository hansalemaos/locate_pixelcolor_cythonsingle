# Compiled Cython Code - Detects colors in images 2-3 x faster than Numpy 

### pip install locate-pixelcolor-cythonsingle

#### Tested+compiled against Windows 10 / Python 3.10 / Anaconda

#### If you can't import it, compile it on your system (code at the end of this page)



### How to use it in Python 

```python
import numpy as np
import cv2
from locate_pixelcolor_cythonsingle import search_colors
# 4525 x 6623 x 3 picture https://www.pexels.com/pt-br/foto/foto-da-raposa-sentada-no-chao-2295744/
picx = r"C:\Users\hansc\Downloads\pexels-alex-andrews-2295744.jpg"
pic = cv2.imread(picx)
colors0 = np.array([[255, 255, 255]],dtype=np.uint8)
resus0 = search_colors(pic=pic, colors=colors0)
colors1=np.array([(66,  71,  69),(62,  67,  65),(144, 155, 153),(52,  57,  55),(127, 138, 136),(53,  58,  56),(51,  56,  54),(32,  27,  18),(24,  17,   8),],dtype=np.uint8)
resus1 =  search_colors(pic=pic, colors=colors1)
####################################################################
%timeit resus0 = search_colors(pic=pic, colors=colors0)
51 ms ± 201 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

b,g,r = pic[...,0],pic[...,1],pic[...,2]
%timeit np.where(((b==255)&(g==255)&(r==255)))
150 ms ± 209 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
####################################################################
%timeit resus1 =  search_colors(pic=pic, colors=colors1)
443 ms ± 1.19 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit np.where(((b==66)&(g==71)&(r==69))|((b==62)&(g==67)&(r==65))|((b==144)&(g==155)&(r==153))|((b==52)&(g==57)&(r==55))|((b==127)&(g==138)&(r==136))|((b==53)&(g==58)&(r==56))|((b==51)&(g==56)&(r==54))|((b==32)&(g==27)&(r==18))|((b==24)&(g==17)&(r==8)))
1 s ± 16.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
####################################################################
```


### The Cython Code 

```python
# cython: language_level=3

import numpy as np
cimport numpy as np

cpdef searchforcolor(np.uint8_t[::1] pic, np.uint8_t[::1] colors, int width, int totallengthpic, int totallengthcolor, int[::1] outputx, int[ ::1] outputy, int[::1] lastresult):
    cdef int counter = 0
    cdef unsigned char r, g, b
    cdef int i, j

    for i in range(0, totallengthcolor, 3):
        r = colors[i]
        g = colors[i + 1]
        b = colors[i + 2]
        for j in range(0, totallengthpic, 3):
            if ( r== pic[j]) and (g == pic[j+1]) and (b == pic[j+2]):
                dividend = j // 3
                quotient = dividend // width
                remainder = dividend % width
                outputx[counter] = quotient
                outputy[counter] = remainder
                lastresult[0] = counter
                counter += 1

# .\python.exe .\colorsearchcythonsinglesetup.py build_ext --inplace

```


### setup.py to compile the code 


```python
# cython: language_level=3

from setuptools import Extension, setup
from Cython.Build import cythonize
import numpy as np
ext_modules = [
    Extension("colorsearchcythonsingle", ["colorsearchcythonsingle.pyx"], include_dirs=[np.get_include()],define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")])
]

setup(
    name='colorsearchcythonsingle',
    ext_modules=cythonize(ext_modules),
)


# .\python.exe .\colorsearchcythonsinglesetup.py build_ext --inplace
```


### Alternatives

I wrote a couple of variations of this function. All of them 
can be used in Python.

#### Cython, but with multiple processors (5-10x faster than Numpy)
https://github.com/hansalemaos/locate_pixelcolor_cythonmulti

#### Cupy, using the GPU (up to 8x faster than Numpy)
https://github.com/hansalemaos/locate_pixelcolor_cupy

#### C - shared library (10x faster than Numpy)
https://github.com/hansalemaos/locate_pixelcolor_c

#### C++ - parallel_for - shared library (up to 10x faster than Numpy) 
https://github.com/hansalemaos/locate_pixelcolor_cpp_parallelfor

#### C++ - pragma omp - shared library (20x faster than Numpy)
https://github.com/hansalemaos/locate_pixelcolor_cpppragma

#### Numba - compiled - ahead of time (2-3x faster than numpy)
https://github.com/hansalemaos/locate_pixelcolor_numba

#### Numba Cuda - compiled - ahead of time (10x faster than numpy)
https://github.com/hansalemaos/locate_pixelcolor_numbacuda

