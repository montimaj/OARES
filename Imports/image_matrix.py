import numpy as np
from PIL import Image

def new_matrix(list_of_lists):
    new_list = []
    for l in list_of_lists:
        row = []
        for value in l:
            row.append(int(value))
        new_list.append(row)
    return np.matrix(new_list)

def get_change_mat(dem_mat1, dem_mat2):
    return dem_mat2 - dem_mat1

def normalize_mat(mat):
    return mat/np.max(mat)

def mat_to_list(mat):
    row, col = mat.shape
    new_list = []
    for i in range(row):
        for j in range(col):
            new_list.append(mat[i, j])
    return new_list

def scale_value(value, bit=8):
    max_val = 2**bit -1
    if value == 0:
        return 0, 0, 0
    elif value < 0:
        return max_val, 0, 0
    return 0, max_val, 0

def generate_change_raster(change_mat):
    cols, rows = (change_mat.shape[1], change_mat.shape[0])
    change_raster = Image.new('RGB', (cols, rows))
    for i in range(rows):
        for j in range(cols):
            pval = scale_value(change_mat[i, j])
            change_raster.putpixel((j,i), pval)
    return change_raster
