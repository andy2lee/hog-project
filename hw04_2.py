import numpy
import skimage.io
import matplotlib.pyplot
import math

img01 = skimage.io.imread("lena512_8bit.bmp")
height, width = img01.shape

#array_new = numpy.zeros((height, width), dtype=numpy.uint8)
print(height, width)
end_height, end_width = height // 8, width // 8 #64, 64
total_move_x, total_move_y = end_height, end_width
numpy_array01 = numpy.zeros(576, dtype=numpy.float32)
array_number = 0

for x_move in range(0, height, total_move_x):
    for y_move in range(0, width, total_move_y):
        for x in range(1 + x_move, end_height - 1, 1):
            for y in range(1 + y_move, end_width - 1, 1):
                gx = img01[x + 1, y].astype(numpy.int32) - img01[x - 1, y].astype(numpy.int32)
                gy = img01[x, y + 1].astype(numpy.int32) - img01[x, y - 1].astype(numpy.int32)
                if gx == 0:
                    if gy != 0:
                        deg = 90
                    if gy == 0:
                        deg = 0
                else:
                    deg = (math.atan(gy / gx) * (180 / math.pi))
                    if deg < 0:
                        deg = (deg + math.pi * (180 / math.pi))
                if gx == 0 and gy == 0:
                    Gxy = 0
                else:
                    Gxy = math.sqrt(gx ** 2 + gy ** 2)
                var = int(deg) // 20
                numpy_array01[array_number + var] += Gxy
        temp_count = array_number
        sum_result = 0
        for total_counting in range(temp_count, temp_count + 9, 1):
            sum_result = numpy_array01[total_counting] + sum_result
        for var_total_label in range(9):
            numpy_array01[array_number + var_total_label] = (numpy_array01[array_number + var_total_label]) / sum_result
        array_number += 9
        end_width += 64
    end_width = 64
    end_height += 64

print(numpy_array01)
matplotlib.pyplot.figure().canvas.set_window_title("HOG")
matplotlib.pyplot.xticks(numpy.arange(0, 576, 50))
matplotlib.pyplot.bar(numpy.arange(576), numpy_array01, align="center", linewidth=0, color="red")
matplotlib.pyplot.show()
