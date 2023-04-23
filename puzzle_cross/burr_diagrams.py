import matplotlib.colors as mc
import colorsys

import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import colors
import math

# Transpose the array to show z-axis vertically, x-axis to the right, and y-axis into our face
def transpose(mma):
    Nz = len(mma)
    Ny = len(mma[0])
    result = []

    for y in range(Ny):
        subresult = []
        for z in range(Nz):
            subresult.append(mma[(Nz-1)-z][y])
        result.append(subresult)




    return result

def getArray(mma):
    result = []
    for layer in mma:
        subresult = []
        for line in layer:
            line2 = line.replace(" ", "")
            line3 = line2.replace(".", "0")
            subresult.append([int(x) for x in list(line3)])
        result.append(subresult)
    return result




theC = ["#ffffff", "#cccccc", "#8DD3C7", "#FFFFB3", "#BEBADA", "#FB8072", "#80B1D3", "#FDB462", "#B3DE69", "#FCCDE5"]





# https://stackoverflow.com/questions/37765197/darken-or-lighten-a-color-in-matplotlib
def lighten_color(color, amount=0.5):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)
    """

    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])


def dimetric(mma, shaded):
    global theC
    fig, ax = plt.subplots()
    plt.gcf().set_size_inches(10, 8)

    ax.axis('equal')

    mm = getArray(mma)
    cellsize = 0.12
    dx = 0.58
    dy = 0.41

    Nz = len(mm)
    Ny = len(mm[0])
    Nx = len(mm[0][0])

    # print("mm = {}".format(mm))

    for zz in range(Nz):
        print("Level {}".format(zz))
        for yy in range(Ny):
            for xx in range(Nx):
                if mm[zz][yy][xx] > 0:
                    print(mm[zz][yy][xx], end=' ')
                else:
                    print('.', end=' ')
            print()

    for zz in range(Nz):
        for yy in range(Ny):
            for xx in range(Nx):
                if mm[zz][yy][xx] in [1,2,3,4,5,6,7,8,9]:
                    C1 = theC[int(mm[zz][yy][xx])]

                    # pretskata kvadratins
                    vertX = [(x + (Nz - zz)*dx)*cellsize for x in [xx-1, xx, xx, xx-1, xx-1]]
                    vertY = [(y + (Nz - zz)*dy)*cellsize  for y in [yy-1, yy-1, yy, yy, yy-1]]
                    plt.plot(vertX, vertY, '-k', zorder=(zz+1))
                    plt.fill(vertX, vertY, C1, zorder=(zz+1))

                    # virsskata kvadratins
                    if shaded:
                        C2 = lighten_color(C1, 0.4)
                    else:
                        C2 = C1
                    vertX = [(x + (Nz - zz) * dx) * cellsize for x in [xx-1, xx, xx+dx, xx-1+dx, xx-1]]
                    vertY = [(y + (Nz - zz) * dy) * cellsize for y in [yy, yy, yy+dy, yy+dy, yy]]
                    plt.plot(vertX, vertY, '-k', zorder=(zz+1))
                    plt.fill(vertX, vertY, C2, zorder=(zz+1))

                    # labaa saanskata kvadraatinjsh
                    if shaded:
                        C3 = lighten_color(C1, 1.6)
                    else:
                        C3 = C1
                    vertX = [(x + (Nz-zz) * dx) * cellsize for x in [xx, xx+dx, xx+dx, xx, xx]]
                    vertY = [(y + (Nz - zz) * dy) * cellsize for y in [yy-1, yy-1+dy, yy+dy, yy, yy-1]]
                    plt.plot(vertX, vertY, '-k', zorder=(zz+1))
                    plt.fill(vertX, vertY, C3, zorder=(zz+1))

    plt.show()


# isometric < - function(dims, mma, shaded)
# {
# mm < - getArray(dims, mma)
# cellsize < - 0.12
# Nx < - dim(mm)[1]
# Ny < - dim(mm)[2]
# Nz < - dim(mm)[3]
# alpha < - pi / 7
# dx < - cos(alpha)
# dy < - sin(alpha)
# # dz <- 3/4
#
# if (shaded) {
# theGP < - list("1" = gpar(col = "black", fill="white", lwd = 1.5),
# "2" = gpar(col = "black", fill="#dddddd", lwd = 1.5),
# "3" = gpar(col = "black", fill="#bbbbbb", lwd = 1.5))
# } else {
# theGP < - list("1" = gpar(col = "black", fill="white", lwd = 1.5),
# "2" = gpar(col = "black", fill="#28AE7B", lwd = 1.5))
# }
#
# for (zz in 1:Nz) {
# for (yy in 1:Ny) {
# for (xx in 1:Nx) {
# if (mm[xx, yy, zz] > 0) {
# # pretskata kvadraatinjsh (skataas uz kreiso pusi)
# if (shaded) {
# gp1 < - theGP[["2"]]
# } else {
# gp1 < - theGP[[as.character(mm[xx, yy, zz])]]
# }
# grid.polygon(x = (c((xx-1) * dx, xx * dx, xx * dx, (xx-1) * dx)+(Nz-zz) * dx) * cellsize,
# y = (c(yy-1 + (Nx - xx + 1) * dy,
# yy-1 + (Nx - xx) * dy,
# yy + (Nx - xx) * dy,
# yy + (Nx - xx + 1) * dy) + (Nz-zz) * dy) * cellsize,
# gp=gp1)
# # virsskata kvadraatinjsh
# if (shaded) {
# gp2 < - theGP[["1"]]
# } else {
# gp2 < - theGP[[as.character(mm[xx, yy, zz])]]
# }
# grid.polygon(x = (c((xx-1) * dx,
# xx * dx,
# xx * dx+dx,
# (xx-1) * dx+dx) + (Nz-zz) * dx) * cellsize,
# y = (c(yy + (Nx - xx + 1) * dy,
# yy + (Nx - xx) * dy,
# yy + (Nx - xx) * dy + dy,
# yy + (Nx - xx + 1) * dy + dy) + (Nz-zz) * dy) * cellsize,
# gp=gp2)
# # labaa saanskata kvadraatinjsh
# if (shaded) {
# gp3 < - theGP[["3"]]
# } else {
# gp3 < - theGP[[as.character(mm[xx, yy, zz])]]
# }
# grid.polygon(x = (c(xx * dx, xx * dx, xx * dx+dx, xx * dx+dx) + (Nz-zz) * dx) * cellsize,
# y = (c(yy-1 + (Nx - xx) * dy,
# yy + (Nx - xx) * dy,
# yy + (Nx - xx) * dy + dy,
# yy-1 + (Nx - xx) * dy + dy) + (Nz-zz) * dy) * cellsize,
# gp=gp3)
#
# }
# }
# }
# }
# }




def main():
    # Z-layers starting from the bottom
    mms3F = [
        [". .",
         ". .",
         ". .",
         "3 ."],
        [". .",
         ". .",
         ". .",
         "3 ."],
        ["1 .",
         "1 .",
         "1 .",
         "2 2"]]

    mms3Ffixed = [
        ["1.",
         "..",
         ".."],
        ["1.",
         "..",
         ".."],
        ["1.",
         "..",
         ".."],
        ["22",
         "3.",
         "3."]
    ]


    dimetric(transpose(mms3F), False)




if __name__ == '__main__':
    main()