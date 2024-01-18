# The results related to the execution time of each of the commands
# 'os_scandir()', 'os_walk()', 'glob.glob()', 'pathlib_iterdir()',
# and 'os_listdir()' are saved in the file 'Results.csv' based on the
# number of folders present in the directory. This file plots these
# results in a graphical format

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Path = "Results.csv"
def ReadCSV(Path):
    headers = ["os_scandir()", "os_walk()", "glob.glob()", "pathlib_iterdir()", "os_listdir()"]
    df = pd.read_csv(Path, index_col=0, header=None)
    df.columns = headers
    return df

def Plot_Results(df):
    ax = df.plot(title = "Execution time")
    ax.set_xlabel("numbers of directories")
    ax.set_ylabel("time (in ms)")

def main():
    df = ReadCSV(Path)
    Plot_Results(df)
    
main()