from collections import defaultdict
import matplotlib.pyplot as plt

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

def show_histogram(rainfall_dict, runoff_dict, year_list):
    l=len(year_list)
    if l<1 or l>4:
        raise ValueError("Invalid year list length")
    for index,year in enumerate(year_list):
        rainfall = rainfall_dict[year]
        runoff = runoff_dict[year]
        day=range(1, len(runoff)+1)
        plt.subplot(2,2, index+1)
        plt.tight_layout()
        plt.plot(day, rainfall, 'b-', label='Rainfall')
        plt.plot(day,runoff,'r-', label='Runoff')
        plt.xlabel('Day')
        plt.ylabel('Runoff, Rainfall (mm)')
        plt.title('\nRunoff ' + str(year))
        plt.legend()
    plt.show()

rainfall_dict = read_daily_data('Data/Weather_Data/weather.csv')
runoff_dict =  read_daily_data('Outputs/runoff.csv')
show_histogram(rainfall_dict, runoff_dict, [2011,2012,2013,2014])