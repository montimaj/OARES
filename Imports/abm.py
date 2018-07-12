from Imports import hydrographs as hydro, clean_file as cf
from subprocess import Popen

def run_simulation(nlogo_path, model_path, original_dem, out_resampled, out_eroded, weather_path, curve_path, output_path):
    prefix = " '"
    suffix = "'"
    nlogo_path = prefix + nlogo_path + suffix
    model_path = prefix + model_path + suffix
    original_dem = prefix + '"' + original_dem + '"' + suffix
    out_resampled = prefix + '"' + out_resampled + '"' + suffix
    out_eroded = prefix + '"' + out_eroded + '"' + suffix
    weather_path = prefix + weather_path + suffix
    curve_path = prefix + curve_path + suffix
    output_path = prefix + output_path + suffix
    args =  nlogo_path + model_path + original_dem + out_resampled + out_eroded + weather_path + curve_path + output_path
    proc_list = ['Rscript --vanilla Imports/rcode.R' + args]
    proc = Popen(proc_list, shell = True)
    proc.wait()

def show_results(original_dem, weather_file, runoff_file, input_resampled_hydro, input_eroded_hydro, out_resampled, out_eroded, year_list, output_dir):
    try:
        cf.generate_new_dem_file(original_dem, out_resampled, input_resampled_hydro)
        cell_size = cf.generate_new_dem_file(original_dem, out_eroded, input_eroded_hydro)
        hydro.generate_results(weather_file, runoff_file, input_resampled_hydro, input_eroded_hydro, year_list, cell_size, output_dir)
    except (ValueError, IOError) as error:
        print(error)

nlogo_path = "/home/monti/Downloads/SW/NetLogo-6.0.2/app"
model_path = "/home/monti/Documents/Projects/OARES/oares.nlogo"
original_dem = "/home/monti/Documents/Projects/OARES/Data/asan_dem.asc"
weather_path = "/home/monti/Documents/Projects/OARES/Data/Weather_Data/weather.csv"
curve_path = "/home/monti/Documents/Projects/OARES/Data/Soil_Data/curve_number.csv"
output_dir = "/home/monti/Documents/Projects/OARES/Outputs"
runoff_path = output_dir + "/runoff.csv"
out_resampled = output_dir + "/input_resampled.asc"
out_eroded = output_dir + "/output_eroded.asc"
#run_simulation(nlogo_path, model_path, original_dem, out_resampled, out_eroded, weather_path, curve_path, runoff_path)

input_resampled_hydro = output_dir + "/resampled_cleaned.asc"
input_eroded_hydro = output_dir + "/eroded_cleaned.asc"
year_list = [1998, 1999, 2000, 2001]
show_results(original_dem, weather_path, runoff_path, input_resampled_hydro, input_eroded_hydro, out_resampled, out_eroded, year_list, output_dir)
