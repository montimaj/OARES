from collections import defaultdict
from Imports import image_matrix as Mat

def clean_data_list(data_list):
    cleaned_list=[]
    for data in data_list:
        data = data.strip()
        data = data.strip('"')
        cleaned_list.append(data)
    return cleaned_list

def read_daily_data(data_file):
    fp = open(data_file, 'r')
    data = fp.readlines()[1:]
    fp.close()
    data_dict = defaultdict(lambda: [])
    for values in data:
        values = values.split(',')
        values = clean_data_list(values)
        year = int(values[-2].split('/')[2])
        value = float(values[-1])
        data_dict[year].append(value)
    return data_dict

def read_dem_data(dem_file):
    fp = open(dem_file, 'r')
    dem_data = fp.readlines()[6:]
    fp.close()
    dem_values=[]
    for values in dem_data:
        values = values.split(' ')
        values = clean_data_list(values)
        dem_values.append(values)
    return Mat.new_matrix(dem_values)

def segment_change_list(change_list):
    deposit, erosion, no_change = [], [], []
    for value in change_list:
        if value == 0:
            deposit.append(0)
            erosion.append(0)
            no_change.append(0)
        elif value < 0:
            erosion.append(value)
            deposit.append(0)
            no_change.append(0)
        else:
            erosion.append(0)
            deposit.append(value)
            no_change.append(0)
    return deposit, erosion, no_change

def new_list(list_of_lists):
    newlist = []
    for l in list_of_lists:
        for value in l:
            newlist.append(value)
    return newlist
