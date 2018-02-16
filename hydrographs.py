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
        plt.plot(day, rainfall, 'b-', label='Rainfall')
        plt.plot(day,runoff,'r-', label='Runoff')
        plt.xlabel('Day')
        plt.ylabel('Rainfall, Runoff (mm)')
        plt.title('\nRainfall, Runoff ' + str(year))
        plt.legend()
    plt.show()


def new_list(list_of_lists):
    newlist = []
    for l in list_of_lists:
        for value in l:
            newlist.append(value)
    return newlist

def show_full_plot(rainfall_dict, runoff_dict):
    total_rainfall = new_list(list(rainfall_dict.values()))
    total_runoff = new_list(list(runoff_dict.values()))
    day = range(1, len(total_rainfall) + 1)
    plt.plot(day, total_rainfall, 'b-', label='Rainfall')
    plt.plot(day, total_runoff, 'r-', label='Runoff')
    plt.xlabel('Day')
    plt.ylabel('Rainfall, Runoff (mm)')
    plt.title("45 Years Plot!")
    plt.legend()
    plt.show()

rainfall_dict = read_daily_data('Data/Weather_Data/weather.csv')
runoff_dict =  read_daily_data('Outputs/runoff.csv')
show_full_plot(rainfall_dict, runoff_dict)
show_yearwise_plot(rainfall_dict, runoff_dict, [2010,2011,2012,2013])