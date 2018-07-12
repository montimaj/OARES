from tkinter import filedialog
from tkinter import *
from functools import partial
from Imports import abm

class oares_gui:
    dem_file = ''
    rainfall_file = ''
    soil_file = ''
    netlogo_dir = ''
    output_dir = ''


    def get_dem_file(self, entry):
        fp = filedialog.askopenfile(initialdir = ".", title = "Select DEM File", filetypes = (("ESRI ASCII files", "*.asc"),))
        if fp:
            self.insert_entry(entry, fp.name)
            self.dem_file = fp.name

    def get_rainfall_file(self, entry):
        fp = filedialog.askopenfile(initialdir = ".", title = "Select Rainfall File", filetypes = (("CSV files", "*.csv"),))
        if fp:
            self.insert_entry(entry, fp.name)
            self.rainfall_file = fp.name

    def get_soil_file(self, entry):
        fp = filedialog.askopenfile(initialdir = ".", title = "Select Soil File", filetypes = (("CSV files", "*.csv"),))
        if fp:
            self.insert_entry(entry, fp.name)
            self.rainfall_file = fp.name

    def get_netlogo_directory(self, entry):
        dir = filedialog.askdirectory(initialdir = ".", title = "Select Netlogo Directory")
        if dir:
            self.insert_entry(entry, dir)
            self.netlogo_dir = dir

    def get_output_directory(self, entry):
        dir = filedialog.askdirectory(initialdir=".", title="Select Output Directory")
        if dir:
            self.insert_entry(entry, dir)
            self.output_dir = dir

    def insert_entry(self, entry, text):
        if text:
            entry.delete(0, END)
            entry.insert(0, text)

    def init_actions(self, root):
        button_texts = ["DEM File", "Rainfall File", "Soil File", "NetLogo App Directory", "Output Directory"]
        action_lists = [self.get_dem_file, self.get_rainfall_file, self.get_soil_file, self.get_netlogo_directory, self.get_output_directory]

        for index, (text, action) in enumerate(zip(button_texts, action_lists)):
            entry = Entry(root, width=20)
            entry.grid(row = index, column = 2)
            button = Button(root, text = text, width = 15, command = partial(action, entry))
            button.grid(row = index, column = 1)

        simbutton = Button(root, text = "Simulate", command = partial(abm.run_simulation, self.netlogo_dir, "oares.nlogo", ))

    def __init__(self):
        root = Tk()
        root.title("OARES")
        self.init_actions(root)
        mainloop()

o1 = oares_gui()