# Open Agent-based Runoff and Erosion Simulation (OARES) tool
from Imports import hydrographs as hydro, clean_file as cf

original_dem = 'Data/asan_dem.asc'
weather_file = 'Data/Weather_Data/weather.csv'
runoff_file= 'Outputs/runoff_new.csv'
input_resampled_hydro = 'Outputs/resampled_cleaned.asc'
input_eroded_hydro = 'Outputs/eroded_cleaned.asc'
out_resampled= 'Outputs/input_resampled.asc'
out_eroded = 'Outputs/output_eroded.asc'
year_list = [1979, 1989, 1999, 2009]

try:
    cf.generate_new_dem_file(original_dem, out_resampled, input_resampled_hydro)
    cell_size = cf.generate_new_dem_file(original_dem, out_eroded, input_eroded_hydro)
    hydro.generate_results(weather_file, runoff_file, input_resampled_hydro, input_eroded_hydro, year_list, cell_size)
except (ValueError, IOError) as error:
    print(error)