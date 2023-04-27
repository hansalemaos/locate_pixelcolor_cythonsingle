from colorsearchcythonsingle import searchforcolor
import numpy as np
def search_colors(pic, colors):
    if not isinstance(colors, np.ndarray):
        colors = np.array(colors, dtype=np.uint8)
    totallengthcolor = (colors.shape[0] * colors.shape[1]) - 1
    totallenghtpic = (pic.shape[0] * pic.shape[1] * pic.shape[2]) - 1
    outputx = np.zeros(totallenghtpic, dtype=np.int32)
    outputy = np.zeros(totallenghtpic, dtype=np.int32)
    endresults = np.zeros(1, dtype=np.int32)
    width = pic.shape[1]
    picb = pic.ravel()
    colorsb = colors.ravel()
    searchforcolor(
        picb,
        colorsb,
        width,
        totallenghtpic,
        totallengthcolor,
        outputx,
        outputy,
        endresults,
    )
    return np.dstack([outputx[: endresults[0] + 1], outputy[: endresults[0] + 1]])[0]


