import matplotlib.pyplot as plt
import numpy as np
from Imports import data_list as DL, image_matrix as Mat

def show_dem_change_plot(change_mat, cell_size):
    change_list = Mat.mat_to_list(change_mat)
    deposit, erosion, no_change = DL.segment_change_list(change_list)
    deposit = pixels_to_meters(deposit, cell_size)
    erosion = pixels_to_meters(erosion, cell_size)
    obs = range(1, len(change_list) + 1)
    plt.tight_layout()
    plt.plot(obs, deposit, label='Deposit')
    plt.plot(obs, erosion, label='Erosion')
    plt.plot(obs, no_change, 'k-', label='No Change')
    plt.xlabel('Pixels')
    plt.ylabel('Values (meters)')
    plt.title('Soil Erosion vs Deposit (1979-2014)')
    plt.legend()
    plt.show()

def show_yearwise_plot(rainfall_dict, runoff_dict, year_list):
    l=len(year_list)
    if l<1 or l>4:
        raise ValueError("Invalid year list length")
    for index,year in enumerate(year_list):
        rainfall = rainfall_dict[year]
        runoff = runoff_dict[year]
        day=range(1, len(runoff)+1)
        plt.subplot(2,2, index+1)
        plt.tight_layout()
        plt.plot(day, rainfall, 'c-', label='Rainfall')
        plt.plot(day,runoff,'r-', label='Runoff')
        plt.xlabel('Day')
        plt.ylabel('Rainfall, Runoff (mm)')
        plt.title('\nRainfall, Runoff ' + str(year))
        plt.legend()
    plt.show()

def show_full_plot(rainfall_dict, runoff_dict):
    total_rainfall = DL.new_list(list(rainfall_dict.values()))
    total_runoff = DL.new_list(list(runoff_dict.values()))
    day = range(1, len(total_rainfall) + 1)
    plt.plot(day, total_rainfall, 'c-', label='Rainfall')
    plt.plot(day, total_runoff, 'r-', label='Runoff')
    plt.xlabel('Day')
    plt.ylabel('Rainfall, Runoff (mm)')
    plt.title("Total Rainfall vs Runoff (1979-2014)")
    plt.legend()
    plt.show()

    r = round(np.corrcoef(total_rainfall, total_runoff)[0, 1],3)
    z=np.polyfit(total_rainfall, total_runoff, 2)
    f = np.poly1d(z)
    new_x = np.linspace(0, max(total_rainfall), len(total_rainfall))
    new_y = f(new_x)
    plt.plot(new_x, new_y, 'r-', label="y = 0.003357x^2 + 0.01181x - 0.06723, R = " + str(r))
    plt.plot(total_rainfall, total_runoff, 'bo')
    plt.xlabel('Rainfall (mm)')
    plt.ylabel('Runoff (mm)')
    plt.title("Rainfall-Runoff Regression Fit (1979-2014)")
    plt.legend()
    plt.show()

def pixels_to_meters(mat, cell_size):
    return Mat.mat_to_list(np.matrix(mat)*111.5*cell_size*1000)

def generate_results(weather_file, runoff_file, input_dem, eroded_dem, year_list, cell_size):
    rainfall_dict = DL.read_daily_data(weather_file)
    runoff_dict = DL.read_daily_data(runoff_file)
    original_dem_mat = DL.read_dem_data(input_dem)
    eroded_dem_mat = DL.read_dem_data(eroded_dem)
    show_full_plot(rainfall_dict, runoff_dict)
    show_yearwise_plot(rainfall_dict, runoff_dict, year_list)
    change_mat = Mat.get_change_mat(original_dem_mat, eroded_dem_mat)
    show_dem_change_plot(change_mat, cell_size)
    Mat.generate_change_raster(change_mat).save('Outputs/image.png')