import numpy
import skimage.io
import matplotlib.pyplot
import math

strings_input = "hw5_dataset/i_testing/obj12__21.bmp"
img01 = skimage.io.imread(strings_input)
height, width = img01.shape

print(height, width)
end_height, end_width = height // 8, width // 8 #16, 16
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
            if numpy_array01[array_number + var_total_label] == 0.0:
                numpy_array01[array_number + var_total_label] = 0.0
            else:
                numpy_array01[array_number + var_total_label] = (numpy_array01[array_number + var_total_label]) / sum_result
        array_number += 9
        end_width += 16

    end_width = 16
    end_height += 16

#print(numpy_array01)

#testing img =============================================================================================
euclidean_distance_DB = numpy.zeros(420, dtype=numpy.float32)
list_name_file = []

for n in range(1, 21, 1):
    for input_counting_picture_end in range(21):
        img01_testing = skimage.io.imread("hw5_dataset/j_training/obj" + str(n) + "__" + str(input_counting_picture_end)
                                          + ".bmp")
        list_name_file.append("hw5_dataset/j_training/obj" + str(n) + "__" + str(input_counting_picture_end)
                                          + ".bmp")
        end_height_testing, end_width_testing = height // 8, width // 8  # 16 16
        total_move_x_testing, total_move_y_testing = end_height_testing, end_width_testing

        numpy_array01_testing = numpy.zeros(576, dtype=numpy.float32)
        array_number_testing = 0

        for x_move_testing in range(0, height, total_move_x_testing):
            for y_move_testing in range(0, width, total_move_y_testing):
                for x_testing in range(1 + x_move_testing, end_height_testing - 1, 1):
                    for y_testing in range(1 + y_move_testing, end_width_testing - 1, 1):
                        gx_testing = img01_testing[x_testing + 1, y_testing].astype(numpy.int32) - img01_testing[
                            x_testing - 1, y_testing].astype(numpy.int32)
                        gy_testing = img01_testing[x_testing, y_testing + 1].astype(numpy.int32) - img01_testing[
                            x_testing, y_testing - 1].astype(numpy.int32)
                        if gx_testing == 0:
                            if gy_testing != 0:
                                deg_testing = 90
                            if gy_testing == 0:
                                deg_testing = 0
                        else:
                            deg_testing = (math.atan(gy_testing / gx_testing) * (180 / math.pi))
                            if deg_testing < 0:
                                deg_testing = (deg_testing + math.pi * (180 / math.pi))
                        if gx_testing == 0 and gy_testing == 0:
                            Gxy_testing = 0
                        else:
                            Gxy_testing = math.sqrt(gx_testing ** 2 + gy_testing ** 2)
                        var_testing = int(deg_testing) // 20
                        numpy_array01_testing[array_number_testing + var_testing] += Gxy_testing
                temp_count_testing = array_number_testing
                sum_result_testing = 0
                for total_counting_testing in range(temp_count_testing, temp_count_testing + 9, 1):
                    sum_result_testing = numpy_array01_testing[total_counting_testing] + sum_result_testing
                for var_total_label_testing in range(9):
                    if numpy_array01_testing[array_number_testing + var_total_label_testing] == 0.0:
                        numpy_array01_testing[array_number_testing + var_total_label_testing] = 0.0
                    else:
                        numpy_array01_testing[array_number_testing + var_total_label_testing] = (numpy_array01_testing[
                                                                                                     array_number_testing + var_total_label_testing]) / sum_result_testing
                array_number_testing += 9
                end_width_testing += 16
            end_width_testing = 16
            end_height_testing += 16

        euclidean_distance = 0.0
        total_temp_picking = 0.0
        for picking_counting in range(576):
            total_temp_picking += ((numpy_array01[picking_counting] - numpy_array01_testing[picking_counting]) ** 2)
        euclidean_distance_DB[input_counting_picture_end + 21 * (n - 1)] = abs(math.sqrt(total_temp_picking))

min_value = euclidean_distance_DB[0]
min_value_tag = 0
print(euclidean_distance_DB)
for choosing_count in range(420):
    if euclidean_distance_DB[choosing_count] < min_value:
        min_value = euclidean_distance_DB[choosing_count]
        min_value_tag = choosing_count

print("ANS", min_value_tag, min_value)
print("==>", list_name_file[min_value_tag])
matplotlib.pyplot.figure().canvas.set_window_title("input")
skimage.io.imshow(strings_input)
matplotlib.pyplot.figure().canvas.set_window_title("result")
skimage.io.imshow(list_name_file[min_value_tag])
skimage.io.show()
