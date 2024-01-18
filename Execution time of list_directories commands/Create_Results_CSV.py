# This file creates folders with random names in the selected directory.
# The considered value is approximately 2000 folders, which you can change.
# It should be noted that these subfolders are in the main branch and there
# are no other subfolders inside them. During the creation of these folders,
# the necessary commands are executed, and their time is measured.
# These calculations are performed inside the file Time_Calculator, and the
# result is returned in the form of a list. For greater accuracy, each calculation
# is performed 10 times, and the estimated average time is in milliseconds. Finally,
# the obtained results are saved as a file named Results.csv.

from Time_Calculator import Execution_Time_Calculator
import random
import os
from Make_Randome_Name import Make_randome_folder_name

#Root directory path
directory = "D:/Test"

#This function creates directories with random names.
def make_new_directories(directory, numbers):
    for _ in range(numbers):
        Folder_Name_len = random.randint(1,100)
        os.makedirs(os.path.join(directory,Make_randome_folder_name(Folder_Name_len)), exist_ok=True)

#This function calculates the execution time of each command and returns the results
# in a suitable format for saving in a CSV file
def get_results():
    Results = [len(os.listdir(directory))]+Execution_Time_Calculator(directory)
    Str = ",".join(map(str,Results))
    return Str

#The results are saved in the file 'Results.csv'
def main():
    FileHead = open("Results.csv", "a")

    for _ in range(100):
        make_new_directories(directory, 20)
        Str = get_results()
        FileHead.write(Str+"\n")
        
    FileHead.close()

main()