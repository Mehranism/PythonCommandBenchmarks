# How to Use the Git Repository

This repository contains several files that are designed to perform specific tasks. This guide will walk you through the steps to properly use each file and understand their functionalities.

## Create_Results_CSV.py

The `Create_Results_CSV.py` file is responsible for creating folders with random names in the selected directory. By default, it creates approximately 2000 folders, but you have the flexibility to change this value. It's important to note that these subfolders are created directly in the main branch and do not contain any additional subfolders within them.

During the folder creation process, the file executes the necessary commands and measures their execution time. These calculations are performed within the `Time_Calculator.py` file, and the results are returned as a list. To ensure accuracy, each calculation is performed 10 times, and the average time is reported in milliseconds. Finally, the obtained results are saved as a file named `Results.csv`.

## Make_Random_Name.py

The `Make_Random_Name.py` file is used to generate random names for directories. The `Make_random_folder_name` function generates strings of a given length by combining random combinations of lowercase and uppercase English letters and numbers. If you require additional characters in the random name generation process, you can add them to the `Valid_chars` string within the file.

## Time_Calculator.py

The `Time_Calculator.py` file is employed to calculate the execution time of commands. It includes the `Execution_Time_Calculator` function, which is used to calculate the execution time (in milliseconds) for a series of commands. The function returns a list of five elements, representing the execution time in descending order for the following commands: `os_scandir()`, `os_walk()`, `glob.glob()`, `pathlib_iterdir()`, and `os_listdir()`.

## Visualize_Results.py

The `Visualize_Results.py` file is responsible for visualizing the results related to the execution time of each of the following commands: `os_scandir()`, `os_walk()`, `glob.glob()`, `pathlib_iterdir()`, and `os_listdir()`. These results are stored in the `Results.csv` file, based on the number of folders present in the directory. The file generates a graphical representation of the results in the form of an output image (`output.png`).

## Results.csv

The `Results.csv` file contains the results of the project. It includes the execution times of the commands for different scenarios, allowing you to analyze and compare the performance.

## output.png

The `output.png` file represents the graphical visualization of the results obtained from the `Visualize_Results.py` file. It provides a visual representation of the execution times of the commands, aiding in the interpretation and understanding of the data.

Please refer to the specific files' documentation and comments within the code for further details on their usage and customization.

Feel free to explore and utilize the repository's files according to your needs and requirements.

For any further assistance or inquiries, please don't hesitate to reach out.

Happy coding!