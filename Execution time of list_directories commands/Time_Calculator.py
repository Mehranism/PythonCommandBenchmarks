def Execution_Time_Calculator(directory):
    #The "Execution_Time_Calculator" function is used to calculate the
    # execution time (im ms) of a series of commands. It ultimately returns a
    # list of five elements, representing the execution time (in ms) in descending
    # order for the following commands: os_scandir(), os_walk(), glob.glob(),
    # pathlib_iterdir(), and os_listdir().

    import time
    import os
    from glob import glob
    from pathlib import Path

    #The variable "RUNS" specifies the number of times each of the commands
    # should be executed. It is embedded in the code to repeat each command
    # multiple times and obtain a more accurate average execution time.
    RUNS = 10


    #To estimate the execution time of the os_walk() command
    def run_os_walk():
        a = time.time_ns()
        for i in range(RUNS):
            fu = [x[0] for x in os.walk(directory)]
        return ((time.time_ns() - a) / 1000 / 1000 / RUNS)

    #To estimate the execution time of the glob.glob() command
    def run_glob():
        a = time.time_ns()
        for i in range(RUNS):
            fu = glob(directory + "/*/")
        return ((time.time_ns() - a) / 1000 / 1000 / RUNS)

    #To estimate the execution time of the pathlib_iterdir() command
    def run_pathlib_iterdir():
        a = time.time_ns()
        for i in range(RUNS):
            dirname = Path(directory)
            fu = [f for f in dirname.iterdir() if f.is_dir()]
        return ((time.time_ns() - a) / 1000 / 1000 / RUNS)

    #To estimate the execution time of the os_listdir() command
    def run_os_listdir():
        a = time.time_ns()
        for i in range(RUNS):
            dirname = Path(directory)
            fu = [os.path.join(directory, o) for o in os.listdir(directory) if os.path.isdir(os.path.join(directory, o))]
        return ((time.time_ns() - a) / 1000 / 1000 / RUNS)

    #To estimate the execution time of the os_scandir() command
    def run_os_scandir():
        a = time.time_ns()
        for i in range(RUNS):
            fu = [f.path for f in os.scandir(directory) if f.is_dir()]
        return ((time.time_ns() - a) / 1000 / 1000 / RUNS)



    return [run_os_scandir(), run_os_walk(), run_glob(), run_pathlib_iterdir(), run_os_listdir()]
