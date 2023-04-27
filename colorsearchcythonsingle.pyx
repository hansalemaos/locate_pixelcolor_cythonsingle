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
