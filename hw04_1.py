import matplotlib.pyplot
import numpy
import skimage.io

img01 = skimage.io.imread("lena512_8bit.bmp")
height, width = img01.shape

array = numpy.zeros(256, dtype=numpy.uint32)
for x in range(height):
    for y in range(width):
        array[img01[x, y].astype(numpy.int32)] += 1
'''
print(array)
'''
matplotlib.pyplot.xticks(numpy.arange(0, 256, 20))
matplotlib.pyplot.bar(numpy.arange(256), array, align="center", width=1, linewidth=0, color="red")
#matplotlib.pyplot.hist(list, bins="auto", color='red', edgecolor="none")
matplotlib.pyplot.show()
